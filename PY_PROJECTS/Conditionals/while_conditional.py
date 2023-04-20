# Example 1
counting = 0
while counting < 9:  # While the variable counting has that value
    print('counting is', counting)
    counting += 1  # Then, the initial value, adds 1
print('Counting complete')
# Example 2
value = int(input('Write the final number = '))
f = 1
while f <= value:
    print('value =', f)
    f += 1
print('thanks!')
# Example 3
value1 = int(input('Write number 0 to begin = '))
while value1 != 0:
    print('Written number: ', value1, 'The number 0 has not been written')
    value1 = int(input('Pls write 0 = '))
print('Thanks !')
