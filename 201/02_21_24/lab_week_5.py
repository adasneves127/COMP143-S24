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
#   d. Write sentences that conveys the minimum value of a prize, the maximum value of a prize,
#       and the total value of all the prizes. Use Python functions on lists and use f-strings.
#       Use the Python slide on lists for guidance.

import random

student_names = ["Alex C.", "Jayden D.", "Vijonet D.", "Sean F.", "Brandon K.", "Benjamin L.", "Nicholas P.", "Josh S."]
# print(student_names[0])
# print(student_names[1])
# print(student_names[-1])
# print(student_names[7])

random_index = random.randrange(len(student_names))
# Alternative Methods:
# random_index = random.randint(0, 7)
# random_index = random.randint(0, len(student_names) - 1)

print(student_names[random_index])

prizes = ["Phone", "Car", "House", "Cash Prize"]
prize_values = [1_500, 45_000, 500_000, 750_000]
prize_index = random.randrange(0, 4)

print(f"Congratulations {student_names[random_index]}, you have won a {prizes[prize_index]}, worth ${prize_values[prize_index]}")
print(f"Congratulations {student_names[random_index]}, you have won two {prizes[prize_index]}s, worth ${prize_values[prize_index] * 2}")

prize_values[2] = prize_values[2] + 50_000

print(f"Congratulations {student_names[random_index]}, you have won a {prizes[prize_index]}, worth ${prize_values[prize_index]}")


print(f"The minimum prize value is: {min(prize_values)}, the maximum prize value is: {max(prize_values)}, and the total value is: {sum(prize_values)}")
