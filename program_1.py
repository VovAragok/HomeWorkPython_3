# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так
# :A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков;
# J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать,
# что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12

#
# A, E, I, O, U, L, N, S, T, R – 1 очко
# А, В, Е, И, Н, О, Р, С, Т – 1 очко
# D, G – 2 очка
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# Й, Ы – 4 очка;
# K – 5 очков;
# Ж, З, Х, Ц, Ч – 5 очков
# J, X – 8 очков;
# Ш, Э, Ю – 8 очков
# Q, Z – 10 очков.
# Ф, Щ, Ъ – 10 очков.
word = str(input("введите слово "))
point = 0
data_set = [
    {1: "A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т"},
    {2: "D, G, Д, К, Л, М, П, У"},
    {3: "Б, Г, Ё, Ь, Я, B, C, M, P"},
    {4: "F, H, V, W, Y, Й, Ы"},
    {5: "K, Ж, З, Х, Ц, Ч"},
    {8: "J, X, Ш, Э, Ю"},
    {10: "Q, Z, Ф, Щ, Ъ"}
]
for i in word.upper():
    for j in data_set:
        for k, v in j.items():
            if i in v.replace(" ", "").split(","):
                point += k
print(point)