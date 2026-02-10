employee_data = {}

with open("emp_data.txt", 'r') as file:
    for i, line in enumerate(file, start=1):
        print(i)
        print("Employee ID:", line.split(", ")[0])
        print("Name:", line.split(", ")[1])