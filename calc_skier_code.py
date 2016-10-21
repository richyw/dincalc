# This function takes the weight, height, age and skier type and returns the numerical
# value that corresponds to the corrected skier code on the din chart

def calc_skier_code(weight, height,age,skier_type):
    # Compute Uncorrected Skier Code
    # Assigns a number from 0-14 corresponding to skier code from a-o
    weight_range = [0,30,39,48,57,67,79,92,108,126,148,175,210]
    height_range = [0,149,158,167,179,195]

    # loop through weight range array weight code
    for index in range(len(weight_range)):
        if weight >= weight_range[index]:
            weight_code = index

    # loop through height range and assign height code
    constant = len(weight_range) - len(height_range) # to account for array length difference
    for index in range(len(height_range)):
        if height >= height_range[index]:
            height_code = index + constant

    #assign skier code to be height code or the weight code - whichever is lower
    if height_code < weight_code:
        skier_code = height_code
    else:
        skier_code = weight_code

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

    return skier_code
