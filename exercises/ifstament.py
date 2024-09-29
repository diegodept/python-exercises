
#if Do some code only IF some condition is True
#   Else do something else

age = int(input("enter your age: "))


if age >= 100:
    print("you are too old to sign up")
elif age >= 18:
    print("you are now signed up")         
elif age < 0:
    print("you havent been born yet")
else:
    print("you must be 18+ to sign up")    
