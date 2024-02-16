# 1. Assign a list of names of the students in the class to a variable.
#       Use standard Python naming conventions as discussed in class.
#       Print the first name from the list using indexing.
#       Print the second name from the list using indexing.
#       Print the last name from the list using indexing.
#       Print a name from the list at random using indexing.
#       Remember to import the random library.
# 2. Assign a list of prizes that can be won in a raffle to a variable.
#       Include four prizes 0, 1, 2, and 3, respectively.
#       Assign a list of monetary values for each of Prizes 0, 1, 2, and 3, respectively, to a variable.
#   a. Draw a prize at random by generating a random number 0, 1, 2, or 3 and
#       using it to index into the prize and value lists to write a sentence
#       that states the prize you won and its value. Use an f-string.
#   b. Draw a prize at random by generating a random number 0, 1, 2, or 3 and
#       using it to index into the prize and value lists to write a sentence
#       that states that you won TWO of one of the prizes, such as two televisions,
#       and their total value. Use an f-string. Round the price to two decimal places.
#   c. The value of one of the prizes increases. Modify one of the elements in the prize list accordingly,
#       using indexing as discussed in class from the Python slide (reference card on lists).
#       Repeat one of the drawings described above.
#   d. Write sentences that convey the minimum value of a prize, the maximum value of a prize,
#       and the total value of all the prizes. Use Python functions on lists and use f-strings.
#       Use the Python slide on lists for guidance.
import random

student_names = ["Diana", "Alona", "John", "Sidora", "Yashira", "Okey", "Yi Yi"]

student_index = random.randint(0, len(student_names) - 1)
first_student = student_names[student_index]



prizes = ["Television", "Car", "House", "Cash Prize"]
prize_values = [400, 15_000, 400_000, 1_000_000]

first_prize_index = random.randint(0, 3)
print(f'Congratulations {first_student}! You have won a {prizes[first_prize_index]}, worth ${prize_values[first_prize_index]}')
prize_values[0] = 700
print(f'Congratulations {first_student}! You have won a {prizes[first_prize_index]}, worth ${prize_values[first_prize_index]}')

next_student_index = random.randint(0, len(student_names) - 1)
second_student = student_names[next_student_index]

second_prize_index = random.randint(0, 3)
print(f"Congratulations {second_student}! You have won TWO {prizes[second_prize_index]}s, worth ${prize_values[second_prize_index] * 2}")

# print(random.choice(student_names))
print()
print(f"The maximum prize value is ${max(prize_values)}")
print(f"The minimum prize value is ${min(prize_values)}")
print(f"The total of the prize values is ${sum(prize_values)}")

