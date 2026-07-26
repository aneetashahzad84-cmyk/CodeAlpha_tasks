from tkinter import *
from tkinter import messagebox
import csv
import os

FILE_NAME = "database.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Phone"])


def display_records():
    record_box.delete("1.0", END)

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) == 3:
                record_box.insert(
                    END,
                    f"Name: {row[0]} | Email: {row[1]} | Phone: {row[2]}\n"
                )


def add_record():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    if name == "" or email == "" or phone == "":
        messagebox.showwarning("Warning", "Please fill all fields.")
        return

    records = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        duplicate = False

        for row in reader:
            records.append(row)

            if len(row) == 3:
                if (
                    row[0].lower() == name.lower()
                    or row[1].lower() == email.lower()
                    or row[2] == phone
                ):
                    duplicate = True

    if duplicate:
        messagebox.showinfo(
            "Duplicate Removed",
            "Duplicate record already exists."
        )
        clear_fields()
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])

    messagebox.showinfo("Success", "Record Added Successfully")

    clear_fields()
    display_records()


def clear_fields():
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)


root = Tk()
root.title("Data Redundancy Removal System")
root.geometry("760x650")
root.configure(bg="lightblue")

Label(
    root,
    text="Data Redundancy Removal System",
    font=("Arial", 22, "bold"),
    bg="lightblue"
).pack(pady=10)

Label(root, text="Name", font=("Arial", 12), bg="lightblue").pack()

name_entry = Entry(root, width=35, font=("Arial", 12))
name_entry.pack(pady=5)

Label(root, text="Email", font=("Arial", 12), bg="lightblue").pack()

email_entry = Entry(root, width=35, font=("Arial", 12))
email_entry.pack(pady=5)

Label(root, text="Phone", font=("Arial", 12), bg="lightblue").pack()

phone_entry = Entry(root, width=35, font=("Arial", 12))
phone_entry.pack(pady=5)

Button(
    root,
    text="Add Record",
    width=18,
    bg="green",
    fg="white",
    font=("Arial", 11),
    command=add_record
).pack(pady=10)

Button(
    root,
    text="Clear",
    width=18,
    bg="orange",
    font=("Arial", 11),
    command=clear_fields
).pack()

Label(
    root,
    text="Stored Records",
    font=("Arial", 16, "bold"),
    bg="lightblue"
).pack(pady=15)

record_box = Text(root, width=70, height=12, font=("Arial", 10))
record_box.pack()

display_records()

root.mainloop()