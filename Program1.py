# Program 1: Create a GUI window that displays your favorite saying.

import tkinter

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text = 'You might be doing too much')
        self.label.pack(padx = 10, pady = 10)
        tkinter.mainloop()

if __name__ == '__main__':
    main = myGUI()
