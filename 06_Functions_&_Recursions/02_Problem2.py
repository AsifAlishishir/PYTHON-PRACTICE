# F = (°C × 9/5) + 32


def celToFah(c):
    f=c * (9 / 5) + 32
    return f

temp=int(input("Enter Temperature in Celsius: "))
print(f"The given temperature in fahrenheit is: {celToFah(temp)}")
