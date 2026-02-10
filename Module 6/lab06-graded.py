employee_data = {}

with open("emp_data.txt", 'r') as file:
    for line in file:
        print("Employee ID:", line.split(", ")[0])
        print("Name:", line.split(", ")[1])