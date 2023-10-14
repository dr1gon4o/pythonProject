centurie = int(input())

year = centurie * 100
days = int(year * 365.2422)
hours = days * 24
minute = hours * 60

print(f'{centurie} centuries = {year} years = {days:.0f} days = {hours:.0f} hours = {minute:.0f} minutes')
