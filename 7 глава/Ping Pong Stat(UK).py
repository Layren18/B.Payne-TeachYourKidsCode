# Вес и рост в шариках для пинг-понга (дюймы и фунты)
def convert_in_cm (inches):
    return inches * 2.54
def convert_lb_kg (pounds):
    return pounds / 2.2
h_in = int(input("Введите свой рост в дюймах: "))
w_lb = int(input("Введите свой вес в фунтах: "))
h_cm = convert_in_cm(h_in)
w_kg = convert_lb_kg(w_lb)

pp_tall = round(h_cm / 4)
pp_heavy = round(w_kg * 1000 / 2.7)

feet = h_in // 12
inch = h_in % 12

print("При росте", feet, "футов и", inch, "дюймах и весе", w_lb,
      "фунтов, ")
print("ваш рост", pp_tall, "шариков для пинг-понга, а ")
print("вес сопостовим с", pp_heavy, "шариков для пинг-понга!")