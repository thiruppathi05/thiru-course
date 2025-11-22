print("Welcome to your simple quiz chatbot!")
print("Answer each question by typing a, b, c, or d.\n")

score = 0

questions = [
    {
        "question": "1. What is the capital of France?",
        "options": {"a": "Berlin", "b": "Madrid", "c": "Paris", "d": "Rome"},
        "answer": "c"
    },
    {
        "question": "2. Which planet is known as the Red Planet?",
        "options": {"a": "Earth", "b": "Mars", "c": "Jupiter", "d": "Venus"},
        "answer": "b"
    },
    {
        "question": "3. Who wrote 'Romeo and Juliet'?",
        "options": {"a": "William Shakespeare", "b": "Mark Twain", "c": "Charles Dickens", "d": "J.K. Rowling"},
        "answer": "a"
    },
    {
        "question": "4. What is the largest ocean on Earth?",
        "options": {"a": "Atlantic Ocean", "b": "Indian Ocean", "c": "Pacific Ocean", "d": "Arctic Ocean"},
        "answer": "c"
    },
    {
        "question": "5. What gas do plants primarily take in?",
        "options": {"a": "Oxygen", "b": "Carbon Dioxide", "c": "Nitrogen", "d": "Hydrogen"},
        "answer": "b"
    },
    {
        "question": "6. How many continents are there on Earth?",
        "options": {"a": "5", "b": "6", "c": "7", "d": "8"},
        "answer": "c"
    },
    {
        "question": "7. What is the fastest land animal?",
        "options": {"a": "Cheetah", "b": "Lion", "c": "Horse", "d": "Gazelle"},
        "answer": "a"
    },
    {
        "question": "8. What is H2O commonly known as?",
        "options": {"a": "Salt", "b": "Water", "c": "Oxygen", "d": "Hydrogen"},
        "answer": "b"
    },
    {
        "question": "9. Which number is the Roman numeral 'X'?",
        "options": {"a": "5", "b": "10", "c": "50", "d": "100"},
        "answer": "b"
    },
    {
        "question": "10. What is the largest planet in our solar system?",
        "options": {"a": "Earth", "b": "Saturn", "c": "Jupiter", "d": "Neptune"},
        "answer": "c"
    }
]

for q in questions:
    print(q["question"])
    for key, value in q["options"].items():
        print(f"  {key}. {value}")

    while True:
        answer = input("Your answer: ").lower()
        if answer in ["a", "b", "c", "d"]:
            break
        else:
            print("Invalid input. Please type a, b, c, or d.")

    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect! The correct answer was '{q['answer']}'.\n")

print("Quiz complete!")
print(f"Your final score is: {score} out of {len(questions)}")

percentage = (score / len(questions)) * 100
print(f"That's {percentage:.1f}%")
89

