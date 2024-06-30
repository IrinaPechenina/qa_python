

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
# class TestBooksCollector:
#
#     # пример теста:
#     # обязательно указывать префикс test_
#     # дальше идет название метода, который тестируем add_new_book_
#     # затем, что тестируем add_two_books - добавление двух книг
#     def test_add_new_book_add_two_books(self):
#         # создаем экземпляр (объект) класса BooksCollector
#         collector = BooksCollector()
#
#         # добавляем две книги
#         collector.add_new_book('Гордость и предубеждение и зомби')
#         collector.add_new_book('Что делать, если ваш кот хочет вас убить')
#
#         # проверяем, что добавилось именно две
#         # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
#         assert len(collector.get_books_rating()) == 2
#
#     # напиши свои тесты ниже

import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books_success(self):
        collector = BooksCollector()  # создали экземпляр(объект) класса
        # добавили две книги
        collector.add_new_book('Чемодан')
        collector.add_new_book('Иностранка')
        assert len(collector.get_books_genre()) == 2  # проверили что в словаре 2 записи

    def test_add_new_book_add_one_book_twice_only_one_added(self):
        collector = BooksCollector()  # создали экземпляр(объект) класса
        # добавили одну книгу дважды
        collector.add_new_book('Чемодан')
        collector.add_new_book('Чемодан')
        assert len(collector.get_books_genre()) == 1  # проверили что в словаре 1 запись

    def test_add_new_book_add_book_more_then_40_symbols_not_added(self):
        collector = BooksCollector()  # создали экземпляр(объект) класса
        # добавили книгу название > 40 букв
        collector.add_new_book('Жизнь, необыкновенные и удивительные приключения Робинзона Крузо, моряка из Йорка, '
                               'прожившего двадцать восемь лет в полном одиночестве на необитаемом острове у берегов '
                               'Америки близ устьев реки Ориноко, куда он был выброшен кораблекрушением, '
                               'во время которого весь экипаж корабля, кроме него, погиб, с изложением его '
                               'неожиданного освобождения пиратами; написанные им самим')
        assert len(collector.get_books_genre()) == 0  # проверили что книга в словарь не добавилась

    @pytest.mark.parametrize('name,genre', [['Сияние', 'Ужасы'], ['Институт', 'Ужасы']])
    # в параметризации наименования книг и жанров
    def test_set_book_genre_set_genre_success(self, name, genre):
        collector = BooksCollector()  # создали экземпляр(объект) класса
        collector.add_new_book(name)  # добавили книгу в словарь books_genre
        collector.set_book_genre(name, genre)  # устанавливаем жанр книге
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name,genre', [['Сияние', 'Ужасы'], ['Незнайка на Луне', 'Мультфильмы']])
    def test_get_book_genre_receive_genre_success(self, name, genre):
        collector = BooksCollector()  # создали экземпляр(объект) класса
        collector.add_new_book(name)  # добавили книгу в словарь books_genre
        collector.set_book_genre(name, genre)  # устанавливаем жанр книге
        assert collector.books_genre.get(name)  # получаем жанр книги по её названию

    @pytest.mark.parametrize('name,genre', [['Сияние', 'Ужасы'], ['Незнайка на Луне', 'Мультфильмы']])
    def test_get_books_with_specific_genre_success(self, name, genre):
        collector = BooksCollector()  # создали экземпляр(объект) класса
        collector.add_new_book(name)  # добавили книгу в словарь books_genre
        collector.set_book_genre(name, genre)  # устанавливаем жанр книге
        assert collector.get_books_with_specific_genre(genre) == [name]  # получаем список книг с определенным жанром

    @ pytest.mark.parametrize('name,genre', [['Незнайка на Луне', 'Мультфильмы'], ['Буратино', 'Комедии'],
                                             ['Сто лет тому вперед', 'Фантастика']])
    def test_get_books_for_children_books_for_children_added_success(self, name, genre):
        collector = BooksCollector()  # создали экземпляр(объект) класса
        collector.add_new_book(name)  # добавили книгу в словарь books_genre
        collector.set_book_genre(name, genre)  # устанавливаем жанр книге
        assert collector.get_books_for_children() == [name]   # в списке книги с жанром, подходящим детям

    @pytest.mark.parametrize('name,genre', [['Сияние', 'Ужасы'], ['Десять негритят', 'Детективы']])
    def test_get_books_for_children_adults_books_not_added(self, name, genre):
        collector = BooksCollector()  # создали экземпляр(объект) класса
        collector.add_new_book(name)  # добавили книгу в словарь books_genre
        collector.set_book_genre(name, genre)  # устанавливаем жанр книге
        assert len(collector.get_books_for_children()) == 0  # в списке книг для детей 0 записей

    @pytest.mark.parametrize('name,genre', [['Сияние', 'Ужасы'], ['Незнайка на Луне', 'Мультфильмы'], ['Оно', 'Ужасы']])
    def test_get_books_genre_receive_dict_books_genre_success(self, name, genre):
        collector = BooksCollector()  # создали экземпляр(объект) класса
        collector.add_new_book(name)  # добавили книгу в словарь books_genre
        collector.set_book_genre(name, genre)  # устанавливаем жанр книге
        assert collector.get_books_genre()  # получаем словарь books_genre

    def test_add_book_in_favorites_one_book_added_success(self):
        collector = BooksCollector()  # создали экземпляр(объект) класса
        collector.add_new_book('Чемодан')  # добавили книгу в словарь books_genre
        collector.add_book_in_favorites('Чемодан')  # добавили книгу в избранные
        assert len(collector.get_list_of_favorites_books()) == 1  # проверили что в избранных 1 запись

    def test_delete_book_from_favorites_one_book_deleted_success(self):
        collector = BooksCollector()  # создали экземпляр(объект) класса
        collector.add_new_book('Чемодан')  # добавили книгу в словарь books_genre
        collector.add_book_in_favorites('Чемодан')  # добавили книгу в избранные
        collector.delete_book_from_favorites('Чемодан')  # удалили книгу из избранных
        assert len(collector.get_list_of_favorites_books()) == 0  # проверили что запись отсутствует

    @pytest.mark.parametrize('name', ['Незнайка на Луне', 'Иностранка'])
    def test_get_list_of_favorites_books_two_books_added_success(self, name):
        collector = BooksCollector()  # создали экземпляр(объект) класса
        collector.add_new_book(name)  # добавили книгу в словарь books_genre
        collector.add_book_in_favorites(name)  # добавили книгу в избранные
        assert collector.get_list_of_favorites_books() == [name]  # выводится список избранных книг
