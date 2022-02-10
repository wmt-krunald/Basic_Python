from locale import str
from questionfile import Question

question_prompts = [
    "\nWhat is color of apple?\n(a)Red/Green\n(b)Blur\n(c)Black\n\n",
    "\nWho is our PM?\n(a)Modi\n(b)Kalu\n(c)Pappu\n\n",
    "\nWhat is color of Banana?\n(a)Red\n(b)Black\n(c)Yellow\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]

def run_mcq(questions):
    score = 0
    for question in questions:
        ans = input(question.que)
        if ans == question.ans:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

run_mcq(questions)