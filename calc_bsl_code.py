# This function takes a boot sole length (in mm) and computes the catagory on
# the din chart

def calc_bsl_code(bsl):
    bsl_range = [0,231,251,271,291,311,331,355]
    for index in range(len(bsl_range)):
        if bsl >= bsl_range[index]:
            bsl_code = index
    return bsl_code
