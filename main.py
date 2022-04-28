bilet = int(input("Сколько билетов необходимо на мероприятие?"))
sum_bilet = 0
for client in range(0, bilet):
    age = int(input("Сколько вам лет?"))
    price = 0
    if 25 > age > 18:
        price = 990
    if age > 25:
        price = 1390
    sum_bilet += price

if bilet > 3:
    sum_bilet *= 0.9

print(sum_bilet)
