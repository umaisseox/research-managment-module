Name:umais riaz
Rollno:F22BSEEN1E02088
    
# Research Management Module

# Base class for supervisors
class Supervisors:
    def __init__(self, name, department):
        self.name = name
        self.department = department

# Base class for students
class Students:
    def __init__(self, name, id_number, supervisor):
        self.__name = name   # Encapsulation: Name is a private attribute and can be accessed only through getter method
        self.__id_number = id_number  # Encapsulation: ID number is a private attribute and can be accessed only through getter method
        self.__supervisor = supervisor   # Encapsulation: Supervisor is a private attribute and can be accessed only through getter method

    # Getter method for name attribute
    def get_name(self):
        return self.__name

    # Getter method for supervisor attribute
    def get_supervisor(self):
        return self.__supervisor

# Derived class for Mphil students
class MphilStudents(Students):
    def __init__(self, name, id_number, supervisor, mphil_topic):
        super().__init__(name, id_number, supervisor)   # Inheritance: MphilStudents inherits from Students
        self.mphil_topic = mphil_topic

# Derived class for PhD students
class PhDStudents(Students):
    def __init__(self, name, id_number, supervisor, phd_topic):
        super().__init__(name, id_number, supervisor)   # Inheritance: PhDStudents inherits from Students
        self.phd_topic = phd_topic

# Base class for research progress details
class ResearchProgress:
    def __init__(self, student, progress):
        self.student = student
        self.progress = progress

# Base class for asset allocations
class AssetAllocations:
    def __init__(self, asset_type, allocation_date):
        self.asset_type = asset_type
        self.allocation_date = allocation_date

# Multiple Inheritance: ResearchProgress and AssetAllocations are independent classes that can be used by any other class

# Sample Usage
supervisor1 = Supervisors("John", "Computer Science")
mphil_student1 = MphilStudents("Alice", "1234", supervisor1, "Natural Language Processing")
phd_student1 = PhDStudents("Bob", "5678", supervisor1, "Machine Learning")
research_progress1 = ResearchProgress(mphil_student1, "Literature review completed")   # Polymorphism: ResearchProgress class can be used for both mphil and phd students
asset_allocation1 = AssetAllocations("Laptop", "2022-01-01")

# Accessing private attributes using getter methods
print(mphil_student1.get_name())   # Encapsulation: Accessing private name attribute using getter method
print(phd_student1.get_supervisor())   # Encapsulation: Accessing private supervisor attribute using getter method

# Polymorphism example
research_progress2 = ResearchProgress(phd_student1, "Experiment setup completed")   # Polymorphism: ResearchProgress class can be used for both mphil and phd students
print(research_progress2.student.name + " - " + research_progress2.progress)
