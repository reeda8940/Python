import time

# Making the tuple that stores all the questions
questions = ("\n1. What is the best selling aircraft in the world?\n a: A320\n b: Boeing 737\n c: Cessna 172\n d: A380",
             "\n2. What is the first plane ever created?\n a: The Wright Flyer\n b: Boeing 001\n c: Airbus A123\n d: The Airplane",
             "\n3. When was the first plane made?\n a: 1893\n b: 1915\n c: 1900 \n d: 1903",
             "\n4. How many buttons and switches are in the cockpit of the Airbus A380?\n a: 420\n b: 273\n c: 320\n d: 490",
             "\n5. What airline has the call sign CACTUS?\n a: American Airlines\n b: US Airways\n c: Emirates\n d: None",
             "\n6. What does the acronym APU stand for?\n a: Alternate Propulsion Unit\n  b: Automatic Pilot Utility\n c: Auxiliary Power Unit\n d: Airborne parachute utility",
             "\n7. What plane is known as the queen of the skies?\n a: Boeing 747\n b: Concord\n c: Airbus A380\n d: Boeing 737",
             "\n8. What is the 4 letter airport code for sydney's international airport?\n a: KLAX\n b: NZAA\n c: YSSY\n d: AUSD",
             "\n9. What was the fastest passenger plane in the world?\n a: A380\n b: SR-71\n c: Boeing 787\n d: Concord",
             "\n10. True or false. Is there an A380 freighter?\n a: True\n b: False",
             "\n11. What is the biggest plane in the world?\n a: Airbus A380\n b: Boeing 747\n c: Antonov 225\n d: Boeing 787",
             "\n12. What is the length of the longest runway in the world?\n a: 5000m\n b: 4190mm\n c: 4900\n d: 5200m",
             "\n13. What airline is known for their hard landings?\n a: Lufthansa\n b: Easyjet\n c: Ryan Air\n d: American airlines",
             "\n14. What is the glide slope angle for landing?\n a: 4 degrees\n b: 5 degrees\n c: 2 degrees\n d: 3 degrees",
             "\n15. What does the acronym TOGA mean?\n a: Take Off, Go Around\n b: Throttle On Greatest Availability\n c: Thrust Override Greater Availability\n d: None of the above")

# Making the tuple the stores all the answers
answers = ("c", "a", "d", "d", "b", "c", "a", "c", "d", "b", "c", "a", "c", "d", "a")


def qna():  # Making the questions function
    # This is the first text that tells you what the quiz is about and how to play the quiz
    print("""Welcome to the quiz about Aviation. It is a multiple choice quiz.
You will get a question and there will be a set of answers below the question. To answer the question enter the letter that is associated to
your answer""")
    time.sleep(5)
    points = 0
    for i in range(len(questions)):  # Getting the length of the questions

        print(questions[i])  # This prints out the questions in order
        user_answer = input("Answer: ")  # This gets the users answer
        user_a_lower = user_answer.lower()  # Makes sure the input can be capitalised and still work
        if user_a_lower == answers[i]:  # This if statement checks the answer and tells the user if they are correct
            print("Correct")  # Tells the user if the answer is correct
            points += 1  # Making the points go up every time they get a question correct
            time.sleep(1.5)  # Waits 1.5 seconds before the next question pops up
        else:
            print("Incorrect")  # Tells the user if the answer is incorrect
            time.sleep(1.5)  # Waits 1.5 seconds before the next question pops up
    # Calculates the percent the user got
    if points >= 0:
        score = points / len(questions) * 100
        percent_score = round(score, 2)  # Rounds the percent to 2 decimal places
        print(f"\nYou got {percent_score}% on my aviation quiz\n")


# making the variable that starts the play


qna()  # Runs the code


# Once the user has completed the quiz, they are asked whether they want to play again.
def restart():
    reset = input("would you like to play again y/n : ")
    if reset == "y":
        return True
    else:
        print("Thanks for Playing")
        return False


while restart():
    qna()

