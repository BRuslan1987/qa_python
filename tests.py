import pytest


from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
   

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_long_name(self):
        collector = BooksCollector()
        long_name = 'a' * 41
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_existing_book(self):
        collector = BooksCollector()
        book_name = 'Суперистория'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_genre(self):
        collector = BooksCollector()
        book_name = 'Книга1'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_book_genre(book_name) == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        book_name = 'Книга2'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фэнтези')
        assert collector.get_book_genre(book_name) == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга3')
        collector.add_new_book('Книга4')
        collector.set_book_genre('Книга3', 'Комедии')
        collector.set_book_genre('Книга4', 'Комедии')
        result = collector.get_books_with_specific_genre('Комедии')
        assert len(result) == 2
        assert 'Книга3' in result
        assert 'Книга4' in result

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Детский фильм')
        collector.set_book_genre('Детский фильм', 'Мультфильмы')
        assert 'Детский фильм' in collector.get_books_for_children()

    def test_get_books_for_children_with_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Книга для взрослых')
        collector.set_book_genre('Книга для взрослых', 'Ужасы')
        assert 'Книга для взрослых' not in collector.get_books_for_children()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = 'Любимая книга'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = 'Книга в избранном'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_add_nonexistent_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    @pytest.mark.parametrize("genre, expected_result", [
        ('Фантастика', True),
        ('Ужасы', True),
        ('Детективы', True),
        ('Мультфильмы', True),
        ('Комедии', True),
        ('Фэнтези', False),  # несуществующий жанр
        ('Романтика', False)  # несуществующий жанр
    ])
    def test_set_book_genre_various_genres(self, genre, expected_result):
        collector = BooksCollector()
        book_name = 'Тестовая книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        if expected_result:
            assert collector.get_book_genre(book_name) == genre
        else:
            assert collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize("book_name, expected_length", [
        ('Гордость и предубеждение и зомби', 1),
        ('Что делать, если ваш кот хочет вас убить', 1),
        ('Очень очень очень очень очень очень длинная книга', 0),  # слишком длинная
        ('', 0),  # пустое название
        ('Нормальная книга', 1)
    ])
    def test_add_new_book_various_names(self, book_name, expected_length):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == expected_length

    @pytest.mark.parametrize("genre, should_be_in_children", [
        ('Мультфильмы', True),
        ('Комедии', True),
        ('Ужасы', False),
        ('Детективы', False)
    ])
    def test_get_books_for_children_various_genres(self, genre, should_be_in_children):
        collector = BooksCollector()
        book_name = 'Тестовая книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        if should_be_in_children:
            assert book_name in collector.get_books_for_children()
        else:
            assert book_name not in collector.get_books_for_children()