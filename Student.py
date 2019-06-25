class Student:

    def __init__(self, rno, name, marks):
        self.rno = rno
        self.name = name
        self.marks = marks

    def information(self):
        print("Roll no:", self.rno)
        print("Name:", self.name)
        print("Marks:", self.marks)


class College:

    def __init__(self, name, students):
        self.name = name
        self.students = students

    def show_student_list(self):
        for stu in self.students:
            stu.information()

    def enroll_new_student(self, stu):
        self.students.append(stu)
        print("New student is enrolled")

    def get_topper(self):
        topper = self.students[0]
        for stu in self.students:
            if topper.marks < stu.marks:
                topper = stu
        return topper

    def get_result(self, stu):
        if stu.marks >= 40:
            print("Pass")
        else:
            print("Fail")


s1 = Student(1, "A", 80)
s2 = Student(2, "B", 69)
s3 = Student(3, "C", 46)
s4 = Student(4, "D", 92)
s5 = Student(5, "E", 33)
s6 = Student(6, "F", 20)
s7 = Student(7, "G", 67)
c1 = College("ABCDEF", [s1, s2, s3, s4, s5, s6])

c1.show_student_list()
c1.enroll_new_student(s7)
c1.show_student_list()

print("Topper")
c1.get_topper().information()