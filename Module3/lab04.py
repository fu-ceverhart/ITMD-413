def main():
    list_of_scores = get_test_scores()
    print("Test #\t\t\tTest Score\tLetter Grade")
    for i, score in enumerate(list_of_scores, start=1):
        grade = letter_grade(score)
        print(f"{i}\t\t\t{score:.2f}\t\t{grade}")
    print("Average:\t\t", f"{calculate_average(list_of_scores):.2f}")
    print("Letter Grade:\t\t", letter_grade(calculate_average(list_of_scores)))

def get_test_scores():
    count = 0
    list_of_scores = []
    while count < 5:
        score = float(input(f"Enter score for test {count + 1}: "))
        if 0 <= score <= 100:
            count += 1
            list_of_scores.append(score)
        else:
            print("Score must be between 0 and 100. Please try again.")
    return list_of_scores

def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

def letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

main()