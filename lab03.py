year = 1
tuition_rate = 5000
print(f"Year {year}:\t$ {tuition_rate:.2f}")
for i in range(4):
    year += 1
    tuition_rate *= 1.04
    print(f"Year {year}:\t$ {tuition_rate:.2f}")