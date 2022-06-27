# import fah_converter as fah
from fah_converter import convert_c_to_f

if __name__ == "__main__":
    print("Enter a celsius vale: ")
    celsius = float(input())
    # celsius = 100
    fahrenheit = fah_converter.convert_c_to_f(celsius)
    print(f"That's {fahrenheit} degrees Fahrenheit")