from tkinter import *
import random


class Foo:
    def __init__(self, parent):
        print("hello world")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Foo(root)
    root.mainloop()

