employee_data = {}

with open("emp_data.txt", 'r') as file:
    for i, line in enumerate(file, start=1):
        # print(i)
        # print("Employee ID:", line.split(", ")[0])
        # print("Name:", line.split(", ")[1])
        employee_data[i] = {
            "employee_id": int(line.split(", ")[0]),
            "employee_name": line.split(", ")[1].strip()
        }

for key, value in employee_data.items():
    print(f"Employee {key}: \n\tID: {value['employee_id']}\n\tName: {value['employee_name']}")
