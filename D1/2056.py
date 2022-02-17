# 연월일 달력 2022-01-25

date = input()

year = ''
month = ''
day = ''
for i in range(len(date)):
    if i < 4:
        year += date[i]
    elif i < 6:
        month += date[i]
    else:
        day += date[i]
        
if month in (['01', '03', '05', '07', '08', '10', '12']):
    if int(day) >= 1 and int(day) <= 31:
        print(f'{year}/{month}/{day}')
    else: print(-1)
elif month == '02':
    if int(day) >= 1 and int(day) <= 28:
        print(f'{year}/{month}/{day}')
    else: print(-1)
elif month in (['04', '06', '09', '11']):
    if int(day) >= 1 and int(day) <= 30:
        print(f'{year}/{month}/{day}')
    else:
        print(-1)
else:
    print(-1)