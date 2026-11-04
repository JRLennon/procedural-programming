reading = "160648" # the faulty reading from the odometer
base9_digits = "".join(str(int(d) - (int(d) > 5)) for d in reading) # base 9 representation of the reading, because it skips 5, so it goes 0,1,2,3,4,6,7,8,9.

actual_distance = int(base9_digits, 9)
print(actual_distance)  # returns 92302
