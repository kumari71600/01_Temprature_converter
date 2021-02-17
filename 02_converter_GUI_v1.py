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
        self.temp_converter_label = Label(self.converter_frame,
                                          text="temperature Converter",
                                          font="Arial 16 bold",
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # User instructions (rov 1)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Type in the amount to be "
                                                "converter and then push "
                                                "one of the buttons below...",
                                       font="Arial 10 italic", wrap=250,
                                       justify=LEFT, bg=background_color,
                                       padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)


        # Temprature entry box (rov 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (rov 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                   bg="Khakil", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)


        # Answer label (rov 4)


        # History / Help button frame (rov 5)


# main rountine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")