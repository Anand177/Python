class Student:

    def __init__(self, name: str, age: int, grade: float):     
        self.name = name                
        self.age = age
        self.grade = grade

    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age

    def getGrade(self) -> float:
        return self.grade

    def setName(self, name: str):
        self.name = name

    def setAge(self, age: str):
        self.age = age

    def setGrade(self, grade: float):
        self.grade = grade

class Course:

    def __init__(self, course_name: str, max_students: int):
        self.course_name=course_name
        self.max_students=max_students
        self.students = []

    def add_student(self, student: Student) -> bool:
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def getAverageGrade(self) -> float:
        tot_grade : float = 0.0
        for student in self.students:
            tot_grade += student.getGrade()
        return tot_grade/len(self.students)


s1= Student("Anand", 38, 9)
s2= Student("Anvith", 7, 9.5)
s3= Student("ABC", 21, 7)

scienceCourse = Course("Science", 2)
print(scienceCourse.add_student(s1))
print(scienceCourse.getAverageGrade())
print(scienceCourse.add_student(s2))
print(scienceCourse.getAverageGrade())
print(scienceCourse.add_student(s3))
print(scienceCourse.getAverageGrade())

print(scienceCourse)