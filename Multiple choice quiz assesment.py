import time

# This is the first text that tells you what the quiz is about and how to play the quiz
print("""Welcome to the quiz about Aviation. It is a multiple choice quiz.
You will get a question and there will be a set of answers below the question. To answer the question enter the letter that is associated to
your answer""")

time.sleep(7)

# Making the tuple that stores all the questions
questions = ("1. What is the best selling aircraft in the world?\n a: A320\n b: Boeing 737\n c: Cessna 172\n d: A380",
             "2. What is the first plane ever created?\n a: The Write Flyer\n b: Boeing 001\n c: Airbus A123\n d: The Airplane",
             "3. When was the first plane made?\n a: 1893\n b: 1915\n c: 1900 \n d: 1903",
             "4. How many buttons and switches are in the cockpit of the Airbus A380?\n a: 420\n b: 273\n c: 320\n d: 490",
             "5. What airline has the call sign CACTUS?\n a: American Airlines\n b: US Airways\n c: Emirates\n d: None",
             "6. What does the acronym APU stand for?\n a: Alternate Propulsion Unit\n  b: Automatic Pilot Utility\n c: Auxiliary Power Unit\n d: Airborne parachute utility")

# Making the tuple the stores all the answers
answers = ("c", "a", "d", "d", "b", "c")


def qna():  # Making the questions function
    for i in range(len(questions)):  # Getting the length of the questions
        print("""
________________________________________________________________
        """)  # This adds a dashed line in between questions, so it makes it easier to read
        print(questions[i])  # This prints out the questions in order
        user_answer = input("Answer: ")  # This gets the users answer
        user_a_lower = user_answer.lower()  # Makes sure the input can be capitalised and still work
        if user_a_lower == answers[i]:  # This if statement checks the answer and tells the user if they are correct
            print("Correct")  # Tells the user if the answer is correct
            time.sleep(1.5)  # Waits 1.5 seconds before the next question pops up
        else:
            print("Incorrect")  # Tells the user if the answer is incorrect
            time.sleep(1.5)  # Waits 1.5 seconds before the next question pops up


qna()  # Runs the code
