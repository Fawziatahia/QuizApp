class Quiz:
    def __init__(self, subject="Hello"):
        self.subject = subject
        self.questions = [
            {"question": "What data type is the object below ? L = [1, 23, 'hello', 1]", "answer": "List", "options": ["List", "Tuple", "Set", "Dictionary"]},
            {"question": "What is 2 + 2?", "answer": "4", "options": ["3", "4", "5", "6"]},
            {"question": "Which operator is used to multiply numbers?", "answer": "*", "options": ["x", "%", "*", "#"]},
            {"question": "Which operator can be used to compare two values?", "answer": "==", "options": ["<>", "==","><","="]},
            {"question": "What is the correct file extension for Python files?", "answer": ".py", "options": [".pt", ".py", ".pyth", ".pyt"]},
            {"question": "What is the correct file extension for Hamim files?", "answer": "Hamim", "options": ["Hamim", ".py", ".pyth", ".pyt"]},
        ]

    def add_question(self, question, answer, options):
        self.questions.append({"question": question, "answer": answer, "options": options})

    def get_subject(self):
        return self.subject

    def get_questions(self):
        return self.questions

if __name__ == "__main__":
    quiz = Quiz(subject="Python")
    # Example of adding a new question
    quiz.add_question("What is the capital of Japan?", "Tokyo", ["Kyoto", "Osaka", "Tokyo", "Nagoya"])
    # Print all questions to verify addition
    for q in quiz.get_questions():
        print(q)