# Quiz App

The Quiz App is a Python application with a graphical user interface (GUI) that allows users to take a timed quiz on a specified subject. The app presents multiple-choice questions, tracks the user's answers, and provides a score report at the end of the quiz.

## Features

- Timed quiz with a customizable duration
- Multiple-choice questions with four options each
- Navigation between questions (previous and next)
- Submission confirmation for unanswered questions
- Score calculation and percentage
- Detailed question analysis in the result file

## Requirements

- Python 3.x
- tkinter module (usually included with Python)

## Installation

1. Clone the repository or download the source code files.
2. Ensure that you have Python 3.x installed on your system.

## Usage

1. Run the `gui.py` file using Python:

   ```
   python gui.py
   ```

2. Enter your name in the start screen and click the "Submit" button.
3. The quiz will start, and you will see the first question along with a timer.
4. Select your answer for each question using the radio buttons.
5. Navigate through the questions using the "Previous" and "Next" buttons.
6. Click the "SUBMIT" button to finish the quiz.
7. If there are unanswered questions, you will be prompted to confirm submission.
8. After submitting, your score and a detailed question analysis will be displayed, and the results will be saved to a text file.

## Customizing the Quiz

To customize the quiz questions and subject:

1. Open the `main.py` file.
2. Modify the `questions` list in the `Quiz` class constructor to add, remove, or update questions.
3. Each question is represented as a dictionary with the following keys:
   - `"question"`: The text of the question.
   - `"answer"`: The correct answer for the question.
   - `"options"`: A list of four options for the question.
4. Update the `subject` parameter in the `Quiz` class constructor to change the quiz subject.

## File Structure

- `gui.py`: Contains the `QuizApp` class responsible for the GUI and quiz functionality.
- `main.py`: Contains the `Quiz` class that manages the quiz questions and subject.

## Adding a Photo

To add a photo to the start screen of the Quiz App:

1. Save your desired image file (e.g., "quiz_image.png") in the same directory as `gui.py`.

2. In the `start_screen` method of the `QuizApp` class in `gui.py`, add:

   ```python
   self.photo = tk.PhotoImage(file="quiz_image.png")
   self.photo_label = tk.Label(self.root, image=self.photo, bg="#2C3E50") 
   self.photo_label.pack(pady=20)
   ```

3. In the `clear_widgets` method, add:

   ```python
   self.photo_label.destroy()
   ```

4. Adjust the image size and placement as needed by modifying the `file` parameter and the `pady` value in the `photo_label` configuration.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

This Quiz App was developed as a sample project to demonstrate the usage of Python and the tkinter module for creating graphical user interfaces.
