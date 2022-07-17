import datetime

today=datetime.date.today()
today
first_date=(input("Enter date with format(y-m-d): "))
second_date=input("Enter date: ")
first_date1=datetime.datetime.strptime(first_date, "%Y-%m-%d")
second_date2=datetime.datetime.strptime(second_date, "%Y-%m-%d")
the_amount_of_time =second_date2-first_date1
x=the_amount_of_time.days
print(f'the year between tow date is {x//365}')
print(f'the days between tow date is {x}')

