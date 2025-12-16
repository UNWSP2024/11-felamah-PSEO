# Program #2: Write a GUI program that displays your name and address when a
# "Show Info" button is clicked. There should also be a "Quit" button which exists the GUI.

import tkinter
import tkinter.messagebox

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.InfoButton = tkinter.Button(self.main_window, text = 'Show Info', command = self.InfoButton_Action)
        self.quitButton = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)
        self.main_window.title('Program #2 GUI Program.')

        self.InfoButton.pack(padx = 10, pady = 10)
        self.quitButton.pack(padx = 10, pady = 10)

        self.main_window.mainloop()

    def InfoButton_Action(self):
        tkinter.messagebox.showinfo('Name, Address', 'Faith Lamah, 12356 55th Orange SE, St. Michael')

if __name__ ==  '__main__':
    main = myGUI()
