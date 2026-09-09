import numpy as np


employees = np.array([
    [95, 130, 5],
    [80,  70, 2],
    [98, 160, 7],
    [90, 105, 3],
    [85,  95, 4]
])


# Complete data
print("Employees:")
print(employees)


# First employee
print("\nFirst Employee:")
print(employees[0])


# Sales column
sales = employees[:, 1]

print("\nSales:")
print(sales)


# Attendance
attendance = employees[:, 0]

print("\nAttendance:")
print(attendance)


# Experience
experience = employees[:, 2]

print("\nExperience:")
print(experience)


# Statistics
print("\nAverage Sales:")
print(np.mean(sales))

print("\nHighest Sales:")
print(np.max(sales))


# Employees achieving target
achieved = employees[sales >= 100]

print("\nEmployees achieving target:")
print(achieved)


# Sales + Attendance condition
good_performers = employees[
    (sales >= 100) & (attendance >= 90)
]

print("\nGood Performers:")
print(good_performers)


# Highest sales employee
best_index = np.argmax(sales)

print("\nBest Employee Index:")
print(best_index)

print("\nBest Employee:")
print(employees[best_index])