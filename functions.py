def level_battery():
    import psutil
    battery = psutil.sensors_battery()
    return str(battery[0])

def critical_battery(limit):
    level = level_battery()
    import psutil
    battery_status = psutil.sensors_battery()
    if battery_status[2]:
        return '#138f00'
    elif int(level) <= int(limit):
        return '#ff0000'
    else: return '#000000'

def time_this_moment():
    from datetime import datetime
    now = datetime.now()
    time_now = now.strftime("%H:%M")
    return time_now

def critical_time(limit):
    seconds = time_this_moment()[6:8]
    if int(seconds) >= int(limit):
        return '#ff0000'
    else: return '#000000'

def main():
    return
    label.pack()
    label.grid(column=0, row=0)
    time_ = str(time_this_moment())
    battery_ = str(level_battery()) + '%'
    full_string = f'{time_} \n {battery_}'
    label.config(text=full_string)
    label.config(fg=critical_battery(15))
    window.update()


