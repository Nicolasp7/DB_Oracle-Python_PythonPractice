list_ints = [1, 2, 3, 4, 5]
list_letters = ['a', 'b', 'c', 'd']
signatures = ['Physics', 'Maths', '1990', True]
prices = [50.26, 10.30, 100.50, 40.10]

# print(list_ints[0])
# print(list_letters[2:5])
# print(signatures[:3])
# print(prices[2:])

# Add elements to a list with append
# list_letters.append('e')
# print(list_letters)
# signatures.append('Biology')
# print(signatures)

# Delete
# del list_letters[2]
# print(list_letters)
# del prices[3]
# print(prices)

# Others
# print([1, 2, 3] + [4, 5, 6])  # Concatenate
# print(['Hi']*4)
# print([3, 2, 6] * 3)
# print(5 in [1, 2, 3])

# Len Function
# print(len(list_ints))  # Count elements list
# print(max(prices))
# print(min(prices))
# print(list_ints.count(5))

# Expend function
# signatures.extend('Maths')
# print(signatures)
# prices.pop(2)  # Delete
# print(prices)
# list_ints.remove(2)
# print(list_ints)

# Reverse
# list_letters.reverse()  # Change order of lists
# print(list_letters)

# Buckle
for f in signatures:
    print(f, end=' / ')