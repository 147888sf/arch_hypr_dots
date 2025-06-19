import os
import re
import sys
import termios
import tty

from colorama import Back, Fore, Style

from tools.log_tools import log


def ansi_aware_center(text: str, width: int) -> str:
    stripped_text = re.sub(r"\x1b\[([0-9;]+)m", "", text)
    text_length = len(stripped_text)

    if text_length >= width:
        return text

    total_padding = width - text_length
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding

    return " " * left_padding + text + " " * right_padding


def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == "\x1b":
            ch += sys.stdin.read(2)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def bool_selection(question: str, default_state=True, full_screen=True):
    selection = default_state

    while 1:
        os.system("clear")
        w, h = os.get_terminal_size()
        print("\n" * (round(h / 2) - 1) + f"{question}".center(w))
        print(
            "\n"
            + ansi_aware_center(
                f"{f'{Back.WHITE}{Fore.BLACK}Yes{Style.RESET_ALL}   No' if selection else f'Yes   {Back.WHITE}{Fore.BLACK}No{Style.RESET_ALL}'}",
                w,
            )
        )

        key = get_key()

        if key == "\x1b[C":
            selection = not selection
        elif key == "\x1b[D":
            selection = not selection
        elif key == "\r":
            os.system("clear")
            break
        else:
            print(key)

    log(f'Bool selection: "{question}": "{selection}"')
    return selection


def list_selection(question, list):
    selection = 0

    while 1:
        os.system("clear")
        w, h = os.get_terminal_size()
        print("\n" * round(h / 2 - len(list) / 2 - 2))
        print(ansi_aware_center(question + "\n", w))
        for i, x in enumerate(list):
            if i == selection:
                print(
                    ansi_aware_center(Back.WHITE + Fore.BLACK + x + Style.RESET_ALL, w)
                )
            else:
                print(ansi_aware_center(x, w))

        key = get_key()

        if key == "\x1b[A":
            selection = selection - 1
        elif key == "\x1b[B":
            selection = selection + 1
        elif key == "\r":
            os.system("clear")
            break
        else:
            print(key)

        if selection > len(list) - 1:
            selection = 0
        if selection < 0:
            selection = len(list) - 1

    log(f'List selection: "{question}": "{selection}"')
    return selection
