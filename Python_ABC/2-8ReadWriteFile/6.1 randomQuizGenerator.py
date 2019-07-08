# Creates quizzes with questions and answers in random order, along with the answer key.

from pathlib import Path
import random
import provinceCapital

# assign location and make directory for exam paper
quizFolder = Path('./quizFolder')
quizFolder.mkdir(mode=0o777, parents=True, exist_ok=True)

# Get paper number
paperNum = int(input("\n您要出几份考卷？  "))

# Generate paperNum quiz files and answer key files
for quizNum in range(paperNum):

	# Create the quiz and answer key files
	quizFilePath = quizFolder.joinpath('quiz{}.txt'.format(quizNum + 1))
	quizFile = quizFilePath.open(mode='w', encoding='utf-8')
	answerKeyFilePath = quizFolder.joinpath('quiz_answers{}.txt'.format(quizNum + 1))
	answerKeyFile = answerKeyFilePath.open(mode='w', encoding='utf-8')

	# Write out the header for the quiz.
	quizFile.write('姓名：\n\n学号：\n\n班级：\n\n')
	quizFile.write(' '*20 + '考 卷 {}'.format(quizNum + 1))
	quizFile.write('\n\n')

	# Shuffle the order of the provinces
	provinces = list(provinceCapital.capitals.keys())
	random.shuffle(provinces)

	# loop through all provinces, making a question for each.
	for questionNum in range(len(provinces)):

		# Get right answers.
		correctAnswer = provinceCapital.capitals[provinces[questionNum]]

		# Get wrong answer pool: all answers then exclude the correct answer
		wrongAnswers = list(provinceCapital.capitals.values())
		wrongAnswers.remove(correctAnswer)

		# random take 3 from wrong answer pool and combine the right one to make 4 answer options
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)

		# Write the question and the answer options to the quiz file.
		quizFile.write('{}、 {}的省会是?\n'.format(questionNum+1, provinces[questionNum]))

		for i in range(4):
			quizFile.write('{}.  {}\n'.format('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')
		# Write the answer key to a file.
		answerKeyFile.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

	quizFile.close()
	answerKeyFile.close()

