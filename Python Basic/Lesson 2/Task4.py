from random import triangular

#Первые четыре значения заданы искуственно, для подтверждения работоспособности кода
#под разные форматы, если генератор не выдаст такие форматы как [rr.00] [.0k] [.k0] [r.kk]
prices = [83, 14.02, 63.2, 7.29]

#В задачу входит доказательство, что список и объекты используются теже, поэтому будет много id()
print(id(prices), '- index\nList -', prices)

i = 1
while i <= 16:
    price_rand = round(triangular(00.01, 99.99), 2)
    prices.append(price_rand)
    i += 1

print(id(prices), '- index\nList -', prices)

for price in prices:
    price = str(price).split('.')
    if len(price) < 2:
        price.append('00')
    if len(price[-1]) < 2:
        price[-1] = price[-1] + '0'
    print(price[0], 'руб', price[-1], 'коп', end=', ')
print('\n')

prices.sort()
for price in prices:
    price = str(price).split('.')
    if len(price) < 2:
        price.append('00')
    if len(price[-1]) < 2:
        price[-1] = price[-1] + '0'
    print(price[0], 'руб', price[-1], 'коп', end=', ')
print()
print(id(prices), '- index\nList -', prices)

new_prices = prices[:]
new_prices.sort(reverse=True)
print(id(new_prices), '- index уже имеет другое значение\nList -', new_prices)
print('Цены пять самых дорогих товара ', new_prices[0:5])