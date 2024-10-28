const std = @import("std");
const Allocator = std.mem.Allocator;

const allocator = std.heap.c_allocator;

const stdout = std.io.getStdOut().writer();
const stdin = std.io.getStdIn().reader();

const WriteError = std.posix.WriteError;
const ReadError = std.posix.ReadError;

const Error = Allocator.Error || WriteError || ReadError;

var should_stop = false;

fn send_message(msg: []const u8) WriteError!void {
    try stdout.writeAll(msg);
    return stdout.writeAll("\n");
}

fn send_message_comptime(comptime msg: []const u8) WriteError!void {
    return stdout.writeAll(msg ++ "\n");
}

fn send_message_raw(msg: []const u8) WriteError!void {
    return stdout.writeAll(msg);
}

const LogType = enum {
    UNKNOWN,
    ERROR,
    MESSAGE,
    DEBUG,
};

fn send_log_f(comptime log_type: LogType, comptime fmt: []const u8, args: anytype) (WriteError || Allocator.Error)!void {
    const out = try std.fmt.allocPrint(allocator, @tagName(log_type) ++ " " ++ fmt ++ "\n", args);
    defer allocator.free(out);
    return send_message_raw(out);
}

fn send_log_c(comptime log_type: LogType, comptime msg: []const u8) WriteError!void {
    return send_message_comptime(@tagName(log_type) ++ " " ++ msg);
}

fn handle_about(_: []const u8) WriteError!void {
    const bot_name = "zig_template";
    const about_answer = "name=\"" ++ bot_name ++ "\", version=\"0.42\"";

    return send_message_comptime(about_answer);
}

fn handle_start(_: []const u8) !void {
    // Handle end
}

fn handle_end(_: []const u8) !void {
    should_stop = true;
}

fn handle_info(msg: []const u8) !void {
    // Handle infos
    _ = msg;
}

fn handle_begin(_: []const u8) !void {
    // Handle begin
}

fn handle_turn(msg: []const u8) !void {
    // Handle turn
    _ = msg;
}

fn handle_board(_: []const u8) !void {
    // Handle board
}

const CommandMapping = struct {
    cmd: []const u8,
    func: *const fn ([]const u8) Error!void,
};

const command_mappings: []const CommandMapping = &[_]CommandMapping{
    .{ .cmd = "ABOUT", .func = handle_about },
    .{ .cmd = "START", .func = handle_start },
    .{ .cmd = "END", .func = handle_end },
    .{ .cmd = "INFO", .func = handle_info },
    .{ .cmd = "BEGIN", .func = handle_begin },
    .{ .cmd = "TURN", .func = handle_turn },
    .{ .cmd = "BOARD", .func = handle_board },
};

fn handle_command(cmd: []const u8) !void {
    for (command_mappings) |mapping| {
        if (std.ascii.startsWithIgnoreCase(cmd, mapping.cmd)) {
            return @call(.auto, mapping.func, .{cmd});
        }
    }
    return send_log_c(.UNKNOWN, "command is not implemented");
}

pub fn main() !void {
    var read_buffer: [256]u8 = undefined;
    while (!should_stop) {
        // Just hope a command is not bigger than the read buffer :)
        const cmd = try stdin.readUntilDelimiterOrEof(&read_buffer, '\n');
        // EOF handling
        if (cmd == null)
            break;
        try handle_command(cmd.?);
    }
}
