class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"


class Student(Person):
    def __init__(self, name, age, job, grade):
        super().__init__(name, age, job)
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Grade: {self.grade}"

class Professor(Person):
    def __init__(self, name, age, job, courses):
        super().__init__(name, age, job)
        self.courses = courses

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Courses: {self.courses}"

class Employee(Person):
    def __init__(self, name, age, job, department):
        super().__init__(name, age, job)
        self.department = department

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Department: {self.department}"

class StudentProfessor(Student, Professor):
    def __init__(self, name, age, job, courses, grade):
        # Initialize Person directly to avoid duplicate initialization
        Person.__init__(self, name, age, job)
        # Initialize specific attributes for Student and Professor
        self.courses = courses
        self.grade = grade

    def get_details(self):
        # Combine details from both Student and Professor
        return (f"Name: {self.name}, Age: {self.age}, Job: {self.job}, "
                f"Courses: {self.courses}, Grade: {self.grade}")

class Location:
    __slots__ = ('name', 'latitude', 'longitude')

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_coordinates(self):
        return (self.latitude, self.longitude)