def convert_far_to_cel(far):
    print(far,"degrees F =", round((far-32)*5/9,2), "degrees C")

def convert_cel_to_far(cel):
    print(cel,"degrees C =", round(cel*9/5+32,2), "degrees F")

farr = float(input("Enter a temperature in degrees F: "))
cell = float(input("Enter a temperature in degrees C: "))

convert_far_to_cel(farr)
convert_cel_to_far(cell)