import tkinter as tk
from random import choices
from string import ascii_letters, digits
from tkinter import font
from tkinter import messagebox
from PIL import ImageTk, Image

if __name__ == "__main__":
    print(">> welcome to password generator v1.1, developed by: Artin (Ketchup d) <<")


def randpass(length):
    return "".join(choices(
        ascii_letters + digits + "!@#$%&", k=length))


def password(nothing=0):
    global entry, textpassword, lenerr_msg, theme, copy2clip

    if lenerr_msg != 0:
        lenerr_msg.destroy()
        lenerr_msg = 0

    if textpassword != 0:
        textpassword.destroy()
        textpassword = 0

    if copy2clip != 0:
        copy2clip.destroy()
        copy2clip = 0

    try:
        if entry.get() == "":
            pass
        else:
            length = int(entry.get())
    except ValueError:
        print("ERROR: invalid input")
    else:
        if entry.get() == "":
            pass
        elif length <= 0:
            if theme.cget("image") == "pyimage2":
                lenerr_msg = tk.Label(frame_msg,
                                      text="password length cannot\n be zero or less.", font=font12, fg="#1A1A1A")
            elif theme.cget("image") == "pyimage3":
                lenerr_msg = tk.Label(frame_msg,
                                      text="password length cannot\n be zero or less.", font=font12, fg="#f0f0f0", bg="#1A1A1A")
            lenerr_msg.pack(pady=20)
            window.after(3000, lenerr_msg.destroy)
        else:
            if theme.cget("image") == "pyimage2":
                copy2clip = tk.Button(frame_copy2clip, text="copy to clipboard",
                                      bg="#f0f0f0", relief="solid", borderwidth=1, command=lambda: c2c(textpassword.get("1.0", tk.END)))
                copy2clip.pack(pady=15)
            if theme.cget("image") == "pyimage3":
                copy2clip = tk.Button(frame_copy2clip, text="copy to clipboard",
                                      bg="#1A1A1A", fg="white", relief="solid", borderwidth=1, command=lambda: c2c(textpassword.get("1.0", tk.END)))
                copy2clip.pack(pady=15)
            if theme.cget("image") == "pyimage2":
                textpassword = tk.Text(frame_password, font=font14,
                                       width=40, height=length/25, bg="#f0f0f0")
            elif theme.cget("image") == "pyimage3":
                textpassword = tk.Text(frame_password, font=font14,
                                       width=40, height=length/25, bg="#212121", fg="white")
            textpassword.pack()
            textpassword.insert(index="0.0", chars=randpass(length))


def txt(nothing=0):
    global theme, copy2clip

    try:
        if textpassword:
            password = textpassword.get("1.0", tk.END)
            with open("password.txt", "w") as txt:
                txt.write(password)
            messagebox.showinfo(
                "Done", "Generated password has been saved in the application directory.")
        else:
            if copy2clip != 0:
                copy2clip.destroy()
                copy2clip = 0
            messagebox.showerror(
                "No password", "Please generate a password first.")
    except Exception:
        if copy2clip != 0:
            copy2clip.destroy()
            copy2clip = 0
        messagebox.ERROR("No password", "Please generate a password first.")


def themechanger():
    global frame, frame_msg, frame_password, frame_theme, lenerr_msg, textpassword, entry, button, label, labelcopyright, theme, dark, light, window, frame_copy2clip, copy2clip

    if theme.cget("image") == "pyimage2":
        window.config(bg="#1A1A1A")
        frame.config(bg="#1A1A1A")
        frame_msg.config(bg="#1A1A1A")
        frame_password.config(bg="#1A1A1A")
        frame_theme.config(bg="#1A1A1A")
        frame_copy2clip.config(bg="#1A1A1A")
        label.config(fg="white", bg="#1A1A1A")
        entry.config(fg="white", bg="#212121")
        button.config(image=buttonimg_dark, bg="#1A1A1A")
        labelcopyright.config(bg="#1A1A1A")

        if lenerr_msg != 0:
            lenerr_msg.config(fg="#f0f0f0", bg="#1A1A1A")
        if textpassword != 0:
            textpassword.config(fg="white", bg="#212121")
        if copy2clip != 0:
            copy2clip.config(bg="#212121", fg="white")
        theme.config(image=light, bg="#1A1A1A")

    elif theme.cget("image") == "pyimage3":
        window.config(bg="#f0f0f0")
        frame.config(bg="#f0f0f0")
        frame_msg.config(bg="#f0f0f0")
        frame_password.config(bg="#f0f0f0")
        frame_theme.config(bg="#f0f0f0")
        frame_copy2clip.config(bg="#f0f0f0")
        label.config(fg="black", bg="#f0f0f0")
        entry.config(fg="black", bg="#f0f0f0")
        button.config(image=buttonimg_light, bg="#f0f0f0")
        labelcopyright.config(bg="#f0f0f0")

        if lenerr_msg != 0:
            lenerr_msg.config(fg="#1A1A1A", bg="#f0f0f0")
        if textpassword != 0:
            textpassword.config(fg="black", bg="#f0f0f0")
        if copy2clip != 0:
            copy2clip.config(bg="#f0f0f0", fg="black")
        theme.config(image=dark, bg="#f0f0f0")


def c2c(text):
    window.clipboard_clear()
    window.clipboard_append(text)


lenerr_msg = 0
textpassword = 0
copy2clip = 0

window = tk.Tk()

icon = tk.PhotoImage(
    file="models\\password_gen.png")
window.iconphoto(False, icon)

labelcopyright = tk.Label(
    text="© 2023 - Password Generator", fg="#949494")
labelcopyright.pack(side="bottom")

menu_bar = tk.Menu(window)

menu1 = tk.Menu(menu_bar, tearoff=0)

menu1.add_command(label="Save as txt", command=txt, accelerator="Ctrl+F")
menu1.add_command(label="Close", command=window.quit, accelerator="Alt+F4")

menu_bar.add_cascade(label="File", menu=menu1)

window.config(menu=menu_bar)

window.title("Password generator")

font18 = font.Font(size=18)
font14 = font.Font(size=14)
font12 = font.Font(size=12)

window.geometry("600x450")

dark = ImageTk.PhotoImage(Image.open(
    "models\\dark.png"))
light = ImageTk.PhotoImage(Image.open(
    "models\\light.png"))

frame_theme = tk.Frame(window, width=30, height=30)
frame_theme.pack(side="top", fill="both", pady=5, padx=5)
theme = tk.Button(frame_theme, image=dark,
                  command=themechanger, borderwidth=0)
theme.pack(side="left")

frame = tk.Frame(window)
frame.pack()

frame_copy2clip = tk.Frame(window)
frame_copy2clip.pack(side="bottom")

frame_password = tk.Frame(window)
frame_password.pack(pady=20)

frame_msg = tk.Frame(window)
frame_msg.pack(side="bottom")

label = tk.Label(frame, text="Password length:",
                 fg="#373737", font=font18)
label.pack()

entry = tk.Entry(frame, width=15, font=font14)
entry.pack()

buttonimg_light = ImageTk.PhotoImage(Image.open(
    "models\\button_light.png"))
buttonimg_dark = ImageTk.PhotoImage(Image.open(
    "models\\button_dark.png"))

button = tk.Button(frame, image=buttonimg_light,
                   command=password, borderwidth=0)
button.pack(pady=15)

window.bind_all("<Return>", password)
window.bind_all("<Control-f>", txt)

if __name__ == "__main__":
    window.mainloop()
