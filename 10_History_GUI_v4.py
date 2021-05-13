from tkinter import *
from functools import partial   # To prevent unwanted windows
import random



class Converter:
    def __init__(self):

        # Formatting variables
        background_color = "light blue"

         # In actual program this is blank and is populated with user calculations
        self.all_calc_list = ["0 degrees C is -17.8 degrees F",
                          "0 degrees C is 32 degrees F",
                          "40 degrees C is 104 degrees F"
                          "40 degrees C is 4.4 degrees F"
                          "12 degrees C is 53.6 degrees F",
                          "24 degrees C is 75.2 degrees F",
                          "100 degrees C is 37.8 degrees F"]

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text = "Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # history Button (row 1)
        self.history_button = Button(self.converter_frame, text="history",
                           font=("Arial", "14"),
                           padx=10, pady=10, command=self.history)
        self.history_button.grid(row=1)

    def history(self):
        get_history = history(self)
        get_history.history_text.configure(text="history text goes here")


class history:
    def __init__(self,partner):

        background = "#a9ef99"  #Pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol("WM_DELETE_WINDOW", partial(self.close_history, partner))


        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, 
                                          text="Here are your most recent "
                                               "calculations.  Please use the "
                                               "export button to create a text "
                                               "file of all your calculations for "
                                               "this session", wrap=250,
                                          font="arial 10 italic",
                                          justify=LEFT, bg=background, fg="maroon",
                                          padx=10, pady=10)
        self.history_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.history_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                            command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()

        

