from tkinter import *
import random


class Start:
    def __init__(self, parent):

        # Start GUI
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery box Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Entry box (row 1)
        self.start_amount_entry = Entry(self.start_frame, font="Arial 16 bold",
                                        text="Please enter a dollar amount "
                                             "(between $5 and $50) in the box "
                                             "below, then choose the stakes, "
                                             "the more you can win!",
                                        wrap=275, justify=LEFT, padx=10, pady=10)
        self.start_amount_entry.grid(row=1)

        # Play Button (row 2)
        self.low_stakes_button = Button(text="Low ($5)",
                                       command=lambda: self.to_game(1))
        self.low_stakes_button.grid(row=2, pady=10)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()
        Game(self, stakes, starting_balance)


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # Disable low stakes button
        partner.low_stakes_button.config(state=DISABLED)

        # Initialise variables
        self.balance = IntVar()

        # Set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row (row =0)
        self.heading_label = Label(self.game_frame, text="Heading",
                                   font="Arial 24 bold", padx=10)
        self.heading_label.grid(row=0)

        # Balance Label
        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1)

        self.balance_label = Label(self.game_frame, text="Balance...")
        self.balance_label.grid(row=2)

        self.play_button = Button(self.game_frame, text="PLAY!",
                                  font="Arial 12 bold", padx=10, pady=10,
                                  command=self.reveal_boxes)
        self.play_button.grid(row=3)

    def reveal_boxes(self):
        # Retrieve the balance from initial func.
        current_balance = self.balance.get()

        # Adjust the Balance
        current_balance += 2

        # Change the Balance
        self.balance.set(current_balance)

        # Label changes so users can see their balance
        self.balance_label.configure(text="Balance: {}".format(current_balance))


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start()
    root.mainloop()