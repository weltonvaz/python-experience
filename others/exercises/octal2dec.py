n = int(raw_input('Digite um numero decimal: '))
decimal = 0
i = 0
while n > 0:
    resto = n % 10
    n /= 10
    decimal = decimal + resto * 8**i
    i += 1
print 'Decimal:', decimal
