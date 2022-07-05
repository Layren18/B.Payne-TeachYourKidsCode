# Пьяница v2
import random

s = ["пики","буби","черви","крести"]
n = ["двойка","тройка","четвёрка","пятёрка","шестёрка","семёрка","восьмёрка",
       "девятка","десятка","валет","дама","король","туз"]
input("Давайте съиграем в Пьяницу? Нажмите [Enter], чтобы продолжить")
keep_go = True
hands = 0
ties = 0
pc_score = 0
pl_score = 0
while keep_go and (hands < 26):
    hands += 1
    pc_s = random.choice(s)
    pl_s = random.choice(s)
    pc_n = random.choice(n)
    pl_n = random.choice(n)
    print("У компьютера",pc_n, "", pc_s)
    print("У Вас",pl_n, "", pl_s)
    if n.index(pc_n) > n.index(pl_n):
        print("Победил компьютер!")
        pc_score += 1 + ties
        ties = 0
    elif n.index(pc_n) < n.index(pl_n):
        print("Вы победили!")
        pl_score += 1 + ties
        ties = 0
    else:
        print("У нас ничья!")
        ties += 1
    print ("Счёт: Компьютер",pc_score, ", Вы",pl_score)
    answer = input("Нажмите [Enter], чтобы продолжить или "
                   "нажмите любую клавишу чтобы выйти: ")
    keep_go = (answer == "")
print("Игра окончена!")
if pc_score > pl_score:
    print ("Компьютер победил в игре!")
elif pl_score > pc_score:
    print ("Ты победил в игре!")
else:
    print ("Ничья в игре!")