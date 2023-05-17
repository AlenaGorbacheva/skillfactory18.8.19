amount = 0
tickets = int(input ("Введитете количество билетов: "))
for age in range (tickets):
    age = int(input("Введите возвраст посетителя:"))
    if age < 18:
        amount += 0
    elif 18 <= age <= 25:
        amount += 990
    elif age > 25:
        amount += 1390
if tickets > 3:
        amount += amount / 100 * 10
print("Сумма к оплате с учетом скидки: ", amount)
print("Сумма к оплате: ", amount)
print("Стоимость ваших билетов: ", amount)