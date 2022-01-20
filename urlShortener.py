from tkinter import *
import pyshorteners

root = Tk()
root.title("Vivekananda Gavini's URL Shortener")

root.geometry("500x600")

def shorten():
	if shorty.get():
		shorty.delete(0, END)

	if my_entry.get():
		# Convert to tinyurl
		url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
		# Output to screen
		shorty.insert(END, url)

		# Reverse URL
		print(pyshorteners.Shortener().tinyurl.expand(url))

def reset():
    my_entry.delete(0,END)
    shorty.delete(0,END)
    
def copyURL():
    root.clipboard_clear()
    root.clipboard_append(shorty.get())

my_label = Label(root, text="Enter Link To Shorten", font=("Helvetica", 34))
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

my_button = Button(root, text="Shorten Link", command=shorten, font=("Helvetica", 24))
my_button.pack(pady=20)

reset_button = Button(root, text="Reset Fields", command=reset, font=("Helvetica", 24))
reset_button.pack(pady=20)

shorty_label = Label(root, text="Shortened Link", font=("Helvetica", 14))
shorty_label.pack(pady=50)

shorty = Entry(root, font=("Helvetica", 22), justify=CENTER, width=30, bd=0, bg="white")
shorty.pack(pady=10)

copy_button = Button(root, text="Copy URL", command=copyURL, font=("Helvetica", 24))
copy_button.pack(pady=20)

root.mainloop()