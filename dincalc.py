import string
import argparse #for initial arguments
from calc_skier_code import calc_skier_code
from calc_bsl_code import calc_bsl_code
from calc_din_setting import calc_din_setting

# Print Title
print ("Din Calculator Version 0.1")
print ("Richard Williams 2016")
print ("")

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
        weight = input('Weight: ')

        #get height (imperial or default metric)
        if args.imperial:
            print("Input Height")
            feet = input('Feet: ')
            inches = input('Inches: ')
            height = feet*30.48+inches*2.54
        else:
            height = input('Height: ')

        age = input('Age: ')
        skier_type = input('Skier Type: ') # How to make this just the five options?
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
letter = list(string.uppercase)[skier_code]

#compute bsl code
bsl_code = calc_bsl_code(boot_length)

#compute din setting
din_setting = calc_din_setting(skier_code,bsl_code)

print("")
print("Din Setting: {}".format(din_setting))
