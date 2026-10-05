students = [
    "Amit", 78, 85, 91,
    "Riya", 88, 79, 84,
    "Rahul", 65, 70, 68,
    "Sneha", 92, 95, 89,
    "Karan", 81, 76, 80
]

i = 0

print(f"Name\t\tMaths\t\tSc.\t\tEng.\t\tTotal")
for n in range(len(students)//4):
    name = students[i]
    m = students[i+1]
    s = students[i+2]
    e = students[i+3]
    total = m + s + e

    print(f"{name}\t\t{m}\t\t{s}\t\t{e}\t\t{total}")

    i = i+4
