value1 = 90
value2 = 90
if value1 == value2:
    print(value1, 'Is the same to', value2)
else:
    print(value1, "Is not the same to", value2)
    if value1 > value2:
        print('The value', value1, 'is greater')
    else:
        print('The value', value2, 'is greater')
    if value1 < value2:
        print('The value', value1, 'is smaller')
    else:
        print('The value', value2, "is smaller")
    if value1 >= value2:
        print('The value', value1, 'is greater or the same than', value2)
    else:
        print('The value', value2, "is greater or the same than", value1)
    if value1 <= value2:
        print('The value', value1, 'is smaller or the same than', value2)
    else:
        print('The value', value2, "is smaller or the same than", value1)

if value1 != value2:
    print(value1, 'Is not the same to', value2)
else:
    print(value1, "Is the same to", value2)
