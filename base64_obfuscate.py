#
# Simple base64 obfuscation of entered string
#
#

# import base64 for simple obfuscation
import base64

#input_string = "PiRiL6__uLaS39"

#def input_string():
    # input a string to be obfuscated


def obfuscate():
    # obfuscate the input string
    obfuscated_string = base64.b64encode(bytes(u'PiRiL6__uLaS39', "utf-8"))
    print(obfuscated_string)


# define the main function
def main():
    # ask for the string entry
    #input_string()

    #  print obfuscated string
    obfuscate()

# call the main() function
if __name__ == '__main__':
    main()