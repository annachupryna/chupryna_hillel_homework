class QuizGame:
    def __init__(self):
        self.questions = [
            {
                'question': "What is the first git command for creating a new project from the existing repository "
                            "before the new branch is created?",
                'answer': "git pull origin master",
                'topic': "git"
            },
            {
                'question': "What is the full command for passing your code to git repository if your branch name "
                            "is ‘test’?",
                'answer': "git push origin test",
                'topic': "git"
            },
            {
                'question': "What represents unchangeable list in Python?",
                'answer': "tuple",
                'topic': "data types"
            },
            {
                'question': "Command to add values to a set?",
                'answer': "update",
                'topic': "data types"
            },
            {
                'question': "What would you use to check if a condition is true - ‘=‘ or ‘==’?",
                'answer': "==",
                'topic': "operators"
            },
            {
                'question': "How would you print a string from 0 to 4 elements with a step of 2?",
                'answer': "[0:4:2]",
                'topic': "data types"
            },
            {
                'question': "What method will search for matches in a string from the end?",
                'answer': "rindex",
                'topic': "data types"
            },
            {
                'question': "What data type will the .isalpha() method return?",
                'answer': "boolean",
                'topic': "data types"
            },
            {
                'question': "What module lets you interact with your operating system via Python?",
                'answer': "os",
                'topic': "modules"
            },
            {
                'question': "What module lets you transform a file into bytes?",
                'answer': "pickle",
                'topic': "modules"
            }
        ]
        self.total_questions = len(self.questions)
        self.correct_answers = 0

    def display_question(self, question):
        print(question['question'])

    def get_user_answer(self):
        return input("Your answer: ")

    def check_answer(self, question, user_answer):
        if user_answer.lower() == question['answer'].lower():
            self.correct_answers += 1

    def play(self):
        for question in self.questions:
            self.display_question(question)
            user_answer = self.get_user_answer()
            self.check_answer(question, user_answer)
            print()

    def calculate_knowledge_level(self):
        percentage = (self.correct_answers / self.total_questions) * 100
        return percentage

    def analyze_incorrect_answers(self):
        incorrect_topics = []
        for question in self.questions:
            if question['answer'].lower() != self.get_user_answer().lower():
                incorrect_topics.append(question['topic'])
        return set(incorrect_topics)


game = QuizGame()
game.play()

knowledge_level = game.calculate_knowledge_level()
print(f"Your knowledge level is: {knowledge_level}%")

incorrect_topics = game.analyze_incorrect_answers()
if incorrect_topics:
    print("You answered incorrectly in the following topics:")
    for topic in incorrect_topics:
        print(topic)
else:
    print("Congratulations! You answered all questions correctly.")
        