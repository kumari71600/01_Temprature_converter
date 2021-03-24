from tkinter import *
from functools import partial
import re

import random


class converter:
    def __init__(self):
        # Formatting Variables This color is blue.
        background_color = "#00c3ff"

        # Start list to hold calculation history
        self.all_calc_list = []

        # Converter Frame
        self.converter_frame = Frame(bg=background_color,
                                     pady=50)
        self.converter_frame.grid()

        # Temperature Converter Heading (Row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "19", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)
        # User Instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame, text="Type in the amount to be "
                                                                        "converted",
                                             font=("Arial", "10"), wrap=290, justify=LEFT,
                                             bg=background_color,
                                             padx=10, pady=10,
                                             )
        self.temp_instructions_label.grid(row=1)
        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20, font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3) Light blue for Celsius, light Red for Fahrenheit
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="Celsius", font="Arial 10 bold",
                                  bg="#74737A", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="Fahrenheit", font="Arial 10 bold",
                                  bg="#FFFFFF", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))

        self.to_f_button.grid(row=0, column=1)

        # Answer Label (row 4)
        self.converted_label = Label(self.converter_frame, width=10, font="Arial 14 bold", text="Conversion goes here",
                                     bg=background_color,
                                     fg='#800000', pady=10, padx=100)

        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font='Arial 12 bold', text="Calculation History",
                                       width=15, bg="#E1D5E7", command=lambda: self.history(self.all_calc_list))
        self.calc_hist_button.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.calc_hist_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help!", width=5, command=self.help,
                                  bg="#E1D5E7")
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)

        error = "#FADBD8"

        # Retrieve amount entered into Entry Field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check amount is a valid number

            # Convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = " {} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # Convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5 / 9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = " {} degrees F is {} degrees C".format(to_convert, celsius)

            # Input is too low
            else:
                answer = "Too Cold!"
                has_errors = "yes"

            # Display the Answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="#800000")
                self.to_convert_entry.configure(bg="white")

            else:
                self.converted_label.configure(text=answer, fg="#800000")
                self.to_convert_entry.configure(bg=error)

            # Add Answer to list for History.
            if has_errors != "yes":
                self.all_calc_list.append(answer)
                self.calc_hist_button.config(state=NORMAL)







        except ValueError:
            self.converted_label.configure(text="Enter a Number!", fg="yellow")
            self.to_convert_entry.configure(bg=error)

    # Rounding!
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

    def history(self, calc_history):
        History(self, calc_history)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Enter a number you wish to convert. \n\n"
                                          "The Calculation history shows up to the most recent 7 calculations.\n\n"
                                          "You may export your full calculation.")


class History:
    def __init__(self, partner, calc_history):
        # This color is green
        background = "#00c3ff"

        # disable history button
        partner.calc_hist_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press 'x' cross at the top, closes history and 'releases' history button.
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation history",
                                 font=("Arial", "15", "bold",),
                                 bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent calculations ",

                                  justify=LEFT, width=40, bg=background, wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # Generate string from list of calculations...

        history_string = ""
        if len(calc_history) > 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history) - item - 1] + "\n"


        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here are your most recent calculations ")

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (Row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial" "12" "bold",
                                    command=partial(lambda: self.export(calc_history)))
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 ", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.calc_hist_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)


class Help:
    def __init__(self, partner):
        # This color is blue
        background = "#00c3ff"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press 'x' cross at the top, closes help and 'releases' help button.
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font=("Arial", "15", "bold",),
                                 bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="orange",
                                  font="arial" "10" "bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class Export:
    def __init__(self, partner, calc_history):

        print(calc_history)

        # This color is  blue
        background = "#00c3ff"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press 'x' cross at the top, closes export and 'releases' export button.
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font=("Arial", "15", "bold",),
                                 bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text= "If the filename you entered already exists,"
                                                          "it will be overwritten.", justify=LEFT, bg=background,
                                 fg='#00c3ff', font="Arial 10 italic",
                                 wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

    def save_history(self, partner, calc_history):

        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = " (no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            self.save_error_label.config(text="Invalid filename - {}".format(problem))

            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            filename = filename + ".txt"

            f = open(filename, "w+")

            f.write("Temperature Convertor History\n")

            for item in calc_history:
                f.write(item + "\n")

            f.close()

            self.close_export(partner)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = converter()
    root.mainloop()