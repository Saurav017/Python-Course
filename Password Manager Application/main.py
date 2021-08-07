
from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip
import json

FONT = ("Arial", 10, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    #     module to copy password from the clipboard

    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():


    """
    Function that takes input entries that write those entries in a file
    :return:
    """
    website_name = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # creating a dictionary so that Json data get stored in it
    new_data = {
        website_name: {
            "email": email,
            "password": password
        }
    }


    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty")
    #     popups a message if you tried to add without entering any field

    else:
        try:
            with open('file.json', "r") as f:
                data = json.load(f)
                # load data from json files
                print(type(data))
                data.update(new_data)
                # updating old data with new data

        except FileNotFoundError:
            with open('file.json', "w") as f:
                json.dump(new_data, f, indent=4)
                # writing data in json files

        else:
            with open('file.json', "w") as f:
                json.dump(data, f, indent=4)
                # writing data in json files

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        #   clearing the input data entries after clicking the Add button

#---------------------------WEBSITE DATA SEARCH--------------------------------#


def search():
    """
    function to search through our json files
    :return:
    """

    website = website_entry.get()
    try:
        with open("file.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File Not Found")

    else:
        if website in data:
            #if website we entered in present on the data we loaded

            email = data[website]["email"]
            password = data[website]["password"]
                #getting hold of email and password
            messagebox.showinfo(title="Website", message=f"Email: {email} \nPassword: {password}")
            #     popups a message showing email and password

        else:
            #   if website not in data
            messagebox.showinfo(title="Website", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# setting up windows

########################################################################################


"""
creating image widgets
"""

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#######################################################################################

"""
Creating labels
"""

website_label = Label(text="Website", font=FONT)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username", font=FONT)
email_label.grid(row=2, column=0)

password_label = Label(text="Password", font=FONT)
password_label.grid(row=3, column=0)


#########################################################################################

"""
Creating entries
"""

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1,)
website_entry.focus()
    # focuses the cursor to this entry

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "saurav@gmail.com")
#     insert some default text in it

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)


###########################################################################################


"""
Creating Buttons
"""

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)


###########################################################################################

window.mainloop()