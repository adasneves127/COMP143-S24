student = {
    'name': 'Alex Dasneves',
    'gpa': 3.7
}

print(student)
print(list(student.keys()))
print(list(student.items()))

for key in student.keys():
    print(f"{key} corresponds to {student[key]}")

# print(student['id'])

print(student.get('name'))

print(student.get('id', 'Not Found'))
print('id' in student)

student['id'] = '00426157'
print(student)
student['id'] = '00426175'
print(student)
# student.pop('id')
# print(student)

student['gpa'] = student['gpa'] - 0.2
print(student)

student['courses'] = []
print(student)
student['courses'].append('COMP 151')
student['courses'].append('COMP 143')
student['courses'].append('COMP 250')
student['courses'].append('COMP 206')
student['courses'].append('COMP 340')
student['courses'].append('COMP 350')

print(student)

for key in student.items():
    print(f"{key[0]} corresponds to {key[1]}")

print(list(student.values()))
