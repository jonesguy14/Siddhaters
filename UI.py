from tkinter import *
from tkinter import ttk

class TitleEntry(object):
    def getTitle(self, *args):
        try:
            self.SearchEntry = self.BookTitle.get()
            self.root.quit()
        except ValueError:
            pass

    def __init__(self):
        SearchEntry = None

    def SearchUI(self):
        self.root = Tk()
        self.root.title("Siddhaters")

        mainframe = ttk.Frame(self.root, padding="9 9 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        self.BookTitle = StringVar()

        title_entry = ttk.Entry(mainframe, width=20, textvariable=self.BookTitle)
        title_entry.grid(column=2, row=1, sticky=(W, E))
        ttk.Button(mainframe, text="Search", command=self.getTitle).grid(column=3, row=1, sticky=E)

        ttk.Label(mainframe, text="Book Title:").grid(column=1, row=1, sticky=W)

        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        title_entry.focus()
        self.root.bind('<Return>', self.getTitle)

        self.root.mainloop()