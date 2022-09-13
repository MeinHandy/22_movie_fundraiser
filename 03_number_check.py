def age_check():
    while True:  # loops until break
        try:
            age = int(input("How old are you? "))
        except ValueError:  # confirms age is an integer
            print("Please input a whole number")
            continue  # restarts the loop
        if age < 12:  # if/elif/else for age logic
            print("You are too young to view the movie")
        elif age > 113:
            print("This age is fake, try again")
        else:
            print("Welcome")
            break  # exits the while loop as input was accepted


age_check()  # runs the age check
