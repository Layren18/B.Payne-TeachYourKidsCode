problem = input ('Введите математическую задачу или "Стоп", чтобы выйти: ')
while (problem!= "Стоп") :
    print("Ответ на ", problem, "- это", eval(problem))
    problem = input('Введите ещё одну задачу или "Стоп", чтобы выйти:')