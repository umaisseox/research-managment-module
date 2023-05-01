class Person:
    def __init__(self, name, email, phone):
        self._name = name
        self._email = email
        self._phone = phone

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone

    def set_name(self, name):
        self._name = name

    def set_email(self, email):
        self._email = email

    def set_phone(self, phone):
        self._phone = phone


class Asset:
    def __init__(self, name, description, owner):
        self._name = name
        self._description = description
        self._owner = owner

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_owner(self):
        return self._owner

    def set_name(self, name):
        self._name = name

    def set_description(self, description):
        self._description = description

    def set_owner(self, owner):
        self._owner = owner


class Supervisor(Person):
    def __init__(self, name, email, phone, research_area):
        super().__init__(name, email, phone)
        self._research_area = research_area
        self._students = []

    def get_research_area(self):
        return self._research_area

    def get_students(self):
        return self._students

    def add_student(self, student):
        self._students.append(student)


class Student(Person):
    def __init__(self, name, email, phone, supervisor):
        super().__init__(name, email, phone)
        self._supervisor = supervisor
        self._progress = []

    def get_supervisor(self):
        return self._supervisor

    def get_progress(self):
        return self._progress

    def add_progress(self, progress):
        self._progress.append(progress)


class MPhil(Student):
    def __init__(self, name, email, phone, supervisor, thesis_topic):
        super().__init__(name, email, phone, supervisor)
        self._thesis_topic = thesis_topic

    def get_thesis_topic(self):
        return self._thesis_topic


class PhD(Student):
    def __init__(self, name, email, phone, supervisor, thesis_topic, co_supervisor):
        super().__init__(name, email, phone, supervisor)
        self._thesis_topic = thesis_topic
        self._co_supervisor = co_supervisor

    def get_thesis_topic(self):
        return self._thesis_topic

    def get_co_supervisor(self):
        return self._co_supervisor


class AssetAllocation:
    def __init__(self, asset, owner):
        self._asset = asset
        self._owner = owner

    def get_asset(self):
        return self._asset

    def get_owner(self):
        return self._owner


# example usage
# create supervisor
supervisor1 = Supervisor("akash ajmal", "johnsmith@example.com", "555-1234", "Machine Learning")

# create students
student1 = MPhil("Alia jameel", "alicebrown@example.com", "555-5678", supervisor1, "Reinforcement Learning")
student2 = PhD("aqeel ahmad", "bobgreen@example.com", "555-9012", supervisor1, "Deep Learning", "Jane Doe")

# add students to supervisor
supervisor1.add_student(student1)
supervisor1.add_student(student2)

# create assets
asset1 = Asset("Computer", "Dell laptop", student1)
asset2 = Asset("Server", "HP ProLiant", student2)
asset3 = Asset("Camera", "Canon EOS 5D", supervisor1)

# allocate assets
allocation1 = AssetAllocation(asset1, student1)
allocation2 = AssetAllocation(asset2, student2)

# print student details, thesis topic, and supervisor details
print("Student 1:")
print("Name:", student1.get_name())
print("Email:", student1.get_email())
print("Phone:", student1.get_phone())
print("Thesis Topic:", student1.get_thesis_topic())
print("Supervisor Name:", student1.get_supervisor().get_name())
print("Supervisor Email:", student1.get_supervisor().get_email())
print("Supervisor Phone:", student1.get_supervisor().get_phone())

print("\nStudent 2:")
print("Name:", student2.get_name())
print("Email:", student2.get_email())
print("Phone:", student2.get_phone())
print("Thesis Topic:", student2.get_thesis_topic())
print("Supervisor Name:", student2.get_supervisor().get_name())
print("Supervisor Email:", student2.get_supervisor().get_email())
print("Supervisor Phone:", student2.get_supervisor().get_phone())
