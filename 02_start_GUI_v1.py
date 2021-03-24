from tkinter import *
import random


class Start:
    def __init__(self, partner):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg="#D4E1F5")
        self.start_frame.grid()

        # Set Initial balance to zero
        self.starting_funds = IntVar()
        self.starting_funds.set(0)


        # background
        background = "#D4E1F5"

        # Mystery box Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 16 bold", bg=background)
        self.mystery_box_label.grid(row=0)

        # Initial instructions (row 1)
        self.mystery_instructions = Label(self.start_frame,
                                          font="Arial 8 italic",
                                          text=" Please enter a dollar amount  "
                                               "(between $5 and $50) in the box "
                                               "below, then choose the stakes, "
                                               "the more you can win! ",
                                          wrap=275, justify=LEFT, padx=10, pady=10)


        self.mystery_instructions.grid(row=1)

        # Entry box and Error Label (row 2)
        self.start_error_frame = Frame(self.start_frame, width=200, bg=background)
        self.start_error_frame.grid(row=2)

        self.start_amount_entry = Entry(self.start_error_frame,
                                        font="Arial 13 bold")
        self.start_amount_entry.grid(row=0, column=0)

        self.start_add_funds = Button(self.start_error_frame, text="Add funds!",
                                      font="Arial 13 bold", bg=background, command=self.check_funds)
        self.start_add_funds.grid(row=0, column=1)

        self.amount_error_label = Label(self.start_error_frame, bg=background, fg="maroon", text="",
                                        font=" Arial 10 bold", wrap=275, justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # Buttons frame ( row 3)

        self.stakes_frame = Frame(self.start_frame, bg=background)
        self.stakes_frame.grid(row=3)

        # Button Font
        button_font = "Oswald 12 bold"

        # Low Stakes Button
        self.low_stakes_button = Button(self.stakes_frame, text="Low ($5)",
                                        font=button_font, bg="#FF9933",
                                        command=lambda: self.to_game(1))
        self.low_stakes_button.grid(row=0, column=0, pady=10)

        # Medium Stakes Button
        self.med_stakes_button = Button(self.stakes_frame, text="Medium (10$)",
                                        font=button_font, bg="#FFFF33",
                                        command=lambda: self.to_game(2))
        self.med_stakes_button.grid(row=0, column=1, pady=10, padx=5)

        # High Stakes Button
        self.high_stakes_button = Button(self.stakes_frame, text="High (15$)",
                                         font=button_font, bg="#09FF33",
                                         command=lambda: self.to_game(3))
        self.high_stakes_button.grid(row=0, column=2, pady=10, padx=5)

        # Disable all stakes buttons at start.
        self.low_stakes_button.config(state=DISABLED)
        self.med_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        # Button frame for help and statistics (row 5)
        self.start_help_frame = Frame(self.start_frame, bg="#D4E1F5")
        self.start_help_frame.grid(row=5)

        # Help and statistics buttons
        self.start_help_button = Button(self.start_help_frame, text="How to play?",
                                        font="Arial 10 bold", bg="#E6E6E6",
                                        command=lambda: self.to_help)
        self.start_help_button.grid(row=0, column=0)


    def check_funds(self):
        starting_balance = self.start_amount_entry.get()

        error_back = "#ffafaf"
        has_errors = "no"

        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        self.low_stakes_button.config(state=DISABLED)
        self.med_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the minimum amount is $5"

            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too high! the maximum amount is $50"



            elif starting_balance >= 15:
                self.low_stakes_button.config(state=NORMAL)
                self.med_stakes_button.config(state=NORMAL)
                self.high_stakes_button.config(state=NORMAL)


            elif starting_balance >= 10:
                self.low_stakes_button.config(state=NORMAL)
                self.med_stakes_button.config(state=NORMAL)
            else:
                self.low_stakes_button.config(state=NORMAL)


        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (no text / decimal)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)
        else:
            self.starting_funds.set(starting_balance)

    def to_game(self, stakes):
        starting_balance = self.starting_funds.get()

        Game(self, stakes, starting_balance)

        root.withdraw()


class Game:
    def __init__(self, partner, stakes, starting_funds):
        print(stakes)
        print(starting_funds)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()

