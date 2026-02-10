states_and_capitals = {
    "California": "Sacramento",
    "Texas": "Austin",
    "Florida": "Tallahassee",
    "New York": "Albany",
    "Colorado": "Denver"
}

correct = 0

for state, capital in states_and_capitals.items():
    answer = input(f"What is the capital of {state}? ")
    # print(state, capital)
    # print("Your answer:", answer)
    if answer == capital:
        print("Correct")
        correct += 1
    else:
        print("Wrong")

print(f"You got {correct} out of {len(states_and_capitals)} correct.")
