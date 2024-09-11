import json

# Reading the JSON file
with open('students.json', 'r') as file:
    data = json.load(file)

# Accessing the list of students
students = data['students']

# Process the data
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Math Grade: {student['grades']['math']}")
    print(f"Science Grade: {student['grades']['science']}")
    print()
