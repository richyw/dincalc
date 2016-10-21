import string

# Receive the data to determine visual indicator setting
weight = input('Weight: ')
height = input('Height: ')
age = input('Age: ')
skier_type = input('Skier Type: ') # How to make this just the five options?
boot_length = input('Boot Sole Length: ')

# Compute Uncorrected Skier Code
# Assigns a number from 0-14 corresponding to skier code from a-o
skier_type = 0; # start with type zero

weight_code = [0,30,39,48,57,67,79,92,108,126,148,175,210]
height_code = [0,149,158,167,179,195]
letter_code = list(string.uppercase)

# loop through weight code array and assign skier type based on weight
for index in range(len(weight_code)):
    if weight >= weight_code[index]:
        skier_type = index

# loop through code and assign skier type based on height
for index in range(len(height_code)):
    constant = len(weight_code) - len(height_code) # to account for array length difference
    if height >= height_code[index] and index + constant < skier_type:
        skier_type = index + constant

#print skier type
print(letter_code[skier_type])
