import random

# student_names = ["Diana", "Alona", "John", "Sidora", "Yashira", "Okey", "Yi Yi"]
student_names = ["Alex C.", "Jayden D.", "Vijonet D.", "Sean F.", "Brandon K.", "Benjamin L.", "Nicholas P.", "Josh S."]


first_student = random.choice(student_names)
second_student = random.choice(student_names)

prizes = [("Television", 400), ("Car", 15_000), ("House", 400_000), ("Cash Prize", 1_000_000)]

first_prize = random.choice(prizes)

second_prize = random.choice(prizes)

print(f"Congratulations {first_student}! You have won a {first_prize[0]}, valued at ${first_prize[1]}")
print(f"Congratulations {second_student}! You have won two {second_prize[0]}s, valued at ${second_prize[1] * 2}")


# You do not need to know how these work.
# This is just so I could have my syntax work with the statistics
print(f"The minimum is {min([x[1] for x in prizes])}")
print(f"The minimum is {max([x[1] for x in prizes])}")
print(f"The minimum is {sum([x[1] for x in prizes])}")

