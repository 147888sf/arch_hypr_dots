import datetime
import signal
import time
import subprocess

temperature_night = 5000

enabled = False

def check_time():
    current_time = datetime.datetime.now().time() # Current time
    start_time = datetime.time(1, 30)              # 1:30
    end_time = datetime.time(7, 0)                # 7:00

    if start_time <= current_time < end_time:
        return True
    else:
        return False

while True:
    should_be_enabled = check_time()
    print(should_be_enabled, enabled)

    if should_be_enabled and not enabled:
        process = subprocess.Popen(
            f'hyprsunset -t {temperature_night}',
            shell=True,
            start_new_session=True
        )
        enabled = should_be_enabled
    if not should_be_enabled and enabled:
        try:
            process.send_signal(signal.SIGINT)
        except:
            pass
        enabled = should_be_enabled

    time.sleep(5)
temperature_night
