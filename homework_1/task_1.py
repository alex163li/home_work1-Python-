# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
#  является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно входит 
# в нужный диапазон

day= int(input('Введите цифру,обозначающую день недели, от 1 до 7: '))
if (day >= 1 and day <= 5):
    print('Это будний день!')
elif ((day == 6) or (day == 7)):
    print('Ура!!! Сегодня выходной день!')    
else:
    print('Такого дня недели не существует!')