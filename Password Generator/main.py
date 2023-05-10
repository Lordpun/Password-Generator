import tkinter as tk
from generate import *
def get_text():
    text = textbox.get()
    text2 = textbox2.get()
    text3 = textbox3.get()
    password = generate(text3, text, text2)
    with open("Passwords.txt", "a") as passwords:
      passwords.write(f"Website: {text}\n")
      passwords.write(f"User: {text2}\n")
      passwords.write(f"Password: {password}\n")
      passwords.write("-------------\n")
root = tk.Tk()

root.minsize(600, 500)
root.title('Password Generator')

label = tk.Label(root, text="Password Generation", font=('Arial', 18), anchor="center")
label.grid(row=0, column=0, padx=20, pady=5)

label2 = tk.Label(root, text='Website:', font=('Arial', 10), anchor="w")
label2.grid(row=1, column=0, padx=20, pady=5)

textbox = tk.Entry(root)
textbox.grid(row=1, column=1)
textbox2 = tk.Entry(root)
textbox2.grid(row=2, column=1)
textbox3 = tk.Entry(root)
textbox3.grid(row=3, column=1)
label3 = tk.Label(root, text='Username:', font=('Arial', 10), anchor="w")
label3.grid(row=2, column=0, padx=20, pady=5)

label4 = tk.Label(root, text='Password Size:\n(recommended to the max the website allows', font=('Arial', 10), anchor="w")
label4.grid(row=3, column=0, padx=20, pady=5)

button = tk.Button(root, text="Get Password", command=get_text)
button.grid(row=4, column=0, padx=20, pady=5)
root.mainloop()
