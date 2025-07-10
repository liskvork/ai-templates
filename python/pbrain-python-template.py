#!/usr/bin/env python3

import os
import logging
import sys

from enum import Enum, auto
from typing import Callable


logger = logging.getLogger(__name__)

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
    UNKNOWN = auto()
    ERROR = auto()
    MESSAGE = auto()
    DEBUG = auto()

    def __str__(self):
        return self.name


def send_log(log_type: LogType, msg: str):
    print(log_type, msg)


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
    cmd_u = cmd.split()[0].upper()

    command_handler = COMMAND_MAPPINGS.get(cmd_u)
    if command_handler is None:
        return logger.warning("command is not implemented")

    return command_handler(cmd)


def main() -> int:
    logging.basicConfig(level=logging.DEBUG)

    while not should_stop:
        try:
            cmd = input()
        except (KeyboardInterrupt, EOFError):
            return os.EX_OK
        handle_command(cmd)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
