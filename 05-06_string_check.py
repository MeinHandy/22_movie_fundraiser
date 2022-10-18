# 01_not_blank
available_seats = 150
valid_snacks = ["popcorn", "m&ms", "pita chips", "orange juice", "water"]
snack_list = []

def not_blank(question):
    while True:  # loops indefinitely until an acceptable input is received
        answer = input(question).strip()  # saves the input to "answer" variable, strips whitespace at the start or end of input

        if answer == "":  # checks if the answer is blank
            print("Input cannot be blank.")  # prints an error based on what has one wrong
        else:
            return answer  # returns the answer


# 02_get_input
def seat_counter(seatage):
    seatage -= 1  # reduces available seats by one each time
    return seatage


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
            return age


def ticket_price(user_age):
    ticket_total = 0
    if user_age <= 15:
        ticket_total += 7.5
    elif age <= 64:
        ticket_total += 10.5
    elif age >= 65:
        ticket_total += 6.5
    else:
        print("error occurred, unaccounted for age recieved")
    print("cost total is ${:.2f}".format(ticket_total))
    return ticket_total


def string_checker(question, for_check):
    valid = False
    while not valid:
        answer = input(question).strip().lower()
        if answer in for_check:
            return answer
        else:
            print("Invalid Input, please answer {}".format(for_check))

def snack_requester():
    valid = False
    while not valid:
        try:
            snack_count = int(input("How many snacks do you want? "))
            valid = True
        except ValueError:  # confirms snack number request is an integer
            print("Please input a whole number")
    for i in range(0, snack_count):
        snack_list.append(string_checker("What snacks do you want? ", valid_snacks))
    print("Snacks ordered are the following: {}".format(snack_list))

# runs the following code until there are no more remaining seats
while available_seats > 0:  # while loops the code when the available seats is more than 0
    print('There are {} seats remaining'.format(available_seats))  # prints the total number of remaining seats
    name = not_blank("What is your name?: ")  # uses the not_blank function so name is not blank
    available_seats = seat_counter(available_seats)  # runs seat_counter
    age = age_check()
    total_cost = ticket_price(age)
    wants_snacks = string_checker("Do you want snacks for the movie? (Yes/No) ", ["yes", "no"])
    if wants_snacks == "yes":
        snack_requester()
    else:
        print("No snacks ordered")
