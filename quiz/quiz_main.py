class QuizMain:
    def __init__(self,question_bk):
        self.question_no=0
        self.question_list=question_bk
        self.score=0

    def still_has_qn(self):
        return  self.question_no<len(self.question_list)   #return true if it is otherwise false

    def next_question(self):
         current_qn=self.question_list[self.question_no]
         self.question_no+=1
         answ=input(f'{self.question_no}:{current_qn.text}(true/false):')
         self.check_answer(answ,current_qn.answer)

    def check_answer(self,answwer,correct_answer):
        if answwer.lower()==correct_answer.lower():
            print('you got it right')
            self.score+=1
            print(f'your score is:{self.score}')
        else:
            print('you got it wrong')
        print(f'your score is:{self.score}/{self.question_no}')
        print(f'correct answer is:{correct_answer}')
        print('\n')



