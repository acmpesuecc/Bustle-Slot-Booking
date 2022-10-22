import tkinter as tk #tkinter is used for GUI
import sqlite3 #used to work with sqlite databases

a = tk.Tk() #Tk() creates the main window and a is the main window object
a.title("BUSTLE Quiz Creator") #sets the title of the window
a.minsize(1000, 360)
a.maxsize(1000, 360) #defines the minimum and maximum sizes that the main window can be resized to

conn = sqlite3.connect("game_files/trivia/test.db") #creates a connection object to the database file test. We use this as SQLite stores databases in .db files instead of normal structred databases like SQL
cur = conn.cursor
cur.execute('DROP TABLE IF EXISTS Quiz;') #executes the SQL query to drop any existing table
cur.execute('''CREATE TABLE Quiz
             (Question           TEXT    NOT NULL,
             Option1            TEXT    NOT NULL,
             Option2            TEXT    NOT NULL,
             Option3            TEXT    NOT NULL,
             Option4            TEXT    NOT NULL);''') #creates a new table with the given constraints


def givedetails():
    data = [[que.get("0.0", tk.END)], [[opt1.get("0.0", tk.END)], [opt2.get("0.0", tk.END)], [opt3.get("0.0", tk.END)],
                                       [opt4.get("0.0", tk.END)]]] #END refers to the endpoint of user input

    conn.execute(f"INSERT INTO Quiz (QUESTION,OPTION1,OPTION2,OPTION3,OPTION4) \
          VALUES (?,?,?,?,?);", (data[0][0], data[1][0][0], data[1][1][0], data[1][2][0], data[1][3][0]))
    conn.commit() #commit() ensures that the changes made are committed into the database

    que.replace("0.0", tk.END, "")
    opt1.replace("0.0", tk.END, "")
    opt2.replace("0.0", tk.END, "")
    opt3.replace("0.0", tk.END, "")
    opt4.replace("0.0", tk.END, "")

#Everything on a tkinter window exists as a widget. Text() is a text widget
textq = tk.Text()
textoc = tk.Text()
texti1 = tk.Text()
texti2 = tk.Text()
texti3 = tk.Text()
que = tk.Text()
opt1 = tk.Text()
opt2 = tk.Text()
opt3 = tk.Text()
opt4 = tk.Text() #creates Text widgets
submit = tk.Button(width=15, text="Submit", command=givedetails) #creates a button widget that executes the function givedetails when clicked on

que.configure(width=92, height=5)
opt1.configure(width=92, height=2)
opt2.configure(width=92, height=2)
opt3.configure(width=92, height=2)
opt4.configure(width=92, height=2)
textq.insert("0.0", "Enter your question:-")
textoc.insert("0.0", "Enter the correct option:-")
texti1.insert("0.0", "Enter the incorrect option:-")
texti2.insert("0.0", "Enter the incorrect option:-")
texti3.insert("0.0", "Enter the incorrect option:-")
textq.configure(state="disabled", width=21, height=1)
textoc.configure(state="disabled", width=26, height=1)
texti1.configure(state="disabled", width=28, height=1)
texti2.configure(state="disabled", width=28, height=1)
texti3.configure(state="disabled", width=28, height=1)

textq.grid(row=0, column=0, padx=5) #grid is a method of adding widgets to the root window by defining a set of rows and columns. the position of widgets is specified by specifiying the row and column values
que.grid(row=0, column=1, padx=10)
textoc.grid(row=1, column=0, padx=5, pady=10)
opt1.grid(row=1, column=1, padx=5, pady=10)
texti1.grid(row=2, column=0, padx=5, pady=10)
opt2.grid(row=2, column=1, padx=5, pady=10)
texti2.grid(row=3, column=0, padx=5, pady=10)
opt3.grid(row=3, column=1, padx=5, pady=10)
texti3.grid(row=4, column=0, padx=5, pady=10)
opt4.grid(row=4, column=1, padx=5, pady=10)
submit.grid(row=5, pady=20) #padx and pady are the padding values along x and y axes

a.mainloop() #mainloop runs the tkinter code
conn.close() #closes the connection object to the database