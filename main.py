from tkinter import *
from tkinter.scrolledtext import ScrolledText
import wikipedia as wiki
from tkinter.messagebox import askokcancel, showinfo
import threading


# Function

def search():
    # Function for getting user input and searching in wikipedia
    global lang_dict
    search_data = enter.get()
    val = lang.get()
    text.delete(0.0, END)
    text.insert(END, 'Searching for {}'.format(search_data))
    try:
        wiki.set_lang(lang_dict[val])
        data = wiki.summary(search_data, sentences=10)
    except Exception as e:
        data = e

    # delete current data from search box ..
    enter.set('')
    text.delete(0.0, END)
    # insert data into text scroll bar
    search_lbl['text'] = "Searching result for : {}".format(search_data)
    text.insert(0.0, data)


def call_search(*args):
    x = threading.Thread(target=search)
    x.start()


def call_back_for_root():
    # Conformation to Quit
    if askokcancel('Quit', 'Do you really want to quit?'):
        root.quit()


def copy_data(*args):
    data = text.get(0.0, END)  # Get all the content from text book
    if data:
        root.clipboard_clear()  # clear clipboard contents
        root.clipboard_append(data)  # append new value to clipboard
        showinfo('copy', 'Data is copied on Clipboard')


lang_dict = {'English': 'en', 'Hindi': 'hi', 'Gujarati': 'gu', 'French': 'fr', 'German': 'de'}

# main GUI window code
root = Tk()
root.title('Search Application')
root.geometry('320x480')
root.resizable(0, 0)
root.protocol("WM_DELETE_WINDOW", call_back_for_root)
root.configure(bg='white')

# Button variable
enter = StringVar()
lang = StringVar()

# Bar for input
search_bar = Entry(root, width=21, font=('arial', 14), bd=2, relief=RIDGE, textvariable=enter)
search_bar.bind('<Return>', call_search)
search_bar.place(x=18, y=20)

# Icon for executing search
img = PhotoImage(file='search.png')
search_button = Button(root, image=img, bd=2, relief=GROOVE, command=search)
search_button.place(x=250, y=20)

# Display input
search_lbl = Label(root, text='Searching result for :  ', font=('arial', 12, 'bold'), bg='white')
search_lbl.place(x=14, y=70)

# Scroll Bar for showing output
text = ScrolledText(root, font=('times', 12), bd=4, relief=SUNKEN, wrap=WORD, undo=True)
text.bind('<Double-1>', copy_data)
text.place(x=15, y=100, height=300, width=300)

# Drop down list for language selection
lang_list = list(lang_dict.keys())
lang.set(lang_list[0])
language = OptionMenu(root, lang, *lang_list)
language.place(x=20, y=420)

# Clear button for Clearing Output
clear_button = Button(root, text='Clear', font=('arial', 10, 'bold'), width=10, command=lambda: text.delete(0.0, END))
clear_button.place(x=110, y=420)

# Exit button to Quit
exit_button = Button(root, text='Exit', font=('arial', 10, 'bold'), width=10, command=root.quit)
exit_button.place(x=210, y=420)

root.mainloop()
