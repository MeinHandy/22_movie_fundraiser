def age_check():
    while True:
        try:
            age = int(input("How old are you? "))
        except ValueError:
            print("Please input a whole number")
            continue
        if age < 12:
            print("You are too young to view the movie")
        elif age > 113:
            print("This age is fake, try again")
        else:
            print("Welcome")
            break


age_check()
