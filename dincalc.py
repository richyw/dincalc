import string
import argparse #for initial arguments
from din import calc_skier_code, calc_bsl_code, calc_din_setting, feet_to_cm

def parseArguments():
    #Create Argument Parser
    parser = argparse.ArgumentParser()

    #Optional Arguments
    parser.add_argument("-w","--weight",help="Weight",type=float,default=0)
    parser.add_argument("-ht","--height",help="Height",type=float,default=0)
    parser.add_argument("-a","--age",help="Age",type=float,default=0)
    parser.add_argument("-t","--skier_type",help="Skier Type",type=int,default=0)
    parser.add_argument("-b","--boot_length",help="Boot Sole Length",type=float,default=0)
    # Argument to take height in feet/inches
    parser.add_argument("-imp","--imperial",help="Imperial",action="store_true")

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    # Print Title
    print ("Din Calculator Version 0.2")
    print ("Richard Williams 2016")
    print ("")

    #Parse the Arguments
    args = parseArguments()

     # Raw print arguments
    if args.weight != 0:
        print("You are computing the DIN for the arguments: ")
        for a in args.__dict__:
            print(str(a) + ": " + str(args.__dict__[a]))

    if args.weight == 0:
        # Receive the data to determine visual indicator setting
        print("Input Skier Data: ")
        weight = int(input('Weight: '))

        #get height (imperial or default metric)
        if args.imperial:
            print("Input Height")
            feet = int(input('Feet: '))
            inches = int(input('Inches: '))
            height = feet_to_cm(feet,inches)
        else:
            height = input('Height: ')

        age = input('Age: ')
        skier_type = input('Skier Type: ')
        boot_length = input('Boot Sole Length: ')
    else:
        weight = args.weight
        height = args.height
        age = args.age
        skier_type = args.skier_type
        boot_length = args.boot_length

#compute corrected skier code
skier_code = calc_skier_code(weight,height,age,skier_type)

#retreive letter code
#letter = list(string.uppercase)[skier_code]

#compute bsl code
bsl_code = calc_bsl_code(boot_length)

#compute din setting
din_setting = calc_din_setting(skier_code,bsl_code)

print("")
print("Din Setting: {}".format(din_setting))
