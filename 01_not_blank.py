
def not_blank(q):
    while True:
        answer = input(q).strip()

        if answer == "":
            print("Input cannot be blank.")
        else:
            return answer


name = not_blank("What is your name?: ")
print("Hello {}".format(name))
