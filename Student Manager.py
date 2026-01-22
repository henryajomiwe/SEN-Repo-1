# Student Result Management System

name = input("Enter student name: ")

scores = []
for i in range(3):
    score = int(input(f"Enter score {i+1}: "))
    scores.append(score)

total = sum(scores)
average = total / len(scores)

print("\n--- Student Result ---")
print("Name:", name)
print("Scores:", scores)
print("Total:", total)
print("Average:", average)
