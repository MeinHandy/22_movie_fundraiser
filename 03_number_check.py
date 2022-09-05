while True:
    try:
        age = int(input("how old nerd? "))
    except ValueError:
        print("Please input a whole number")
        continue
    break

if age < 12:
    print("You are too young to view the movie")
elif age > 113:
    print("This age is fake, try again")
else:
    print("Welcome")
