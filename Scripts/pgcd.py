a = int(input("Number 1 : "))       # you enter the a value
b = int(input("Number 2 : "))       # you enter the b value
while a != 0 and b != 0:            # while a is different of 0 AND b is different of 0
    left = a % b                    # the left of the division of a/b is stored in left
    a = b                           # we set the a value to the b value
    b = left                        # we set the b value to the left value
                                    # we start again until a=0 AND b=0
print("The GCD is : ", a)           # we print the last value a takes