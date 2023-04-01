class ResearchManagement:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    
    def get_details(self):
        return f"Name: {self.name}\nDepartment: {self.department}"
    
class Supervisor(ResearchManagement):
    def __init__(self, name, department, area_of_expertise):
        super().__init__(name, department)
        self.area_of_expertise = area_of_expertise
    
    def get_details(self):
        return f"Name: {self.name}\nDepartment: {self.department}\nArea of expertise: {self.area_of_expertise}"
    
if __name__ == "__main__":
    researcher = ResearchManagement("John", "Physics")
    supervisor = Supervisor("Jane", "Chemistry", "Organic Synthesis")
    
    print(researcher.get_details())
    print(supervisor.get_details())
