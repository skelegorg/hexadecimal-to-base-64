# this is the file that converts the hexadecimals to base 64
import codecs


# first, convert the hexadecimal to a number
with open('hexfile.txt', 'rb') as hexfile:
    hexstring = hexfile.read()

finalstring = codecs.encode(codecs.decode(hexstring, "hex"), 'base64').decode()
print(finalstring)
