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
    print(state, capital)
    print("Your answer:", answer)
