# horarios = [24]
# minutos = [60]
# segundos = [60]
n = 0
for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
