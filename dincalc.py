import string
from calc_skier_code import calc_skier_code
from calc_bsl_code import calc_bsl_code

# Receive the data to determine visual indicator setting
weight = input('Weight: ')
height = input('Height: ')
age = input('Age: ')
skier_type = input('Skier Type: ') # How to make this just the five options?
boot_length = input('Boot Sole Length: ')

#compute corrected skier code
skier_code = calc_skier_code(weight,height,age,skier_type)
#retreive letter code
letter = list(string.uppercase)[skier_code]

#compute bsl code
bsl_code = calc_bsl_code(boot_length)

print(letter)
print(bsl_code)
