import tkinter as tk
from random import choices
from string import ascii_letters, digits
from tkinter import font
from PIL import ImageTk, Image

if __name__ == "__main__":
    print(">> welcome to password generator v1.0, developed by: Artin (Ketchup d) <<")


def randpass(length):
    return "".join(choices(
        ascii_letters + digits + "!@#$%&", k=length))


def password(nothing=0):
    global entry, textpassword, lengtherror, nopassworderror, theme, copy2clip

    if nopassworderror != 0:
        nopassworderror.destroy()
        nopassworderror = 0

    if lengtherror != 0:
        lengtherror.destroy()
        lengtherror = 0

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
                lengtherror = tk.Label(frame_error,
                                       text="password length cannot\n be zero or less.", font=font12, fg="#1A1A1A")
            elif theme.cget("image") == "pyimage3":
                lengtherror = tk.Label(frame_error,
                                       text="password length cannot\n be zero or less.", font=font12, fg="#f0f0f0", bg="#1A1A1A")
            lengtherror.pack(pady=20)
        else:
            if theme.cget("image") == "pyimage2":
                copy2clip = tk.Button(frame_copy2clip, text="copy to clipboard",
                                      bg="#f0f0f0", command=lambda: ctcb(textpassword.get("1.0", tk.END)))
                copy2clip.pack(pady=15)
            if theme.cget("image") == "pyimage3":
                copy2clip = tk.Button(frame_copy2clip, text="copy to clipboard",
                                      bg="#1A1A1A", fg="white", command=lambda: ctcb(textpassword.get("1.0", tk.END)))
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
    global lengtherror, nopassworderror, theme, copy2clip

    if nopassworderror != 0:
        nopassworderror.destroy()
        nopassworderror = 0

    if lengtherror != 0:
        lengtherror.destroy()
        lengtherror = 0

    if copy2clip != 0:
        copy2clip.destroy()
        copy2clip = 0

    try:
        if textpassword:
            password = textpassword.get("1.0", tk.END)
            with open("password.txt", "w") as txt:
                txt.write(password)
        else:
            if theme.cget("image") == "pyimage2":
                nopassworderror = tk.Label(frame_error,
                                           text="Please generate a password first", font=font12, fg="#1A1A1A")
            elif theme.cget("image") == "pyimage3":
                nopassworderror = tk.Label(frame_error,
                                           text="Please generate a password first", font=font12, fg="#f0f0f0",  bg="#1A1A1A")
            nopassworderror.pack(pady=20)
    except Exception:
        if theme.cget("image") == "pyimage2":
            nopassworderror = tk.Label(frame_error,
                                       text="Please generate a password first", font=font12, fg="#1A1A1A")
        elif theme.cget("image") == "pyimage3":
            nopassworderror = tk.Label(frame_error,
                                       text="Please generate a password first", font=font12, fg="#f0f0f0",  bg="#1A1A1A")
        nopassworderror.pack(pady=20)


def themechanger():
    global frame, frame_error, frame_password, frame_theme, lengtherror, textpassword, nopassworderror, entry, button, label, labelcopyright, theme, dark, light, window, frame_copy2clip, copy2clip

    if theme.cget("image") == "pyimage2":
        window.config(bg="#1A1A1A")
        frame.config(bg="#1A1A1A")
        frame_error.config(bg="#1A1A1A")
        frame_password.config(bg="#1A1A1A")
        frame_theme.config(bg="#1A1A1A")
        frame_copy2clip.config(bg="#1A1A1A")
        label.config(fg="white", bg="#1A1A1A")
        entry.config(fg="white", bg="#212121")
        button.config(image=buttonimg_dark, bg="#1A1A1A")
        labelcopyright.config(bg="#1A1A1A")

        if lengtherror != 0:
            lengtherror.config(fg="#f0f0f0", bg="#1A1A1A")
        if textpassword != 0:
            textpassword.config(fg="white", bg="#212121")
        if nopassworderror != 0:
            nopassworderror.config(fg="#f0f0f0", bg="#1A1A1A")
        if copy2clip != 0:
            copy2clip.config(bg="#212121", fg="white")

        theme.config(image=light, bg="#1A1A1A")

    elif theme.cget("image") == "pyimage3":
        window.config(bg="#f0f0f0")
        frame.config(bg="#f0f0f0")
        frame_error.config(bg="#f0f0f0")
        frame_password.config(bg="#f0f0f0")
        frame_theme.config(bg="#f0f0f0")
        frame_copy2clip.config(bg="#f0f0f0")
        label.config(fg="black", bg="#f0f0f0")
        entry.config(fg="black", bg="#f0f0f0")
        button.config(image=buttonimg_light, bg="#f0f0f0")
        labelcopyright.config(bg="#f0f0f0")

        if lengtherror != 0:
            lengtherror.config(fg="#1A1A1A", bg="#f0f0f0")
        if textpassword != 0:
            textpassword.config(fg="black", bg="#f0f0f0")
        if nopassworderror != 0:
            nopassworderror.config(fg="#1A1A1A", bg="#f0f0f0")
        if copy2clip != 0:
            copy2clip.config(bg="#f0f0f0", fg="black")

        theme.config(image=dark, bg="#f0f0f0")


def ctcb(text):
    window.clipboard_clear()
    window.clipboard_append(text)


lengtherror = 0
textpassword = 0
nopassworderror = 0
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
theme = tk.Button(frame_theme, image=dark, command=themechanger, borderwidth=0)
theme.pack(side="left")

frame = tk.Frame(window)
frame.pack()

frame_copy2clip = tk.Frame(window)
frame_copy2clip.pack(side="bottom")

frame_password = tk.Frame(window)
frame_password.pack(pady=20)

frame_error = tk.Frame(window)
frame_error.pack(side="bottom")

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
