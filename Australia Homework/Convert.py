# Function to convert decimal number
# to binary using recursion
import decimal


decima = int(input("Enter your decimal or binary no."))
convert = int(
    input("Press 1 for binary conversion \nPress 2 for reverse conversion"))
if convert == 1:
    print("Binary no. is", bin(decima))
elif convert == 2:
    dec = decimal.Decimal(bin)
    print("Decimal no. is", dec)

'''def DecimalToBinary(num):

    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')


if __name__ == '__main__':

    # decimal value
    dec_val = 24

    # Calling function
    DecimalToBinary(dec_val)
'''
