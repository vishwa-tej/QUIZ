QUS = [
    {
        "question": "What is the correct file extension for Python files?",
        "choices": ["A) .pyth", "B) .pt", "C) .py", "D) .pyt"],
        "answer": "C"
    },
    {
        "question": "Which function is used to display output in Python?",
        "choices": ["A) write()", "B) print()", "C) display()", "D) output()"],
        "answer": "B"
    },
    {
        "question": "How do you start a comment in Python?",
        "choices": ["A) //", "B) #", "C) *", "D) --"],
        "answer": "B"
    },
    {
        "question": "What is the output of: print(2 + 3 * 4)?",
        "choices": ["A) 20", "B) 14", "C) 24", "D) 9"],
        "answer": "B"
    },
    {
        "question": "Which of the following is a valid variable name in Python?",
        "choices": ["A) 2var", "B) var_name", "C) var-name", "D) var name"],
        "answer": "B"
    },
    {
        "question": "How do you take input from the user in Python?",
        "choices": ["A) get()", "B) input()", "C) scan()", "D) read()"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used for function definition in Python?",
        "choices": ["A) function", "B) define", "C) def", "D) fun"],
        "answer": "C"
    },
    {
        "question": "What is the result of len(\"Python\")?",
        "choices": ["A) 5", "B) 6", "C) 7", "D) Error"],
        "answer": "B"
    }
]

score = 0


for i, q in enumerate(QUS, 1):
    print(f"\nQuestion {i}: {q['question']}")
    for choice in q["choices"]:
        print(choice)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.")

print(f"\nQuiz completed! Your score: {score}/{len(QUS)}")
