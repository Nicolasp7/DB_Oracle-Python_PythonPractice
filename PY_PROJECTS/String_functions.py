word = 'hi everybody'
# Count
print(word.count('e'))
print(word.index('y'))  # Position of letter
print(word.startswith('v'))  # Does it begin with that letter?
print(word.endswith('y'))  # Does it finish ?
print(word[:8])  # Bring the first characters
print(word[8:])  # Bring the last characters
print(word.capitalize())  # First letter of my text in May

word1 = 'HI EVERYBODY'
print(word1.lower())  # For min
print(word.upper())  # For mayus
print(word.isnumeric())  # To search numbers

word2 = 'hi'
print(word2.center(50))  # Out of text in console
print(word2.ljust(20))  # Out of text in console at left
print(word2.rjust(30))  # Out of text in console at right
print(len(word2))  # Count characters in the word