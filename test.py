from datetime import datetime

day = datetime.today()

us_format = day.strftime('%m-%d-%Y')

print(us_format)

str_1 = '''how
are
you'''

list = str_1.split()
print(list)