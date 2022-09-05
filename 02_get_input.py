
def not_blank(q):
    while True:
        answer = input(q).strip()

        if answer == "":
            print("Input cannot be blank.")
        else:
            return answer


def seat_counter():
    available_seats = 150
    while available_seats > 0:
        print('There are {} seats remaining'.format(available_seats))
        name = not_blank("What is your name?: ")
        available_seats -= 1
        print("Hello {}".format(name))


seat_counter()
