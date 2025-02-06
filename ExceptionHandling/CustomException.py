class PinError(Exception): # we have to derived from base class
    pass
correctPin = 1212
pin = int(input("Enter the 4 digit pin"))
try:
    if(pin == correctPin):
        print("Account Unblocked")
    else:
        raise PinError('Entered pin is', pin)
except PinError as e:
    print("Incorrect pin: ", e)



