from questions2 import quiz

score = 1000000

#Here quiz is the dictionary drawn from, and question will act as the variable 

for question in quiz:
    pass

for question in quiz:
    attempts = 1

while attempts <= 0:
    pass

#Now onto attempting to print the questions

#History section - using only questions numbered as five, not sections five 

#Question one

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["Which two symbols adorned the flag of the Soviet Union?"])
        answer = input("B" or "Hammer and Sickle")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["B" or "Hammer and Sickle"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Question two

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["In which year did the Russia Revolution first start to take place?"])
        answer = input("A" or "1917")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["A" or "1917"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Question three

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["Sir Walter Raleigh, a favourite of Elizabeth I, notoriously introduced tobacco to England - but which monarch ordered his execution?"])
        answer = input("C" or "James I")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["C" or "James I"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Question four

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["In 1066, who did William of Normandy defeat to claim the English throne?"])
        answer = input("C" or "Harold Godwineson")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["C" or "Harold Godwineson"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Music round

#Question one

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["Vanessa Carlton became a one-hit wonder for which 2001 song?"])
        answer = input("B" or "A Thousand Miles")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["B" or "A Thousand Miles"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Question two

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["What is David Bowie's real surname?"])
        answer = input("D" or "Jones")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["D" or "Jones"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Question three

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["What is the name of Parmore’s debut album?"])
        answer = input("C" or "All We Know Is Falling")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["C" or "All We Know Is Falling"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Question four

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["Including streaming figures, what was the best-selling UK single of the 2010s?"])
        answer = input("C" or "Shape of You - Ed Sheeran")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["C" or "Shape Of You - Ed Sheeran"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#General Knowledge round

#Question one

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["In the NATO phonetic alphabet, what word represents the letter 'O'?"])
        answer = input("A" or "Oscar")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["A" or "Oscar"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Question two

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["Charles Dickens wrote A Tale of Two Cities. What are the 2 cities?"])
        answer = input("B" or "London and Paris")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["B" or "London and Paris"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Question three

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["Which gas is the most found in abundance in the Earth's atmosphere?"])
        answer = input("B" or "Nitrogen")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["B" or "Nitrogen"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Question four

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["In chess, which piece cannot move in a straight line?"])
        answer = input("A" or "Knight")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["A" or "Knight"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Technology round

#Question one

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["What does a Geiger counter measure?"])
        answer = input("D" or "Radiation")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["D" or "Radiation"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Question two

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["What is Elon Musk's aerospace company called?"])
        answer = input("D" or "SpaceX")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["D" or "SpaceX"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Question three

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["What Company did Elon musk found?"])
        answer = input("B" or "Tesla")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["B" or "Tesla"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False

#Question four

for question in quiz:
    attempts = 1
        while attempts <= 0:
            print(quiz[question]["In which decade was the Sony Walkman launched?"])
        answer = input("B" or "1970s")
            check = check_ans(question, answer, attempts, score)
        score += 1
        break
    attempts -= 1

def check_ans(qyestion, ans, attempts, score):
    if quiz[question]["B" or "1970s"].lower() == ans.lower():
        print(f"Correct. \n Your score is {score + 5000}!")
        return True
    else:
        print(f"Wrong answer! \n Your score is {score - 5000}.")
        return False
