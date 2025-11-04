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

def individual_records(input):
    students = student_records()
    for student in students:
        if student['number'] == input:
            print(f"Name: {student['name']}\nNumber: {student['number']}\ncoursework: {student['coursework']}\nexam: {student['exam']}\npercent overall: {student['percent']}\ngrade: {student['grade']}\n")
            break
        if input not in student:
         print("User not found\n")

def highest_mark():
   students = student_records()
   best_so_far = None 
   highest_percent = -1

   for student in students:
        if student['percent'] > highest_percent:
            highest_percent = student['percent']
            best_so_far = student

   if best_so_far:
       print(f"Name: {best_so_far['name']}\nNumber: {best_so_far['number']}\ncoursework: {best_so_far['coursework']}\nexam: {best_so_far['exam']}\npercent overall: {best_so_far['percent']}\ngrade: {best_so_far['grade']}\n")
   else:
        print("No student records found.")

def lowest_mark():
   students = student_records()
   less_so_far = None 
   lowest_percent = 9999

   for student in students:
        if student['percent'] < lowest_percent:
            lowest_percent = student['percent']
            less_so_far = student

   if less_so_far:
       print(f"Name: {less_so_far['name']}\nNumber: {less_so_far['number']}\ncoursework: {less_so_far['coursework']}\nexam: {less_so_far['exam']}\npercent overall: {less_so_far['percent']}\ngrade: {less_so_far['grade']}\n")
   else:
        print("No student records found.")


def main():

    program_running = ""
    
    while program_running.lower() != "9":
        print("1. View all student records\n2.View individual student record\n3.Show student with highest total score \n4.Show student with lowest total score \n5.Sort student records\n6.Add a student record\n7.Delete a student record\n8.Update a student record\n9.Close Program\n")
        program_running = input("Please select one of the following (enter the number):")
        if program_running.lower() == "1":
            students = student_records()
            for student in students:
             print(f"Name: {student['name']}\nNumber: {student['number']}\ncoursework: {student['coursework']}\nexam: {student['exam']}\npercent overall: {student['percent']}\ngrade: {student['grade']}\n")
        elif program_running.lower() == "2":
            user_id = input("enter ID: ")
            individual_records(user_id)
        elif program_running.lower() == "3":
           highest_mark()
        elif program_running.lower() == "4":
            lowest_mark()
        elif program_running.lower() == "5":
            #SORTING LIST
            pass
        elif program_running.lower() == "6":
            #ADD
            pass
        elif program_running.lower() == "7":
            user_id = input("enter ID: ")
            pass
        elif program_running.lower() == "8":
            #UPDATE
            pass
        elif program_running.lower() == "9":
            print("Closing program.")
        else:
            print("Invalid selection. Please try again.")

main()
