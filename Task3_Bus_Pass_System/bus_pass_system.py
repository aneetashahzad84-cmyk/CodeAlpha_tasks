from tkinter import *
from tkinter import ttk, messagebox
import csv
import os

FILE_NAME = "bus_pass.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "CNIC", "Route", "Pass Type", "Fare"])


def calculate_fare():
    if pass_type.get() == "Student":
        return 500
    return 1000


def add_pass():
    name = name_entry.get().strip()
    cnic = cnic_entry.get().strip()
    route = route_combo.get()
    ptype = pass_type.get()
    fare = calculate_fare()

    if name == "" or cnic == "":
        messagebox.showwarning("Warning", "Please fill all fields.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, cnic, route, ptype, fare])

    messagebox.showinfo(
        "Bus Pass Generated",
        f"Name : {name}\n"
        f"CNIC : {cnic}\n"
        f"Route : {route}\n"
        f"Pass Type : {ptype}\n"
        f"Fare : Rs.{fare}\n\n"
        f"Status : Saved Successfully"
    )

    load_data()
    clear_fields()


def load_data():
    listbox.delete(0, END)

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            listbox.insert(
                END,
                f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | Rs.{row[4]}"
            )


def clear_fields():
    name_entry.delete(0, END)
    cnic_entry.delete(0, END)
    route_combo.current(0)
    pass_type.set("Student")


root = Tk()
root.title("Cloud Bus Pass System")
root.geometry("700x700")
root.configure(bg="lightblue")

Label(
    root,
    text="Cloud Bus Pass System",
    font=("Arial", 24, "bold"),
    bg="lightblue"
).pack(pady=10)

Label(
    root,
    text="Cloud Database Simulation (CSV Storage)",
    font=("Arial", 12),
    fg="blue",
    bg="lightblue"
).pack()

Label(root, text="Name", bg="lightblue", font=("Arial", 12)).pack()

name_entry = Entry(root, width=35, font=("Arial", 11))
name_entry.pack()

Label(root, text="CNIC", bg="lightblue", font=("Arial", 12)).pack()

cnic_entry = Entry(root, width=35, font=("Arial", 11))
cnic_entry.pack()

Label(root, text="Route", bg="lightblue", font=("Arial", 12)).pack()

route_combo = ttk.Combobox(
    root,
    values=["Route A", "Route B", "Route C"],
    state="readonly",
    width=20
)
route_combo.current(0)
route_combo.pack()

Label(root, text="Pass Type", bg="lightblue", font=("Arial", 12)).pack()

pass_type = StringVar(value="Student")

Radiobutton(
    root,
    text="Student",
    variable=pass_type,
    value="Student",
    bg="lightblue"
).pack()

Radiobutton(
    root,
    text="Regular",
    variable=pass_type,
    value="Regular",
    bg="lightblue"
).pack()

Button(
    root,
    text="Generate Pass",
    command=add_pass,
    bg="green",
    fg="white",
    width=20,
    font=("Arial", 11, "bold")
).pack(pady=10)

Button(
    root,
    text="Clear",
    command=clear_fields,
    bg="orange",
    width=20,
    font=("Arial", 11, "bold")
).pack()

Label(
    root,
    text="Issued Bus Passes",
    bg="lightblue",
    font=("Arial", 16, "bold")
).pack(pady=15)

listbox = Listbox(root, width=80, height=12, font=("Arial", 10))
listbox.pack()

load_data()

root.mainloop()