# for letter in "programming":
#     print(letter)
#     if letter == 'm':
#         break  # Here is buckles out
#
# print('letter found: ', letter, 'Buckle end')

# In while
# counting = 10
# while counting > 0:
#     print('Counting in: ', counting)
#     counting = counting - 1
#     if counting == 5:
#         break  # Here is Buckles out
# print('Counting end')

# Continue function
for letter in 'programming':
    if letter == 'e':
        print('Wrong letter')
        continue  # Continue until the Buckle's end
    print(letter)
print('Buckles end')