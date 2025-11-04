import random

def displayMenu():
    ''' A function that displays the difficulty level menu at the beginning of the quiz.'''
    while True:
     choice = input("Choose difficulty:\n1. Easy\n2. Moderate\n3. Advanced\nEnter 1/2/3: ").strip()
     if choice == '1' or choice.lower() == 'easy':
        return 'easy'
     if choice == '2' or choice.lower() == 'moderate':
        return 'moderate'
     if choice == '3' or choice.lower() == 'advanced':
        return 'advanced'
    print("Invalid selection — please enter 1, 2 or 3.")



def randomint(Level=None):
    '''A function that determines the values used in each question. The min and max values of the numbers should be based on the difficulty level chosen as described above.'''
    if Level is None:
        Level = displayMenu()

    lvl = Level.lower()
    if lvl == 'easy':
        a = random.randint(1, 9)
        b = random.randint(1, 9)
    elif lvl == 'moderate':
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    elif lvl == 'advanced':
        a = random.randint(1000, 9999)
        b = random.randint(1000, 9999)
    else:
        raise ValueError(f"Unknown difficulty: {Level}")
    return a, b


def decideoperation():
    ''' A function that randomly decides whether the problem is an addition or subtraction problem and returns a char.'''
    return random.choice(['+', '-'])

def displayProblem(level):
    '''A function that displays the question to the user and accepts their answer.'''
    a, b = randomint(level)
    op = decideoperation()
    if op == '-' and a < b:
        a, b = b, a
    correct_answer = a + b if op == '+' else a - b
    raw = input(f"Question: {a} {op} {b} = ")
    user_answer = int(raw.strip())
    is_correct = (user_answer == correct_answer)
    return is_correct, correct_answer

     

    
def isCorrect(level):
    '''A function that checks whether the users answer was correct and outputs an appropriate message'''
    correct, correct_answer = displayProblem(level)
    if correct:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer was {correct_answer}.")
    return correct

    

def displayResults(score, total):
    """Print final score (percentage) and a simple grade."""
    percent = round((score / total) * 100, 1) if total else 0
    if percent >= 90:
        grade = "A+"
    elif percent >= 80:
        grade = "A"
    elif percent >= 70:
        grade = "B"
    elif percent >= 60:
        grade = "C"
    elif percent >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"\nFinal score: {score}/{total} ({percent}%) — Grade: {grade}")

def main():
    level = displayMenu()
    num_questions = 10
    score = 0
    for i in range(1, num_questions + 1):
        print(f"\nQuestion {i}/{num_questions}")
        if isCorrect(level):
            score += 1
    displayResults(score, num_questions)

main()
    
