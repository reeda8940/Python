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
             "6. What does the acronym APU stand for?\n a: Alternate Propulsion Unit\n  b: Automatic Pilot Utility\n c: Auxiliary Power Unit\n d: Airborne parachute utility",
             "7. What plane is known as the queen of the skies?\n a: Boeing 747\n b: Concord\n c: Airbus A380\n d: Boeing 737",
             "8. What is the 4 letter airport code for sydney's international airport?\n a: KLAX\n b: NZAA\n c: YSSY\n d: AUSD",
             "9. What was the fastest passenger plane in the world?\n a: A380\n b: SR-71\n c: Boeing 787\n d: Concord",
             "10. True or false. Is there an A380 freighter?\n a: True\n b: False",
             "11. What is the biggest plane in the world?\n a: Airbus A380\n b: Boeing 747\n c:Antonov 225\n d: Boeing 787",
             "12. What is the length of the longest runway in the world?")

# Making the tuple the stores all the answers
answers = ("c", "a", "d", "d", "b", "c", "a", "c", "d", "b", "c")


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
