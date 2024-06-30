# qa_python


# Спринт 4
## Задача: покрыть тестами приложение **BooksCollector**

## Описание тестов
Метод **add_new_book**
1. test_add_new_book_add_two_books_success - проверили, что можно добавить книги с наименованием больше нуля, 
но меньше 40 символов. Успешно добавились две книги с разными названиями.
2. test_add_new_book_add_one_book_twice_only_one_added -  проверили, что книгу можно добавить только один раз - 
Дважды добавили книгу с одним и тем же названием, в словарь добавилась одна книга
3. test_add_new_book_add_book_more_then_40_symbols_not_added проверили, что нельзя добавить книгу с наименованием 
больше 40 символов. В словарь книга не добавилась
 
Метод **set_book_genre**
1. test_set_book_genre_set_genre_success - проверили, что книге присваивается жанр

Метод **get_book_genre**
1. test_get_book_genre_receive_genre_success - проверили, что можно получить жанр книги по её названию

Метод **get_books_with_specific_genre**
1. test_get_books_with_specific_genre_success - проверили, что можно вывести список книг с определенным жанром

Метод **get_books_for_children** 
1. test_get_books_for_children_books_for_children_added_success - проверили, что можно вывести список книг с жанром,
подходящем детям
2. test_get_books_for_children_adults_books_not_added -  проверили, что в список книг для детей не добавляются
книги жанров для взрослых

Метод **get_books_genre**
1. test_get_books_genre_receive_dict_books_genre_success - проверили, что можно получить словарь books_genre
 
Метод **add_book_in_favorites** 
1. test_add_book_in_favorites_one_book_added_success - проверили, что книга успешно добавляется в Избранное

Метод **delete_book_from_favorites** 
1. test_delete_book_from_favorites_one_book_deleted_success - проверили, что книга удаляется из Избранного

Метод **get_list_of_favorites_books**
1. test_get_list_of_favorites_books_two_books_added_success -проверили, что выводится список избранных книг 
