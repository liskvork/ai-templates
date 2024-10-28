#!/usr/bin/env python3

import sys
from typing_extensions import Callable
from enum import Enum


should_stop: bool = False


def handle_about(msg: str) -> None:
    bot_name = "python_template"
    print(f'name="{bot_name}", version="0.42"')


def handle_start(msg: str) -> None: ...


def handle_end(msg: str) -> None:
    global should_stop
    should_stop = True


def handle_info(msg: str) -> None: ...


def handle_begin(msg: str) -> None: ...


def handle_turn(msg: str) -> None: ...


def handle_board(msg: str) -> None: ...


class LogType(Enum):
    UNKNOWN = 0
    ERROR = 1
    MESSAGE = 2
    DEBUG = 3

    def __str__(self):
        return f"{self.name}"


def send_log(log_type: LogType, msg: str):
    print(f"{str(log_type)} {msg}")


COMMAND_MAPPINGS: dict[str, Callable[[str], None]] = {
    "ABOUT": handle_about,
    "START": handle_start,
    "END": handle_end,
    "INFO": handle_info,
    "BEGIN": handle_begin,
    "TURN": handle_turn,
    "BOARD": handle_board,
}


def handle_command(cmd: str) -> None:
    cmd_u = cmd.upper()
    if cmd_u not in COMMAND_MAPPINGS:
        return send_log(LogType.UNKNOWN, "command is not implemented")
    return COMMAND_MAPPINGS[cmd_u](cmd)


def main() -> int:
    while not should_stop:
        try:
            cmd = input()
        except EOFError:
            return 0
        handle_command(cmd)
    return 0


if __name__ == "__main__":
    sys.exit(main())
