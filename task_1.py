time = "1h 45m,360s,25m,30m 120s,2h 60s"
time_list = [t.split() for t in time.split(",")]
minutes_total = 0.0

for t_list in time_list:
    for item in t_list:
        minuts = 0.0
        unit = int(item[:-1])
        if item[-1] == "s":
            minuts += unit / 60
        elif item[-1] == "h":
            minuts += unit * 60
        elif item[-1] == "m":
            minuts += unit
        else:
            print(
                "Ошибка неверный формат записи. Исправьте вводимые значения и запустите программу заного."
            )
            break

        minutes_total += minuts

print(minutes_total)
