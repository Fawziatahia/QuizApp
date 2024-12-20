import tkinter as tk
from tkinter import messagebox
from main import Quiz
import time

class QuizApp:
    def __init__(self, root, quiz, duration=60):  # duration in seconds
        self.root = root
        self.quiz = quiz
        self.questions = self.quiz.get_questions()
        self.subject = self.quiz.get_subject()
        self.score = 0
        self.question_index = 0
        self.answers = [None] * len(self.questions)  # Store answers for navigation
        self.duration = duration  # Timer duration
        self.end_time = time.time() + self.duration
        self.student_name = ""
        self.start_screen()

    def start_screen(self):
        self.clear_widgets()
        self.root.title("Quiz App")
        self.root.geometry("1280x720")
        self.root.config(bg="#2C3E50")

        self.title_label = tk.Label(self.root, text="Quiz App", font=("Century Gothic", 36, "bold"), fg="white", bg="#2C3E50")
        self.title_label.pack(pady=20)

        self.name_frame = tk.Frame(self.root, bg="#2C3E50")
        self.name_frame.pack(pady=50)

        self.name_label = tk.Label(self.name_frame, text="Enter your name:", font=("Century Gothic", 20), fg="white", bg="#2C3E50")
        self.name_label.pack(side="left", padx=10)

        self.name_entry = tk.Entry(self.name_frame, font=("Century Gothic", 20), width=30)
        self.name_entry.pack(side="left", padx=10)

        self.name_submit_button = tk.Button(self.name_frame, text="Submit", command=self.start_quiz, font=("Century Gothic", 20, "bold"), fg="white", bg="#E67E22")
        self.name_submit_button.pack(side="left", padx=10)

    def start_quiz(self):
        self.student_name = self.name_entry.get()
        if not self.student_name.strip():
            messagebox.showwarning("Input Error", "Please enter your name.")
        else:
            self.quiz_screen()

    def quiz_screen(self):
        self.clear_widgets()
        self.root.title("Quiz App")
        self.root.geometry("1280x720")
        self.root.config(bg="#2C3E50")

        self.create_widgets()
        self.show_question()
        self.update_timer()

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text=self.subject, font=("Century Gothic", 28, "bold"), fg="white", bg="#2C3E50")
        self.title_label.pack(pady=10)

        self.info_frame = tk.Frame(self.root, bg="#34495E")
        self.info_frame.pack(pady=10, fill="x")
        
        self.total_questions_label = tk.Label(self.info_frame, text=f"Questions: {len(self.questions)}", font=("Century Gothic", 18), fg="white", bg="#34495E")
        self.total_questions_label.pack(side="left", padx=20)

        self.time_label = tk.Label(self.info_frame, text="03:00", font=("Century Gothic", 18), fg="white", bg="#34495E")
        self.time_label.pack(side="right", padx=20)

        self.question_frame = tk.Frame(self.root, bg="#2C3E50")
        self.question_frame.pack(pady=10, fill="x")

        self.question_label = tk.Label(self.question_frame, text="", wraplength=1000, font=("Century Gothic", 20, "bold"), fg="white", bg="#2C3E50")
        self.question_label.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        self.option_vars = ["A", "B", "C", "D"]
        for i in range(4):
            frame = tk.Frame(self.root, bg="#2C3E50")
            frame.pack(pady=5, fill="x", padx=50)
            label = tk.Label(frame, text=self.option_vars[i], font=("Century Gothic", 18, "bold"), fg="white", bg="#E67E22", width=3, height=2)
            label.pack(side="left", padx=20)
            rb = tk.Radiobutton(frame, text="", variable=self.radio_var, value="", font=("Century Gothic", 18), fg="white", bg="#2C3E50", selectcolor="#E67E22", indicatoron=0, width=30, height=2, borderwidth=2, relief="groove", highlightthickness=0)
            rb.pack(side="left")
            self.radio_buttons.append(rb)

        self.nav_frame = tk.Frame(self.root, bg="#2C3E50")
        self.nav_frame.pack(pady=10)

        self.prev_button = tk.Button(self.nav_frame, text="Previous", command=self.prev_question, font=("Century Gothic", 18, "bold"), fg="white", bg="#E67E22")
        self.prev_button.pack(side="left", padx=20)

        self.next_button = tk.Button(self.nav_frame, text="Next", command=self.next_question, font=("Century Gothic", 18, "bold"), fg="white", bg="#E67E22")
        self.next_button.pack(side="left", padx=20)

        self.submit_button = tk.Button(self.root, text="SUBMIT", command=self.submit_quiz, font=("Century Gothic", 20, "bold"), fg="white", bg="#E67E22", activebackground="#E67E22", activeforeground="white")
        self.submit_button.pack(pady=10, fill="x", padx=50)

    def update_timer(self):
        remaining_time = self.end_time - time.time()
        if remaining_time > 0:
            minutes, seconds = divmod(int(remaining_time), 60)
            self.time_label.config(text=f"{minutes}:{seconds:02d} sec left")
            self.root.after(1000, self.update_timer)
        else:
            self.time_label.config(text="0:00 sec left")
            self.submit_quiz()

    def show_question(self):
        question_data = self.questions[self.question_index]
        self.question_label.config(text=f"{self.question_index + 1}. {question_data['question']}")
        for i, option in enumerate(question_data["options"]):
            self.radio_buttons[i].config(text=option, value=option)
        if self.answers[self.question_index] is not None:
            self.radio_var.set(self.answers[self.question_index])
        else:
            self.radio_var.set("")

    def prev_question(self):
        self.store_answer()
        if self.question_index > 0:
            self.question_index -= 1
            self.show_question()

    def next_question(self):
        self.store_answer()
        if self.question_index < len(self.questions) - 1:
            self.question_index += 1
            self.show_question()

    def store_answer(self):
        selected_answer = self.radio_var.get()
        if selected_answer:
            self.answers[self.question_index] = selected_answer

    def submit_quiz(self):
        self.store_answer()
        unanswered = self.answers.count(None)
        if unanswered > 0:
            if messagebox.askyesno("Unanswered Questions", f"There are {unanswered} unanswered questions. Do you want to submit anyway?"):
                self.calculate_score()
        else:
            self.calculate_score()

    def calculate_score(self):
        self.score = sum(1 for i, answer in enumerate(self.answers) if answer == self.questions[i]["answer"])
        percentage = (self.score / len(self.questions)) * 100
        
        # Create result file
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"quiz_result_{self.student_name}_{timestamp}.txt"
        
        with open(filename, "w", encoding='utf-8') as f:
            f.write(f"Quiz Results for {self.student_name}\n")
            f.write(f"Subject: {self.subject}\n")
            f.write(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Score: {self.score}/{len(self.questions)} ({percentage:.2f}%)\n")
            f.write("\nDetailed Question Analysis:\n")
            f.write("-" * 50 + "\n")
            
            for i, (question, answer) in enumerate(zip(self.questions, self.answers)):
                is_correct = "CORRECT" if answer == question["answer"] else "INCORRECT"
                f.write(f"\nQuestion {i+1}: {question['question']}\n")
                f.write(f"Your Answer: {answer if answer else 'Not answered'}\n")
                f.write(f"Correct Answer: {question['answer']}\n")
                f.write(f"Status: {is_correct}\n")
        
        messagebox.showinfo("Quiz Completed", 
                          f"Your score is {self.score}/{len(self.questions)} ({percentage:.2f}%)\n"
                          f"Results have been saved to {filename}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    quiz = Quiz(subject="Python")
    app = QuizApp(root, quiz)
    root.mainloop()