# Угадай число от 1 до 10
import random
the_number = random.randint(1, 10)
guess = int(input("Угадай число от 1 до 10: "))
while guess != the_number:
    if guess > the_number:
        print(guess, "Слишком большое число.")
    if guess < the_number:
        print(guess, "Слишком маленькое число.")
    guess = int(input("Попробуй снова!"))
print(guess, "Правильное число! Ты победил!")