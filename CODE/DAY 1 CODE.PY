# Day 1: AI Learner Profile

name = input("Enter your name: ")
hours = float(input("How many hours will you study AI weekly? "))
topic = input("Which AI topic interests you most? ")

print("\n--- AI Learner Profile ---")
print("Name:", name)
print("Weekly study hours:", hours)
print("Favourite topic:", topic)

print("Your monthly study estimate:", hours * 4, "hours")