# 1. Определите класс Book со следующими атрибутами: Название, Автор (полное имя), Цена.
# Определите конструктор, используемый для инициализации атрибутов метода значениями, 
# введенными пользователем.
# Задайте метод View() для отображения информации для текущей книги.
# Протестируйте.

class Book:
    def __init__(self, name_of_book, author, price):
        self.name_of_book = name_of_book
        self.author = author
        self.price = price
        
    def show_info_about_book(self):
        print('Name of book is: {0}\nAuthor is: {1} \nPrice is: {2}'.format(self.name_of_book, self.author, self.price)) 

name_of_book = input('Enter name of book: ')
author = input('Enter author of book: ')
price = int(input('Enter price: '))

printing_book_info = Book(name_of_book, author, price)
printing_book_info.show_info_about_book()

print('*' * 100)
# 2. Определите класс Playlist, его метод __init__() должен иметь два аргумента: self,
# song_list - список из классов Song.
# Класс Song с полями:
# - name - название песни,
# - lyric - слова песни.
# Внутри класса Playlist создайте метод sing_me_a_song(song_name), 
# который находит песню по её названию и выводит
# каждый элемент текста песни в отдельной строке. Обработайте возможные ошибки.

class Playlist:
    def __init__(self, songlist):
        self.songlist = songlist

    def sing_me_a_song(self, song_name):
        self.song_name = song_name
        for line in self.songlist:
            print(line)
        
class Song:
    def __init__(self, name, lyric):
        self.name = name
        self.lyric = lyric

songlist = Playlist('This is the end,Hold your breath and count to ten,Feel the Earth move and then'.split(','))

find_song_by_name = Song('Skyfall', songlist)
songlist.sing_me_a_song(find_song_by_name)

print('*' * 100)
# 3. Игра в кости для 2ух игроков, игроки по очереди бросают кости, 
# начинает первый игрок, пока он вводит в консоль слово: 
# mix - кости перемешиваются(максимум 5 раз, иначе автопоражения, 
# предупреждать об оставшемся количестве перемешиваний), 
# если вводит любое другое слово кости бросаются и показывается результат(он записывается), 
# потом очередь 2ого игрока.
# После этого тоже самое делает 2ой игрок и так 3 раза, 
# у кого по итогу этих 3-ёх раз будет большее число - тот победил.

from random import randint

first_player_chance = 3
first_player_sum = 0

second_player_chance = 3
second_player_sum = 0

while first_player_chance != 0: 
    first_player_chance -= 1
    player_input = input('Enter word "mix" to show first players number of dice: ')
    if player_input.lower() == 'mix':
        first_players_dice = randint(1, 5)
        print(f'Your dice number: {first_players_dice}, Your have {first_player_chance} more chance')
        first_player_sum += first_players_dice 

    else:
        print(f'Automatic loose. You have: {first_player_chance} more chance')

print('Second Player')   
while second_player_chance != 0: 
    second_player_chance -= 1
    player_input = input('Enter word "mix" to show second players number of dice: ')
    if player_input.lower() == 'mix':
        second_player_dice = randint(1, 5)
        print(f'Your dice number: {second_player_dice}, Your have {second_player_chance} more chance') 
        second_player_sum += second_player_dice

    else:
        print(f'Automatic loose. You have: {second_player_chance} more chance')

if first_player_sum > second_player_sum:
    print(f'First player is WINNER, total score: {first_player_sum}, second players score is: {second_player_sum}')
else:
    print(f'Second player is WINNER, total score: {second_player_sum}, first player score is: {first_player_sum}' )

print('*' * 100)
# 4. Функции для расчета стоимости вашей поездки:
# Определите функцию hotel_cost с одним аргументом nights в качестве входных данных. 
# Стоимость проживания в отеле составляет 140 долларов за ночь. 
# Таким образом, функция hotel_cost должна возвращать 140 * nights.

# Определите функцию plane_ride_cost, которая принимает на вход строку city. 
# Функция должна возвращать разные цены в зависимости от местоположения, 
# как в примере кода выше.

#  Ниже приведены допустимые пункты назначения и соответствующие им цены туда и обратно.
# "Шарлотт": 183
# "Тампа": 220
# "Питтсбург": 222
# "Лос-Анджелес": 475

# -Под существующим кодом определите функцию rental_car_cost с аргументом days. 
# Рассчитайте стоимость аренды автомобиля: Каждый день аренды автомобиля стоит $40.
# (cost=40*days) Если вы арендуете автомобиль на 7 или более дней, 
# вы получаете скидку $50(cost-=50).
# В качестве альтернативы (elif), 
# если вы арендуете автомобиль на 3 или более дней, вы получите скидку $20. 
# Вы не можете получить обе вышеуказанные скидки. Верните эту стоимость.
# -Затем определите функцию trip_cost, которая принимает два аргумента, город и дни.
#  Как и в примере выше, пусть ваша функция возвращает сумму вызовов 
# функций rental_car_cost(days), hotel_cost(days) и plane_ride_cost(city).
# Измените определение функции trip_cost. Добавьте третий аргумент, spending_money. 
# Измените то, что делает функция trip_cost. 
# Добавьте переменную `spending_money к возвращаемой ею сумме.


def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city == "Шарлотт":
        return 183
    elif city == "Тампа":
        return 220
    elif city == "Питтсбург":
        return 222
    elif city == "Лос-Анджелес":
        return 475
        
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    
    return cost
    
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    
    
print(trip_cost("Питтсбург", 9 , 2000))



    







