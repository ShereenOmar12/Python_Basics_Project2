from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount_of_money = int(input("Please enter the amount you want to convert: "))

old_currency = input("Please enter the currency that you to be converted: ").upper()

new_currency = input("Please enter the currency that want to convert: ").upper()

print("the  converting", amount_of_money, old_currency, "to", new_currency,".")

Result = c.convert(old_currency, new_currency, amount_of_money)

print("The converted unit is:", Result)
