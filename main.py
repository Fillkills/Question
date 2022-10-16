from Question import Question

firstname = input('Введите ваше имя')
surname = input('Введите вашу фамилию')
age = int(input('введите ваш возраст'))

if age <= 35:
    print(f'Привет, {firstname}!')
else:
    print(f'Здравствуйте, {firstname} {surname} !')

print('Готовы ли вы пройти тест на знание английского языка?')

question_prompts = [
    "1. ..... is the first mounts is summer in Russia.\n(a) July\n(b) June\n(c) May\n(d) September\n\n",
    "2. ..... you .... last summer at the seaside?\n(a) Did...spend\n(b) Do...spend\n(c) Did...spent\n(d) "
    "Do...spent\n\n",
    "3. Marry .... her school bug now.\n(a) is packing\n(b) packs\n(c) packed\n(d) pack\n\n",
    "4. There is cafe .... the cinema and the bank.\n(a) in front\n(b) to the left\n(c) between\n(d) in back\n\n",
    "5. There .... a museum and a theatre in this square last year.\n(a) where\n(b) was\n(c) is\n(d) in\n\n",
    "6. They left Paris .... Moscow two days ago.\n(a) to\n(b) in\n(c) for\n(d) on\n\n",
    "7. There aren't ... apples at home. Can you buy some?\n(a) any\n(b) some\n(c) much\n(d) many\n\n",
    "8. Is there .... cheese in the fridge?\n(a) some\n(b) any\n(c) many\n(d) more\n\n",
    "9. .... your Granny usually cook pancakes at the weekend.\n(a) Do\n(b) Does\n(c) Is\n(d) Did\n\n",
    "10. There is ... armchair to the right of the window.\n(a) a\n(b) the\n(c) an\n(d) on\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "c"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)