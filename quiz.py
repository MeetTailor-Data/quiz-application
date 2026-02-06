questions = []
score = 0

q1 = {
    "question": "What is the capital of India?",
    "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
    "answer": "A"
}

q2 = {
    "question": "Which language is used for Data Science?",
    "options": ["HTML", "Python", "CSS", "PHP"],
    "answer": "B"
}

q3 = {
    "question": "What is 5 + 3?",
    "options": ["5", "8", "10", "15"],
    "answer": "B"
}

questions.extend([q1, q2, q3])
total_questions = len(questions)

print("Welcome to The Quiz App Created By Meet Tailor!\n")

for q in questions:
    print(q["question"])

    options_labels = ["A", "B", "C", "D"]
    for i in range(4):
        print(options_labels[i] + ".", q["options"][i])

    user_ans = input("Enter your answer (A/B/C/D): ").upper()

    if user_ans == q["answer"]:
        score += 1
        print(" Correct Answer\n")
    else:
        correct_option = options_labels.index(q["answer"])
        print(" Wrong Answer")
        print("Correct Answer is:", q["options"][correct_option], "\n")

percentage = (score / total_questions) * 100

print("Total Questions:", total_questions)
print("Your Score:", score)
print("Your Percentage:", percentage)

if percentage >= 55:
    print("Result: PASS ")
else:
    print("Result: FAIL ")
