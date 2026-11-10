# Day 2: Student Performance Calculator

name = input("Enter student name: ")

marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3
percentage = (total / 300) * 100

print("\n--- Student Performance Report ---")

print("Student:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage)

print("Passed:", average >= 50)