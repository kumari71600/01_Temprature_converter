from tkinter import *
import random



class Start:
    def __init__(self, partner):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg="#D4E1F5")
        self.start_frame.grid()

        # Set Initial balance to zero
        self.starting_funds  = IntVar()
        self.starting_funds.set(0)


        # background
        background = "#D4E1F5"

        # Mystery box Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 16 bold", bg=background)
        self.mystery_box_label.grid(row=0)

        # Initial instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, text=" Please enter a dollar amount",
                                          font="Arial 8 italic", fg="red", bg=background)
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
        self.start_help_button = Button(self.start_help_frame, text="Help",
                                        font="Arial 10 bold", bg="#E6E6E6",
                                        command=lambda: self.to_help)
        self.start_help_button.grid(row=0, column=0)

        self.start_statistics_button = Button(self.start_help_frame, text="Statistics / Export",
                                              font="Arial 10 bold", bg="#E6E6E6",
                                              command=lambda: self.to_stats)
        self.start_statistics_button.grid(row=0, column=1, padx=5)

        self.start_statistics_button.config(state=DISABLED)

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
        def __init__(self, partner, stakes, starting_balance):
            print(stakes)
            print(starting_balance)

            # initialise variables
            self.balance = IntVar()
            # Set starting balance to amount entered by user at start of the game
            self.balance.set(starting_balance)

            # Get value of stakes (use it as a multiplier when calculating winnings
            self.multiplier = IntVar()
            self.multiplier.set(stakes)

            # List for holding statistic
            self.round_stats_list = []
            self.game_stats_list=[starting_balance, starting_balance]

            # GUI Setup
            self.game_box = Toplevel()

            # If users press cross at top, game quits
            self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

            self.game_frame = Frame(self.game_box)
            self.game_frame.grid()

            # Heading Row
            self.heading_label = Label(self.game_frame, text="Play...",
                                       font="Arial 24 bold", padx=10,
                                       pady=10)
            self.heading_label.grid(row=0)

            # Instructions Label
            self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                            text="Press <enter> or click the 'Open "
                                                 "Boxes' button to reveal the "
                                                 "contents of the mystery boxes.",
                                            font="Arial 10", padx=10, pady=10)
            self.instructions_label.grid(row=1)

            # Boxes go here (row 2)
            self.box_frame = Frame(self.game_frame)
            self.box_frame.grid(row=2, pady=10)

            photo = PhotoImage(file="images\question.gif")

            self.prize1_label = Label(self.box_frame, image=photo,
                                      padx=10, pady=10)
            self.prize1_label.photo = photo
            self.prize1_label.grid(row=0, column=0)

            self.prize2_label = Label(self.box_frame, image=photo,
                                      padx=10, pady=10)
            self.prize2_label.photo = photo
            self.prize2_label.grid(row=0, column=1)

            self.prize3_label = Label(self.box_frame, image=photo,
                                      padx=10, pady=10)
            self.prize3_label.photo = photo
            self.prize3_label.grid(row=0, column=2)

            # Play button goes here (row 3)
            self.play_button = Button(self.game_frame, text="Open Boxes",
                                      bg="#FFFF33", font="Arial 15 bold", width=20,
                                      padx=10, pady=10, command=self.reveal_boxes)
            self.play_button.grid(row=3)

            # bind button to <enter> (users can push enter to reveal boxes)

            self.play_button.focus()
            self.play_button.bind('<Return>', lambda e: self.reveal_boxes())

            # Balance label (row 4)

            start_text = "Game Cost: ${} \nHow Much " \
                         "will you win?".format(stakes * 5)

            self.balance_label = Label(self.game_frame, font="Arial 12 bold", fg="blue",
                                       text=start_text, wrap=300,
                                       justify=LEFT)
            self.balance_label.grid(row=4, pady=10)

            # Help and Game Stats button (row 5)
            self.help_export_frame = Frame(self.game_frame)
            self.help_export_frame.grid(row=5, pady=10)

            self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                      font="Arial 15 bold",
                                      bg="#808080", fg="white")
            self.help_button.grid(row=0, column=0, padx=2)

            self.stats_button = Button(self.help_export_frame, text="Game Stats...",
                                       font="Arial 15 bold",
                                       bg="#003366", fg="white")
            self.stats_button.grid(row=0, column=1, padx=2)

            # Quit Button
            self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                      bg="#660000", font="Arial 15 bold", width=20,
                                      command=self.to_quit, padx=10, pady=10)
            self.quit_button.grid(row=6, pady=10)

        def reveal_boxes(self):
            # retrieve the balance from the initial function...
            current_balance = self.balance.get()
            stakes_multiplier = self.multiplier.get()

            round_winnings = 0
            prizes = []
            stats_prizes = []

            # Allows photo to change depending on stakes.
            # lead not in the list as that is always 0
            copper = ["images\copper_low.gif", "images\copper_med.gif", "images\copper_high.gif"]
            silver = ["images\silver_low.gif", "images\silver_med.gif", "images\silver_high.gif"]
            gold = ["images\gold_low.gif", "images\gold_med.gif", "images\gold_high.gif"]
            for item in range(0, 3):
                prize_num = random.randint(1, 100)

                if 0 < prize_num <= 5:
                    prize = PhotoImage(file=gold[stakes_multiplier - 1])
                    prize_list = "gold (${})".format(5 * stakes_multiplier)
                    round_winnings += 5 * stakes_multiplier
                elif 5 < prize_num <= 25:
                    prize = PhotoImage(file=silver[stakes_multiplier - 1])
                    prize_list = "silver (${})".format(2 * stakes_multiplier)
                    round_winnings += 2 * stakes_multiplier
                elif 25 < prize_num <= 65:
                    prize = PhotoImage(file=copper[stakes_multiplier - 1])
                    prize_list = "copper (${})".format(1 * stakes_multiplier)
                    round_winnings += stakes_multiplier
                else:
                    prize = PhotoImage(file="images\lead.gif")
                    prize_list = "lead ($0)"

                prizes.append(prize)
                stats_prizes.append(prize_list)

            photo1 = prizes[0]
            photo2 = prizes[1]
            photo3 = prizes[2]

            # Display prizes a edit background...
            self.prize1_label.config(image=photo1)
            self.prize1_label.photo = photo1
            self.prize2_label.config(image=photo2)
            self.prize2_label.photo = photo2
            self.prize3_label.config(image=photo3)
            self.prize3_label.photo = photo3

            # Deduct cost of game
            current_balance -= 5 * stakes_multiplier

            # Add winnings
            current_balance += round_winnings

            # Set balance to new balance
            self.balance.set(current_balance)
            # update game_stats_lists with current balance
            # posistion 1 with current balance
            self.game_stats_list[1] = current_balance

            balance_statement = "Game Cost: ${}\nPayback: ${} \n" \
                                "Current Balance: ${}".format(5 * stakes_multiplier,
                                                              round_winnings,
                                                              current_balance)

            # add round results to statistics list
            round_summary = "[] | [] | {} - Cost: $[] | " \
                            "Payback: ${} | Current Balance: " \
                            "${}".format(stats_prizes[0], stats_prizes[1],
                                         stats_prizes[2],
                                         5 * stakes_multiplier, round_winnings,
                                         current_balance)
            self.round_stats_list.append(round_summary)
            print(self.round_stats_list)

            # Edit label so user can see their balance
            self.balance_label.configure(text=balance_statement)

            if current_balance < 5 * stakes_multiplier:
                self.play_button.config(state=DISABLED)
                self.game_box.focus()
                self.play_button.config(text="Game Over")

                balance_statement = "Current Balance: ${}\n" \
                                    "Your balance is too low. You can only quit " \
                                    "or view your stats. Sorry about that.".format(current_balance)
                self.balance_label.config(fg="#660000", font="Arial 10 bold",
                                          text=balance_statement)

        def to_quit(self):
            root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()