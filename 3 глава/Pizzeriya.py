kolvo = eval(input("Сколько пицц вы хотите?"))
stoim = eval(input("Сколько стоит 1 пицца?"))
stoimv = kolvo * stoim
nalog = 0.1
nalogv = stoimv * nalog
vsego = stoimv + nalogv
print ("Стоимость вашего заказа с учётом налога:", vsego, "рублей")