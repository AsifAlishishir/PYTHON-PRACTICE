num=int(input("Enter inch: "))

def toCm(inc):
    if inc<=0:
        print("Enter a valid Inch Measurement!")
    else:
        print(f"The given {inc} inch's Centimeter value is: {inc * 2.54}")

toCm(num)