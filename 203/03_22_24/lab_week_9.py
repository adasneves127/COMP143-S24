numbers = [92,12,100,0,17,18]

new_list = []
for i in range(len(numbers)):
    new_list.append(numbers[-1*(i+1)])

print(new_list)

min_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num
# Result of our code:
print(min_num)
# Result of the built-in function:
print(min(numbers))

max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

# Result of our code:
print(max_num)
# Result of the built-in function:
print(max(numbers))


age = 15
if age <= 12:
    print("The ticket cost is $6")
if age > 12 and age < 55:
    print("The ticket cost is $12")
if age >= 55:
    print("The ticket cost is $8")

if age <= 12:
    print("The ticket cost is $6")
elif age < 55:
    print("The ticket cost is $12")
else:
    print("The ticket cost is $8")

placement_score = 3
gpa = 2.9

if placement_score >= 5:
    print("Take MATH 101")
if placement_score < 5 and gpa >= 3:
    print("Take MATH 101E")
if placement_score < 5 and gpa < 3:
    print("Take MATH 100")


if placement_score >= 5:
    print("Take MATH 101")
else:
    if gpa >= 3:
        print("Take MATH 101E")
    else:
        print("Take MATH 100")
