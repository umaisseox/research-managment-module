""" Name:Umais
    Section and semester: (2E) 2nd semester
    Rollno:F22BSEEN1E02088"""
class Student:
    def __init__(self, name, email, phone_number, student_id, supervisor, degree, research_start_date, research_topic):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.student_id = student_id
        self.supervisor = supervisor
        self.degree = degree
        self.research_start_date = research_start_date
        self.research_topic = research_topic

class Supervisor:
    def __init__(self, name, email, phone_number, supervisor_id):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.supervisor_id = supervisor_id
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
def print_student_info(student):
    print("Name:", student.name)
    print("Email:", student.email)
    print("Phone Number:", student.phone_number)
    print("Student ID:", student.student_id)
    print("Degree:", student.degree)
    print("Supervisor:", student.supervisor.name)
    print("Research Start Date:", student.research_start_date)
    print("Research Topic:", student.research_topic)

def print_supervisor_info(supervisor):
    print("Name:", supervisor.name)
    print("Email:", supervisor.email)
    print("Phone Number:", supervisor.phone_number)
    print("Supervisor ID:", supervisor.supervisor_id)
    print("Students under Supervision:")
    for student in supervisor.students:
        print(student.name)
      # Create some example students and supervisors
s1 = Student("Ajmal", "john@example.com", "123-456-7890", 1, Supervisor("Dr. Jane Doe", "jane@example.com", "555-555-5555", 1), "Ph.D.", "2022-01-01", "Artificial Intelligence")
s2 = Student("Hassan", "alice@example.com", "987-654-3210", 2, Supervisor("Dr. Bob Smith", "bob@example.com", "555-555-5555", 2), "MPhil", "2022-02-01", "Data Science")
s3 = Student("Ahmad", "james@example.com", "555-555-5555", 3, Supervisor("Dr. Jane Doe", "jane@example.com", "555-555-5555", 13), "Ph.D.", "2022-01-01", "Computer Vision")

# Add the students to their supervisors' lists
s1.supervisor.add_student(s1)
s2.supervisor.add_student(s2)
s3.supervisor.add_student(s3)

# Call the print_student_info method for a specific student
print_student_info(s2)

# Call the print_sup

