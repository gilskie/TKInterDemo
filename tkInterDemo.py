import tkinter


def main():
    widget = tkinter.Tk()
    widget.title("Sample")

    button = tkinter.Button(text = "hello", command = display_button_message)
    button.place(x = 100, y = 50)

    label = tkinter.Label(text = "click here")
    label.place(x=35, y = 50)

    widget.mainloop()

def display_button_message():
    widget2 = tkinter.Tk()
    widget2.title("sample 2")


main()