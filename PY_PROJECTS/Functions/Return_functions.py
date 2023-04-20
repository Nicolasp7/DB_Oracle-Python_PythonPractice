# Function to calculate triangle area
# def triangle (base, height):
#     area = base*height/2
#     return area
# base=int(input('Write base...'))
# height=int(input('Write height...'))
# print("The Triangle area is: ", triangle(base,height))

# Function calculate higher value
def higher_value(value1, value2):
    if value1 > value2:
        higher = value1
    else:
        higher = value2
    return higher


# Mainly block
v1 = int(input('Write first value...'))
v2 = int(input('Write second value...'))
print('The higher value is: ', higher_value(v1, v2))
print('The higher value is: ', higher_value(v1, v2))
