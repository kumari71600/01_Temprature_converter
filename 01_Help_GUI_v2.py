from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

         # Fomatting variables...
         background_color = "light blue"

         # Converter Main Screen GUI...
         self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                       pady=10)
         self.converter_frame.grid()

         # Temp Conversion Heading (rov 0)
         self.temp_converter_label = Label(self.converter_frame, text="Temperature Conversion",
                                                font=("Arial", "16", "bold"),
                                                bg=background_color,
                                                padx=10, pady=10)
         self.temp_converter_label.grid(row=0)

         # Help Button (rov 1)
         self.help_button = Button(self.converter_frame, text="Help",
                                    font=("Arial", "14"),
                                    padx="10", pady=10, command=self.help)
         self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):

        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="help / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)


        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help buttons back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main rountine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()