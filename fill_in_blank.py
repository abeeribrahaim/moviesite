# - *- coding: utf- 8 - *-
#quiz
easy_quiz = "The most basic use case for Python is as___1___ and___2___ language. Python isn’t just a replacement for___3___ or___4___, but is also used to automate___5___ with web browsers or application GUIs or system provisioning and configuration in tools such as Ansible and Salt."
madium_quiz = "Python is used for general application programming. Both ___1___ and ___2___ applications can be created with Python and ____3___ as self-contained executables. Python doesn’t have the native ability to generate a ___4___ from a script, but third-party packages like ___5____ or ___6___ can be used to accomplish that."
hard_quiz = "Python is used for ___1___ and ___2___. Python’s native libraries and third-party web frameworks provide ___3___ and ___4___ ways to create everything from simple ___5___ in a few lines of code, to ___6___, data-driven sites. Python’s latest versions have powerful support for asynchronous operations, allowing sites to handle up to tens of thousands of requests per second with the right libraries"
#answers
answers_easy = ["scripting","automation","shell scripts","batch files","interactions"]
answers_madium = ["CLI","cross-platform GUI","deployed","cx_Freeze","PyInstaller"]
answers_hard = ["web services","RESTful APIs","fast", "convenient","REST APIs","full-blown"]

blanks = ["___1___", "___2___", "___3___","___4___","___5___","___6___"]
# ask user to choose the difficulty level
def difficulty():
# when the user choose the the level,(the quize and the answer)are be called
    user_input = raw_input("please choose your level, easy, madium, hard !")
    if user_input == "easy":
        return easy_quiz, answers_easy
    elif user_input == "madium":
        return madium_quiz, answers_madium
    elif user_input == "hard":
        return hard_quiz, answers_hard
#replace the old text with new
def replacer(old,new,text):
    return text.replace(old, new)
# when the user answer the questions the text will change with user's answer
def check_answer(question, answers):
#the question number's order , (the quiz and answers start from 0)
    question_number = 0
    while question_number < len(answers):
        print question
#raw_input show the order of the question for user
        user_answer = raw_input("fill the blank"+blanks[question_number]+ "?")
        if user_answer == answers[question_number]:# check if the user answer is correct(and if it is correct "good job"will be printed )
            print "good job!"
            question =  replacer(blanks[question_number],user_answer, question)# change the quiz with user answer
            question_number += 1
# promet the user to answer correctly befor go to second question
        else:
            print "try again!"
def run():
#show and run the quiz from the biggning to the end(1/welcomed massege-2/difficulty level-3/check the answer-4/the end )
    print "welcome to Python fill in blank quiz"
    question, answers = difficulty()
    check_answer(question, answers)
    print "thank you"
run()
