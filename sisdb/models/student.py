from datetime import datetime
#from course import Course
#from enrollment import Enrollment
#TASK 1
class Student:
    def __init__(self, StudentID, FirstName, LastName, DateOfBirth, Email, PhoneNumber):
        self._StudentID = StudentID
        self._FirstName = FirstName
        self._LastName = LastName
        self._DateOfBirth = DateOfBirth
        self._Email = Email
        self._PhoneNumber = PhoneNumber
        self._enrolled_courses=[]
        #self._payment_history = []
        #self._enrollments = []


    @property
    def StudentID(self):
        return self._StudentID

    @StudentID.setter
    def StudentID(self, new_StudentID):
        if isinstance(new_StudentID, int) and new_StudentID > 0:
            self._StudentID = new_StudentID
        else:
            raise ValueError("Student ID must be a positive integer.")

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, new_FirstName):
        if isinstance(new_FirstName, str) and new_FirstName:
            self._FirstName = new_FirstName
        else:
            raise ValueError("First name must be a non-empty string.")

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, new_LastName):
        if isinstance(new_LastName, str) and new_LastName:
            self._LastName = new_LastName
        else:
            raise ValueError("Last name must be a non-empty string.")

    @property
    def DateOfBirth(self):
        return self._DateOfBirth

    @DateOfBirth.setter
    def DateOfBirth(self, new_DateOfBirth):
        self._DateOfBirth = new_DateOfBirth

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, new_Email):
        if isinstance(new_Email, str) and "@" in new_Email:
            self._Email = new_Email
        else:
            raise ValueError("Invalid email format.")

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, new_PhoneNumber):
        if isinstance(new_PhoneNumber, str) and new_PhoneNumber.isdigit() and len(new_PhoneNumber) == 10:
            self._PhoneNumber = new_PhoneNumber
        else:
            raise ValueError("Invalid phone number format.")

    def EnrollInCourse(self, course):
        self._enrolled_courses.append(course)
        print(f"Student {self.FirstName} {self.LastName} enrolled in {course.CourseName}.")


    '''
    s= Student(StudentID=1, FirstName="Siddhant", LastName="Mundhe", DateOfBirth=datetime(2002, 3, 8),
                Email="siddhant.m@gmail.com", PhoneNumber="1234567890")
        math_course = Course(101, "Mathematics", "MATH101", "Professor Smith")

        s.EnrollInCourse(math_course)
    '''


    def UpdateStudentInfo(self, firstName, lastName, dateOfBirth, email, phoneNumber):
        self.FirstName = firstName
        self.LastName = lastName
        self.DateOfBirth = dateOfBirth
        self.Email = email
        self.PhoneNumber = phoneNumber
        print("Student information updated successfully.")

    '''
s= Student(StudentID=1, FirstName="Siddhant", LastName="Mundhe", DateOfBirth=datetime(2002, 3, 8),
                Email="siddhant.m@gmail.com", PhoneNumber="1234567890")
s.UpdateStudentInfo("Siddhant","Mundhe", (2001, 3, 8),"siddhant@gmail.com", "1234567880")
    '''


    def MakePayment(self, amount, paymentDate):
        payment_record = {"Amount": amount, "PaymentDate": paymentDate}
        self._payment_history.append(payment_record)
        print(f"Payment of {amount} made on {paymentDate} recorded successfully.")


    '''
s = Student(StudentID=1, FirstName="Siddhant", LastName="Mundhe", DateOfBirth=datetime(2002, 3, 8),
            Email="siddhant.m@gmail.com", PhoneNumber="1234567890")
s.MakePayment(50,"12-12-2023")
    '''


    def DisplayStudentInfo(self):
        print(f"Student ID: {self.StudentID}")
        print(f"Name: {self.FirstName} {self.LastName}")
        print(f"Date of Birth: {self.DateOfBirth}")
        print(f"Email: {self.Email}")
        print(f"Phone Number: {self.PhoneNumber}")


    '''
s = Student(StudentID=1, FirstName="Siddhant", LastName="Mundhe", DateOfBirth=datetime(2002, 3, 8),
            Email="siddhant.m@gmail.com", PhoneNumber="1234567890")
s.DisplayStudentInfo()
    '''

    def GetEnrolledCourses(self):
        return self._enrolled_courses
    '''
s= Student(StudentID=1, FirstName="Siddhant", LastName="Mundhe", DateOfBirth=datetime(2002, 3, 8),
            Email="siddhant.m@gmail.com", PhoneNumber="1234567890")
math_course = Course(101, "Mathematics", "MATH101", "Professor Smith")

s.EnrollInCourse(math_course)
s.GetEnrolledCourses()
    '''

    def GetPaymentHistory(self):
        return self._payment_history
    '''
s = Student(StudentID=1, FirstName="Siddhant", LastName="Mundhe", DateOfBirth=datetime(2002, 3, 8),
                Email="siddhant.m@gmail.com", PhoneNumber="1234567890")
s.MakePayment(50,"12-12-2023")
s.GetPaymentHistory()
    '''





