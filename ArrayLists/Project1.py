import array

amount = int(input("How many days of temperature? "))
days = []
for i in range(amount):
    temp = int(input(f'Day {i + 1}\'s high temp: '))
    days.append(temp)
average = sum(days) / len(days)
print(f'Average = {average}')
above_average = [temp for temp in days if temp > average]
print(f'{len(above_average)} day(s) above average')