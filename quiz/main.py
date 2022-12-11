from  question_model import Question
from questions import question_data
from quiz_main import QuizMain
question_bk=[]
for question in question_data:
    qn=question["question"]
    an=question["correct_answer"]
    new_q=Question(qn,an)
    question_bk.append(new_q)


q=QuizMain(question_bk)


while q.still_has_qn():
    q.next_question()

print('quiz has ended')
print(f'your final score is:{q.score}/{q.question_no}')