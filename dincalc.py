import string

# Receive the data to determine visual indicator setting
weight = input('Weight: ')
height = input('Height: ')
age = input('Age: ')
skier_type = input('Skier Type: ') # How to make this just the five options?
boot_length = input('Boot Sole Length: ')

# Compute Uncorrected Skier Code
# Assigns a number from 0-14 corresponding to skier code from a-o
#skier_code = 0; # start with type zero

weight_range = [0,30,39,48,57,67,79,92,108,126,148,175,210]
height_range = [0,149,158,167,179,195]
letter_code = list(string.uppercase) # To convert Skier code to letter

# loop through weight code array weight code
for index in range(len(weight_range)):
    if weight >= weight_range[index]:
        weight_code = index

# loop through code and assign height code
constant = len(weight_range) - len(height_range) # to account for array length difference
for index in range(len(height_range)):
    if height >= height_range[index]:
        height_code = index + constant

#assign skier code to be height code or the weight code - whichever is lower
if height_code < weight_code:
    skier_code = height_code
else:
    skier_code = weight_code

#print skier code
print(letter_code[skier_code])

#make corrections for age
if age <= 9 or age > 50:
    skier_code -= 1

#make corrections for skier type
if skier_type == "-1":
    skier_code -=1

elif skier_type == "3+":
    skier_code += 3

else:
    skier_code += skier_type - 1

#print skier type
print(letter_code[skier_code])
