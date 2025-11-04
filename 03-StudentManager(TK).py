import tkinter as tk
from tkinter import *
from tkinter import messagebox

def student_records():
    students = []
    with open('studentMarks.txt', 'r', encoding='utf-8') as records:
        next(records)
        for line in records:
         clean_line = line.strip()

         parts = [part.strip() for part in clean_line.split(',')]

         student = {
         'name': parts[1],
         'number': parts[0],
         'coursework': int(parts[2]),
         'exam': int(parts[3]),
         'percent': int(parts[4]),
         'grade': int(parts[5])
            }
         students.append(student)
         
    return students

def individual_record(number):
    for s in student_records():
        if s['number'] == number:
            return s
    return None

def highest_mark():
   students = student_records()
   best_so_far = None
   highest_percent = -1

   for student in students:
        if student['percent'] > highest_percent:
            highest_percent = student['percent']
            best_so_far = student
   return best_so_far

def lowest_mark():
   students = student_records()
   less_so_far = None 
   lowest_percent = 9999

   for student in students:
        if student['percent'] < lowest_percent:
            lowest_percent = student['percent']
            less_so_far = student
   return less_so_far


root = tk.Tk()
root.geometry("600x400")
root.title("Student Manager")

tk.Label(root, text="Student Manager", font='Helvetica 18 bold').grid(row=0,column=0,padx=10,pady=10)

button_frame = tk.Frame(root)
button_frame.grid(pady=10)

def show_all():
    students = student_records()
    text_box.delete("1.0", tk.END)
    if not students:
        text_box.insert(tk.END, "No records found.\n")
        return
    for student in students:
        text_box.insert(tk.END, f"Name: {student['name']}\nNumber: {student['number']}\ncoursework: {student['coursework']}\nexam: {student['exam']}\npercent overall: {student['percent']}\ngrade: {student['grade']}\n\n")

def show_highest():
    student = highest_mark()
    text_box.delete("1.0", tk.END)
    if student:
        text_box.insert(tk.END, f"Name: {student['name']}\nNumber: {student['number']}\ncoursework: {student['coursework']}\nexam: {student['exam']}\npercent overall: {student['percent']}\ngrade: {student['grade']}\n")
    else:
        text_box.insert(tk.END, "No records found.")

def show_lowest():
    student = lowest_mark()
    text_box.delete("1.0", tk.END)
    if student:
        text_box.insert(tk.END, f"Name: {student['name']}\nNumber: {student['number']}\ncoursework: {student['coursework']}\nexam: {student['exam']}\npercent overall: {student['percent']}\ngrade: {student['grade']}\n")
    else:
        text_box.insert(tk.END, "No records found.")

def show_individual():
    number = id_entry.get()
    student = individual_record(number)
    text_box.delete("1.0", tk.END)
    if student:
        text_box.insert(tk.END, f"Name: {student['name']}\nNumber: {student['number']}\ncoursework: {student['coursework']}\nexam: {student['exam']}\npercent overall: {student['percent']}\ngrade: {student['grade']}\n")
    else:
        messagebox.showerror("Error", "Student not found")


tk.Button(button_frame, text="View All Records", command=show_all, width=20).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Show Highest", command=show_highest, width=20).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Show Lowest", command=show_lowest, width=20).grid(row=0, column=2, padx=5)


lookup_frame = tk.Frame(root)
lookup_frame.grid(pady=10)

tk.Label(lookup_frame, text="Enter Student ID:").grid(row=0, column=0)
id_entry = tk.Entry(lookup_frame, width=20)
id_entry.grid(row=0, column=1, padx=5)
tk.Button(lookup_frame, text="Find", command=show_individual).grid(row=0, column=2, padx=5)


text_box = tk.Text(root, height=15, width=80)
text_box.grid(pady=10)

root.mainloop()