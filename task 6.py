a = int(input("Введите результат с первого дня пробежки в км "))
b = int(input("Введите желаемый показатель в км "))
res_days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    res_days += 1
    result_km = res_days + a
print(f"Вы достигнете нужных показателей на %.d день" % res_days)
