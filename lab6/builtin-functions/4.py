import time
import math
def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    print(result)
number = 25100
milliseconds = 2123
calculate_square_root(number, milliseconds)