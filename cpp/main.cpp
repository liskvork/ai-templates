#include <array>
#include <cstdint>
#include <functional>
#include <iostream>
#include <string>
#include <string_view>
#include <unordered_map>

namespace {

bool SHOULD_STOP = false;

enum log_type : std::uint8_t {
  UNKNOWN,
  ERROR,
  MESSAGE,
  DEBUG,
};

const std::unordered_map<log_type, std::string_view> LOG_TYPE_MAPPINGS{
    {UNKNOWN, "UNKNOWN"},
    {ERROR, "ERROR"},
    {MESSAGE, "MESSAGE"},
    {DEBUG, "DEBUG"},
};

auto send_log(log_type type, const std::string_view &msg) -> void {
  std::cout << LOG_TYPE_MAPPINGS.at(type) << " " << msg << std::endl;
}

auto handle_about([[maybe_unused]] std::string &cmd) -> void {
  constexpr std::string_view bot_name = "cpp_template";
  std::cout << "name=\"" << bot_name << "\", version=\"0.42\"" << std::endl;
}

auto handle_start(std::string &cmd) -> void {
  // Handle start
}

auto handle_end([[maybe_unused]] std::string &cmd) -> void {
  SHOULD_STOP = true;
}

auto handle_info(std::string &cmd) -> void {
  // Handle info
}

auto handle_begin(std::string &cmd) -> void {
  // Handle begin
}

auto handle_turn(std::string &cmd) -> void {
  // Handle turn
}

auto handle_board(std::string &cmd) -> void {
  // Handle board
}

struct CommandMapping {
  std::string_view cmd;
  std::function<void(std::string &)> func;
};

const std::array<CommandMapping, 7> COMMAND_MAPPINGS{{
    {
        "ABOUT",
        handle_about,
    },
    {
        "START",
        handle_start,
    },
    {
        "END",
        handle_end,
    },
    {
        "INFO",
        handle_info,
    },
    {
        "BEGIN",
        handle_begin,
    },
    {
        "TURN",
        handle_turn,
    },
    {
        "BOARD",
        handle_board,
    },
}};

auto handle_command(std::string &cmd) -> void {
  std::string token = cmd.substr(0, cmd.find(' '));
  for (const auto &i : COMMAND_MAPPINGS) {
    if (i.cmd == token) {
      i.func(cmd);
      return;
    }
  }
  send_log(UNKNOWN, "command is not implemented");
}

} // namespace

auto main() -> int {
  for (std::string line; !SHOULD_STOP && std::getline(std::cin, line);) {
    handle_command(line);
  }
  return 0;
}
