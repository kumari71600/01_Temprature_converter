from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Converter:
    def  __init__(self):

        # Formatting variables
        background_color = "light_blue"

        # Converter Frame
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
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
                                       font="Arial 10 italic", wrap=250,
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
                                   bg="Khakil", padx=10, pady=10,
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

    def temp_convert(self, to):
        print(to)

        # retrieve amount entered into entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)

            # Check amount is a valid number

            # Convert to F

            # Convert to C

            # Round!!

            # Display answer

            # Add answer to list for History

        except ValueError:
            self.converted_label.configure(text="Enter a number!!!", fg="red")
            self.to_convert_entry.configure(bg="pink")







# main rountine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")