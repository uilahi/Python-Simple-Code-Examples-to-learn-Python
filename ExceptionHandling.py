class ExpHand:
    def ask_int(self):
        while True:
            try:
                x = int(input("Please enter an integer:\n"))
            except:
                print("Not an integer")
                # continue
            else:
                print("Success...!!! Thank you")
                break

my_exphand = ExpHand()
my_exphand.ask_int()

