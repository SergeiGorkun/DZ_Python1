
# # 1. Напишите программу которая будет на вход принимать цифру, обозначающую день недели, и проверяет, является ли этот день выходным
# N = int(input('Введите номер дня недели: '))
# if N > 7:
#         print('Ошибка, такого дня недели не существует')
# if N == 6 or N == 7:
#         print('Да! этот день недели является выходным')
# else:
#         print('Нет! этот день является будним')


# 2. напишите программу , которая будет принимать на вход координаты  точки (Х и Y), причем X =! 0 и Y =! 0 и выдает номер четверти плоскости, в которой находится эта точка ( или на какой оси она находится)
# X = int(input('Введите координаты X '))
# Y = int(input('Введите координаты Y '))

# if X != 0 and Y != 0:
#         if X > 0 and Y > 0:
#                 print('I четверть плоскости')
#         if X < 0 and Y > 0:
#                 print('II четверть плоскости')
#         if X < 0 and Y < 0:
#                 print('III четверть плоскости')
#         if X > 0 and Y < 0:
#             print('IV четверть плоскости')
        




# 3. напишите программу которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x  и y)
number = int(input('Введите номер четверти: '))
if number == 1:
    print('X > 0 и Y > 0')
if number == 2:
    print('X < 0 и Y > 0')
if number == 3:
    print('X < 0 и Y < 0')
if number == 4:
    print('X > 0 и Y < 0')
else: print('Нет такой четверти')



# 4. Напишите программу, которая на вход принимает координаты двух точек и находит расстояние между ними в 2D пространстве

# import math
# X1 = int(input('Введите значение координаты X для первой точки: '))
# Y1 = int(input('Введите значение координаты Y для первой точки: '))
# X2 = int(input('Введите значение координаты X для второй точки: '))
# Y2 = int(input('Введите значение координаты Y для второй точки: '))
# p1 = [X1, Y1]
# p2 = [X2, Y2]
# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
# print('Расстояние от точки A до точки B составляет: ')
# print(distance)