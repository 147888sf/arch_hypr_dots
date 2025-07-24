import os
import subprocess

log_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")


def clear_log():
    with open(log_filename, "w") as log_file:
        log_file.write("")


def log(msg):
    with open(log_filename, "ab") as log_file:
        log_file.write((msg + "\n").encode())


def log_print(msg):
    log(msg)
    print(msg)


def err_log(err):
    log(f"{type(err)}: {err}")


def log_cmd(command, cwd=os.path.expanduser("~")):
    try:
        output = subprocess.run(
            command, shell=True, cwd=cwd, check=True, text=True, capture_output=True
        )
        log(output.stdout)
    except Exception as error:
        err_log(error)
