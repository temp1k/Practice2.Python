year = int(input("Введите год: "))
days = 0
result = 0
visokosniy = 0

if year % 4 == 0:
    visokosniy = 29
                
else:
    visokosniy = 28

for i in range(1, 13):
    match i:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            days = 31
        case 4 | 6 | 9 | 11:
            days = 30
        case 2:
            days = visokosniy
    
    for x in range(1, days + 1):
        number = 0
        for y in str(x):
            number += int(y)
        result += number

print(f"Полученный результат: {result}")