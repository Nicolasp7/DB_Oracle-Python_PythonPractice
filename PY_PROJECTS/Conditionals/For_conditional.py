# for f in range(10):
#     print('Value of f: ', f)
# # Example bucle while
# f = 0
# while f < 10:
#     print('Value of', f)
#     f += 1
# for f in range(10, 30, 3):
#     print('Value of f: ', f)
# print('Cycle end')
#
# # Example
# suma = 0
# for f in range(10):
#     value = int(input('Write value'))
#     suma = suma + value
# print('The addition is: ', suma)
# average = suma / 10
# print('The average is: ', average)

# Example 2
# for f in 'Python':
#     print(f, end='')

# Characters control
# arroba = '@'
# cant = 0
# mail = input('Write your mail... ')
# for f in mail:
#     if f == '@':
#         cant += 1
# if cant >= 1:
#     print('correct')
# else:
#     print('Incorrect, it has not arroba')

# Multiplication table
value = int(input('Write the value... '))
print('You have chosen see the table of: ', value)
for f in range(11):
    print(value, 'X', f,' = ', f*value)
