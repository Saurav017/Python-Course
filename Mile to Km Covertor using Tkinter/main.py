

from tkinter import *

window = Tk()
# setting a screen

window.title("Miles to KM Convertor")
window.minsize(width=300, height=200)
# setting tiltle and min screen size

def miles_to_km():

    """
    function to convert miles to km
    :return:
    """

    entry_miles = entry.get()
    in_km = round(int(entry_miles) * 1.602,2)
    label_2.config(text=f"{in_km}")
#     change the text

label_1 = Label(text="is equal to", font={"Arial", 24, "Bold"})
label_1.grid(row=3, column=3, padx=15, pady=15)
# for is equal to

label_2 = Label(text=0, font={"Arial", 24, "Bold"})
label_2.grid(row=3, column= 5, padx=15, pady=15)
# for 0

label_3 = Label(text="km", font={"Arial", 24, "Bold"})
label_3.grid(row=3, column=7, padx=15, pady=15)
# for km

label_4 = Label(text="Miles", font={"Arial", 24, "Bold"})
label_4.grid(row=1, column=7, padx=15, pady=15)
# for Miles

entry = Entry(width=15)
entry.grid(row=1, column=5, padx=25, pady=15)
# For entry

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=5, column=5, padx=25, pady=15)
# for button

window.mainloop()