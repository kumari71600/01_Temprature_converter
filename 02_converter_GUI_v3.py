from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Converter:
    def __init__(self):

        # Formatting variables
        background_color = "light blue"

        # In actual program this is blank and is populated with user calculations


         # initialise list to hold calculation history
        self.all_calculations = []

        # Converter Frame
        self.converter_frame = Frame(bg=background_color,
                                     pady=10)
        self.converter_frame.grid()


        # Temparture Converter heading (rov 0)
        self.temp_heading_label = Label(self.converter_frame,
                                          text="temperature Converter",
                                          font="Arial 16 bold",
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (rov 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                          text="Type in the amount to be "
                                                "converter and then push "
                                                "one of the buttons below...",
                                       font="Arial 10 italic", wrap=290,
                                       justify=LEFT, bg=background_color,
                                       padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)


        # Temperature entry box (rov 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (rov 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                   bg="Khaki1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)


        # Answer label (rov 4)
        self.converted_label = Label(self.converter_frame, font="Arial 12 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)


        # History / Help button frame (rov 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                            text="Help", width=5)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf" # pale pink when error happens

        # retrieve amount entered into entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_error = "no"
            has_errors = "yes"

            # Check amount is a valid number
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # Check  and convert to centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees C is {} degrees F".format(to_convert, celsius)

            else:
                # Input is invalid (too cold)!!
                answer = "Too Cold!"
                has_errors = "yes"

            # Display answer
            if has_errors == "no":
                 self.converted_label.configure(text=answer, fg="blue")
                 self.to_convert_entry.configure(bg="white")
            else:
                 self.converted_label.configure(text=answer, fg="red")
                 self.to_convert_entry.configure(bg=error)


            # Add answer to list for history
            if answer != "Too Cold":
                 self.all_calculations.append(answer)
                 print(self.all_calculation)

        except ValueError:
            self.converted_label.configure(text="Enter a number!!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 ==0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded



# main rountine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()