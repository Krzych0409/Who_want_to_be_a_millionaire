import json
from random import shuffle, choice
from math import ceil
from pyinputplus import inputChoice


class Game:

    def __init__(self):
        # File with five levels of 15 questions
        self.file = open('questions_file.txt')
        self.dict = json.load(self.file)
        self.win_balance = 0
        self.tips = ['NEW', '50']
        self.the_end = 1 # If == 0  Game over

        # Randomizing questions from a given level
        for lvl in self.dict['games']:
            shuffle(lvl['questions'])


        self.name = input('What is your name: ')
        # Levels of win
        self.levels = {1 : 1000, 2 : 2000, 3 : 5000, 4 : 10_000, 5 : 25_000, 6 : 50_000, 7 : 100_000, 8 : 250_000, 9 : 500_00, 10 : 1_000_000}


    def shuffle_questions(self, turn):
        # Calculation of questions level
        self.lvl_q = ceil(turn / 2)
        # Draw three questions every second turn from a given level
        if turn % 2 != 0:
            self.nr_of_question = 0
            self.three_questions = []
            while(len(self.three_questions) < 3):
                self.q = choice(self.dict['games'][self.lvl_q-1]['questions'])
                if self.q not in self.three_questions:
                    self.three_questions.append(self.q)


    def asking_question(self, turn):
        print(self.three_questions[self.nr_of_question]['question'])
        print(f'A : {self.three_questions[self.nr_of_question]["content"][0]}')
        print(f'B : {self.three_questions[self.nr_of_question]["content"][1]}')
        print(f'C : {self.three_questions[self.nr_of_question]["content"][2]}')
        print(f'D : {self.three_questions[self.nr_of_question]["content"][3]}')
        self.answer_of_gamer = inputChoice(('A', 'B', 'C', 'D', 'pass', 'new', '50'), prompt='').upper()

        # If answer is correct
        if ((self.answer_of_gamer == 'A' and self.three_questions[self.nr_of_question]["correct"] == 0) or (self.answer_of_gamer == 'B' and self.three_questions[self.nr_of_question]["correct"] == 1) or
        (self.answer_of_gamer == 'C' and self.three_questions[self.nr_of_question]["correct"] == 2) or (self.answer_of_gamer == 'D' and self.three_questions[self.nr_of_question]["correct"] == 3)):
            self.win_balance = self.levels[turn]
            print(f'Correct answer - Your current win = {self.win_balance}$')
            self.nr_of_question += 1

        # If the player gives up - Game over
        elif self.answer_of_gamer == 'PASS':
            print(f'You win {self.win_balance}$')
            self.the_end = 0

        # Changing the question
        elif self.answer_of_gamer == 'NEW':
            if self.answer_of_gamer in self.tips:
                self.nr_of_question += 1
                self.tips.remove('NEW')
                game.asking_question(turn)
            else:
                print(f'You do not have this tip')
                game.asking_question(turn)

        # Deletion of two answers
        elif self.answer_of_gamer == '50':
            if self.answer_of_gamer in self.tips:
                self.tips.remove('50')
                # Loop until two incorrect answers are removed
                while self.three_questions[self.nr_of_question]["content"].count('') < 2:
                    self.random_index = choice(range(4))
                    if self.three_questions[self.nr_of_question]["correct"] != self.random_index:
                        self.three_questions[self.nr_of_question]["content"][self.random_index] = ''
            else: print(f'You do not have this tip')
            game.asking_question(turn)

        # If answer incorrect - Game over
        else:
            print(f'Answer incorrect - You lose {self.win_balance}$')
            self.the_end = 0


game = Game()

# Loop that executes 10 times
for turn in range(1, 11):
    game.shuffle_questions(turn)

    if turn == 1:
        print(f'\nHi {game.name}. You must correctly answer 10 questions from 5 levels to win 1.000.000 $')
        print(f"Available answers - 'A', 'B', 'C', 'D', 'pass', 'new', '50'\n")
    print(f'\nQuestion {turn} for {game.levels[turn]}$ :')

    game.asking_question(turn)

    # Game over
    if game.the_end == 0: break

