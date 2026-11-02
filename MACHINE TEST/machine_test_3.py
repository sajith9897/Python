students = [
    {"id": 1, "name": "rajesh"},
    {"id": 2, "name": "rahul"},
    {"id": 3, "name": "sruthi"}
]

while True:
    try:
        student_id = int(input("Enter student ID: "))

        found = False

        for student in students:
            if student["id"] == student_id:
                print("Student name:", student["name"])
                found = True
                break

        if not found:
            print("Student not found")

    except ValueError:
        print("Invalid input")