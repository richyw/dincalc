def calc_skier_code(weight,height,age,skier_type):
    """ This function takes the weight, height, age and skier type and returns
    the numerical value that corresponds to the corrected skier code on the din
    chart"""
    height = int(height)
    weight = int(weight)
    age = int(age)
    if skier_type == "3+":
        skier_type = 4
    elif skier_type == "-1":
        skier_type = 0
    else:
        skier_type = int(skier_type)

    # Compute Uncorrected Skier Code
    # Assigns a number from 0-14 corresponding to skier code from a-o
    weight_range = [0,30,39,48,57,67,79,92,108,126,148,175,210]
    height_range = [0,149,158,167,179,195]

    # loop through weight range array weight code
    for (ind,val) in enumerate(weight_range):
        if weight >= val:
            weight_code = ind

    # loop through height range and assign height code
    constant = len(weight_range) - len(height_range) # to account for array length difference
    for (ind,val) in enumerate(height_range):
        if height >= val:
            height_code = ind + constant

    #assign skier code to be height code or the weight code - whichever is lower
    if height_code < weight_code:
        skier_code = height_code
    else:
        skier_code = weight_code

    #make corrections for age
    if age <= 9 or age >= 50:
        skier_code -= 1

    #make corrections for skier type
    if skier_type >= 3 and weight <= 48:
        skier_code += skier_type - 2
    else:
        skier_code += skier_type - 1

    #skier code cannot be less than zero
    if skier_code < 0:
        skier_code = 0

    return skier_code

def calc_bsl_code(bsl):
    """takes a boot sole length (in mm) and computes the catagory on the din
    chart"""
    bsl = int(bsl)
    bsl_range = [0,231,251,271,291,311,331,355]
    for (ind, val) in enumerate(bsl_range):
        if bsl >= val:
            bsl_code = ind
    return bsl_code

def calc_din_setting(skier_code,bsl_code):
    """Takes the skier_code and the bsl_code and computes the final
    visual indicator setting (calc_din_setting)"""
    din_chart = [[0.75,0.75,0.75,0.75,0.75,0.75,0.75,0.75],
                 [1,1,0.75,0.75,0.75,0.75,0.75,0.75],
                 [1.5,1.25,1.25,1,1,1,1,1],
                 [2,1.75,1.5,1.5,1.25,1.25,1.25,1.25],
                 [2.5,2.25,2,1.75,1.5,1.5,1.5,1.5],
                 [3,2.75,2.5,2.25,2,1.75,1.75,1.75],
                 [3.5,3.5,3,3,2.75,2.5,2.25,2,2],
                 [3.5,3.5,3.5,3,3,2.75,2.5,2.5],
                 [4.5,4.5,4.5,4,3.5,3.5,3,3],
                 [5.5,5.5,5.5,5,4.5,4,3.5,3],
                 [6.5,6.5,6.5,6,5.5,5,4.5,4],
                 [7.5,7.5,7.5,7,6.5,6,5.5,5],
                 [8.5,8.5,8.5,8.5,8,7,6.5,6],
                 [10,10,10,10,9.5,8.5,8,7.5],
                 [11.5,11.5,11.5,11.5,11,10,9.5,9],
                 [12,12,12,12,12,12,11,10.5]]

    din_setting = din_chart[skier_code][bsl_code]
    return din_setting
