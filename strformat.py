#String Formatting

price = 49
name = 'Ayush'
quantity = 100

txt = 'The price is {} rs/-'
txt2 = 'Decimal price is {:.2f}'

print(txt.format(price))
print(txt2.format(price))

info = 'Customer {} has buyed {} cars for {:.4f} $/-'
info2 = 'Customer {0} has buyed {1} cars for {2:.4f} $/-. Thanks {0}'

print(info.format(name, quantity, price))
print(info2.format(name, quantity, price))

myorder = 'Thanks {name} for buying {car} at rs {price}'
print(myorder.format(name = 'Ayush', car = 'lambo', price = '15798545'))