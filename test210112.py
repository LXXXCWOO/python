# 1.
재고량 = 10

if 재고량 > 0:
    print('지금주문가능합니다')

# 2.
중고차재고 = ['K5', 'BMW', 'ModelS']

if 'K6' in 중고차재고:
    print('지금주문가능합니다')
else:
    print('주문불가능합니다')

# 3.
for i in range(0, 10):
    print('K5 있습니다.')

중고차들 = ['K5', '그랜져', '소렌토']

for i in 중고차들:
    print(i)


# For loop on a list
numbers = [2, 4, 6, 8]
product = 1
for number in numbers:
    product = product * number

print('The product is:', product)
