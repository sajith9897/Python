python = {"Arun","Vinoy","Mahesh"}
data_science = {"Aromal","Pranav","Sooraj","Amal"}

python.add("Amal")
print("Students in python",python)

data_science.remove("Sooraj")
print("Students in data science",data_science)

print("Students in both courses:", python & data_science)

print ("Students only in python and not in data science:", python - data_science)

print("List of all students:", python | data_science)

courses = {
    "Python":len(python),
    "Data Science":len(data_science)
}
print (courses)

for course, count in courses.items():
    print (f"Course: {course}, Students: {count} ")

expected_growth = {course: count*2 
                   for course, count in courses.items()}
print("Expected Growth:",expected_growth)