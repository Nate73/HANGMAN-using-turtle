# things left to do: making the fonts and the size 
# of the letters better say what the word was at the end
import turtle
import random
import time
turtle.penup()
turtle.goto(-100, 250)
turtle.pendown()
turtle.write("HANGMAN", font=("Times New Roman", 15, "normal"))
guess = 0
#input words and add them to a list
numberOfWords = turtle.textinput("", "How many words do you want to input?")
numberOfWordsint = int(numberOfWords)
words = []
for i in range(numberOfWordsint):
    inputtedWords = turtle.textinput("", "Input a word:")
    inputtedWords.lower()
    words.append(inputtedWords)
turtle.penup()
turtle.goto(-100, 220)
turtle.write("Letter that didn't work:", font=("Times New Roman", 15, "normal"))
turtle.penup()
turtle.goto(-100, 150)
turtle.write("The word:", font=("Times New Roman", 15, "normal"))
def drawing(x):
    if x == 1:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.forward(90)
        turtle.penup()
        turtle.goto(-100, 200)
        turtle.pendown()
    if x == 2:
        turtle.penup()
        turtle.goto(45, 0)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.penup()
        turtle.goto(-90, 200)
        turtle.pendown()
    if x == 3:
        turtle.penup()
        turtle.goto(45, 200)
        turtle.pendown()
        turtle.forward(90)
        turtle.penup()
        turtle.goto(-80, 200)
        turtle.pendown()
    if x == 4:
        turtle.penup()
        turtle.goto(135, 200)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.penup()
        turtle.goto(-70, 200)
        turtle.pendown()
    if x == 5:
        turtle.penup()
        turtle.goto(135, 175)
        turtle.pendown()
        turtle.right(180)
        turtle.circle(25)
        turtle.penup()
        turtle.goto(-60, 200)
        turtle.left(180)
        turtle.pendown()
    if x == 6:
        turtle.penup()
        turtle.goto(135, 125)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(60)
        turtle.penup()
        turtle.left(90)
        turtle.goto(-50, 200)
        turtle.pendown()
    if x == 7:
        turtle.penup()
        turtle.goto(135, 65)
        turtle.right(70)
        turtle.pendown()
        turtle.forward(50)
        turtle.left(70)
        turtle.penup()
        turtle.goto(-40, 200)
        turtle.pendown()
    if x == 8:
        turtle.penup()
        turtle.goto(135, 65)
        turtle.right(110)
        turtle.pendown()
        turtle.forward(50)
        turtle.left(110)
        turtle.penup()
        turtle.goto(-30, 200)
        turtle.pendown()
    if x == 9:
        turtle.penup()
        turtle.goto(105, 95)
        turtle.pendown()
        turtle.forward(60)
word = words[random.randint(0, len(words)-1)]
answer = ""
wordLength = len(word)
turtle.penup()
turtle.goto(-100, 130)

turtle.pendown()
while wordLength > 0:
    turtle.pencolor("white")
    turtle.forward(10)
    turtle.pencolor("black")
    turtle.forward(10)
    wordLength -= 1
for i in range(9):
    letterAnswer = turtle.textinput("", "Guess a letter:")
    if letterAnswer in word:
        letterInAnswer = word.find(letterAnswer)
        turtle.penup()
        turtle.goto((2*(letterInAnswer*10))-87.5, 130)
        turtle.pendown()
        turtle.write(letterAnswer)
    else:
        guess += 1
        drawing(guess)
        turtle.write(letterAnswer)
    if guess == 9:
        answer = turtle.textinput("", "Guess the word:")
        if answer == word:
            turtle.clear()
            turtle.penup()
            turtle.goto(0, 0)
            turtle.pendown()
            turtle.write("Well done you win!", font=("Times New Roman", 20, "normal"))
            time.sleep(5)
            break
        else:
            turtle.clear()
            turtle.penup()
            turtle.goto(0, 0)
            turtle.pendown()
            turtle.write("You Lost", font=("Times New Roman", 20, "normal"))
            time.sleep(5)
            break
    answer1 = turtle.textinput("", "Do you want to guess the word? y/n")
    if answer1 == "y":
        answer = turtle.textinput("", "Guess the word: ")
    if answer == word:
        turtle.clear()
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.write("Well done you win!", font=("Times New Roman", 20, "normal"))
        time.sleep(5)
        break