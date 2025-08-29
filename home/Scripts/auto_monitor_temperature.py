import datetime
import signal
import subprocess
import time

enabled = False

time_shedule = [
    (datetime.time(22, 30), 5000),
    (datetime.time(23, 0), 4000),
    (datetime.time(23, 30), 3250),
    (datetime.time(7, 0), 6000),
]


def get_current_temperature():
    current_time = datetime.datetime.now().time()

    sorted_schedule = sorted(time_shedule, key=lambda x: x[0])

    for start_time, temperature in reversed(sorted_schedule):
        if current_time >= start_time:
            return temperature

    return sorted_schedule[-1][1]


def change_temperature(new_temperature, current_temperature):
    global proccess
    if new_temperature != current_temperature:
        current_temperature = new_temperature
        try:
            proccess.send_signal(signal.SIGINT)
            time.sleep(1)
        except NameError:
            pass

        proccess = subprocess.Popen(
            f"hyprsunset -t {current_temperature}", shell=True, start_new_session=True
        )


subprocess.run("killall hyprsunset", shell=True)
time.sleep(1)

current_temperature = 0

while True:
    new_temperature = get_current_temperature()

    change_temperature(new_temperature, current_temperature)
    current_temperature = new_temperature

    time.sleep(10)
