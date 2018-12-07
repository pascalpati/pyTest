#
#
# File operations basic exercise code
#
# Have fun!

# No need to import any classes as file operations are built into python

def openFile_write():
    # Open a file for writing or create it if it does not exist (that is what "+" is for)
    f = open("sampleText.txt", "a+")

    # Write some data to the file
    for i in range(100):
        f.write("This is line number %d\r\n" % (i + 1))

    f.close()

def openFile_read():
    # Open a file to read
    with open("sampleText.txt", "r") as f:
        fileContents = f.readlines(45)
        print(fileContents)



def main():
    # This is the main() function
    print("main() - entry")

    # Open a file for file operations
    openFile_write()

    # Open the file to read
    openFile_read()


if __name__ == '__main__':
    main()