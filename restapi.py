import datetime
from oop import Student
import requests

url = "https://66666990a2f8516ff7a34e22.mockapi.io/api/v1/persons"


def fetch_students():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


# Fetch Student
json_response = fetch_students()
if json_response:
    student_list = []
    for std in json_response:
        student = Student(
            cityzen_id=std["cityzen_id"],
            first_name=std["first_name"],
            last_name=std["last_name"],
            dob=datetime.datetime.strptime(std["dob"], "%Y-%m-%dT%H:%M:%S.%fZ"),
            student_id=std["student_id"],
            school_name=std["school_name"],
        )
        student_list.append(student)
        print(student)
