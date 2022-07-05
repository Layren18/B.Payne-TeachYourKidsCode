# Яцзы (покер на костях) сортированный
import random
print("Давайте съиграем в игру Яцзы (покер на костях)?")
print("Правила просты: нужно всего лишь бросить 5 костей, "
      "больше совпадений - больше баллов!")
input("Нажмите на [Enter], чтобы продолжить: ")
keep_go = True
while keep_go:
    dice = [0,0,0,0,0]
    for x in range(5):
        dice[x] = random.randint(1,6)
    dice.sort()
    print("Вам выпало:", dice)
    if dice[0] == dice[4]:
        print("Янцзы! Все 5 костей одинаковые!")
    elif (dice[0] == dice[3]) or (dice[1] == dice[4]):
        print("Выпали 4 одинаковые кости!")
    elif (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
        print("Выпали 3 одинаковые кости!")
    elif (dice[0] == dice[1]) or (dice[1] == dice[2]) or (dice[2] == dice[3]) or (dice[3] == dice[4]):
        print("Выпали 2 одинаковые кости!")
    else:
        print("Совпадений не найдено!")
    keep_go = (input("Нажмите [Enter] для продолжения или "
                        "нажмите на любую клавишу, чтобы выйти: ") == "")