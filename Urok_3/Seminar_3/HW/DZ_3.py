# Задача 3.
# Насоревнованиипобиатлонуодинизтрехспортсменовстреляетипопадаетв
# мишень.Вероятностьпопаданиядляпервогоспортсменаравна0.9,длявторого
# —0.8,длятретьего—0.6.Найтивероятностьтого,чтовыстрелпроизведен:
# a).первымспортсменом
# б).вторымспортсменом
# в).третьимспортсменом

# Вероятности попадания для спортсменов
p1 = 0.9
p2 = 0.8
p3 = 0.6
# Вероятности того, что выстрел произведен каждым спортсменом
prob1 = p1 / (p1 + p2 + p3)
prob2 = p2 / (p1 + p2 + p3)
prob3 = p3 / (p1 + p2 + p3)
print(f"Вероятность того, что выстрел произведен первым спортсменом:{prob1:.5f}")
print(f"Вероятность того, что выстрел произведен вторым спортсменом:{prob2:.5f}")
print(f"Вероятность того, что выстрел произведен третьимспортсменом: {prob3:.5f}")