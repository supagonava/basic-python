import datetime


class Person:
    cityzen_id: str
    first_name: str
    last_name: str
    dob: datetime.datetime

    def __init__(self, cityzen_id: str, first_name: str, last_name: str, dob: datetime):
        self.cityzen_id = cityzen_id
        self.first_name = first_name

        # Optional condition
        if len(first_name) > 8:
            self.first_name = first_name[:8]

        self.last_name = last_name
        self.dob = dob

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    student_id: str
    school_name: str

    def __init__(self, cityzen_id: str, first_name: str, last_name: str, student_id: str, school_name: str, dob: datetime):
        self.cityzen_id = cityzen_id
        self.first_name = first_name
        self.student_id = student_id
        self.school_name = school_name

        # Optional condition
        if len(first_name) > 8:
            self.first_name = first_name[:8]

        self.last_name = last_name
        self.dob = dob

    @property
    def schoolname_with_stdid(self):
        return f"school : {self.school_name}, std id: {self.student_id}"


supakorn_person = Person(first_name="supakorn55555", last_name="emchannon", cityzen_id="111000", dob=datetime.datetime.now())
print(supakorn_person.get_fullname())

supakorn_student = Student(first_name="supakorn", last_name="emchannon", cityzen_id="111000", dob=datetime.datetime.now(), school_name="RMUTT", student_id="1234")
print(supakorn_student.get_fullname(), supakorn_student.schoolname_with_stdid)
