class Professor:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def greet_students(self):
        print("Welcome to class!")

# Define ScienceProfessor as a subclass of Professor
class ScienceProfessor(Professor):
    def greet_students(self):
        print("Hi everyone! It's a great day to study Science!")
        super().greet_students()  # Call the greet_students method from the parent class

# Create an instance of ScienceProfessor and assign to a variable
science_professor = ScienceProfessor("Dr. Smith", 40, "Biology")

# Call the greet_students method of the ScienceProfessor instance
science_professor.greet_students()

