frontend = {"Rahul", "Noorudeen", "Glen", "Sajith"}
backend = {"Rahul", "Glen", "Amal", "Vishnu"}

backend.add("Manu")
print(backend)

frontend.remove("Sajith")
print(frontend)

print ("Students in both subjects:", frontend & backend)

print ("Students in backend only", backend - frontend)

print ("Total unique students:", len(frontend | backend))

courses = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}
print(courses)

for course, count in courses.items():
    print(f"Course: {course}, Students: {count}")

fullstack_courses = {
    course: count for course, count in courses.items()
}

fullstack_courses["Full Stack:"] = sum(courses.values())

print(fullstack_courses)