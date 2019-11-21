films={
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
}
while True:
    choice = input("What film would you like to watch..?").strip().title()

    if choice in films:
        age = int(input("How old are you..?"))

        if age > films[choice][0]:

            if films[choice][1]>0:
                print("Enjoy the film...!!!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("No seats available...!!!")
        else:
            print("Sorry... you are too young to watch this film....!!!")
    else:
        print("This film is not available")

