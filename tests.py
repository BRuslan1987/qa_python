import pytest


from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()


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
   
    def test_get_books_genre_basic(self, collector):
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        books_genre = collector.get_books_genre()
        assert len(books_genre) == 2
        assert books_genre['Книга1'] == ''
        assert books_genre['Книга2'] == ''

    # Отдельный тест для get_book_genre
    def test_get_book_genre_single_book(self, collector):
        book_name = 'Тестовая книга'
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''

    # Тест добавления двух книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # Тест добавления книги с пустым именем
    def test_add_new_book_empty_name(self, collector):
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    # Тест добавления книги с длинным названием
    def test_add_new_book_long_name(self, collector):
        long_name = 'a' * 41
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    # Тест добавления существующей книги
    def test_add_existing_book(self, collector):
        book_name = 'Суперистория'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    # Тест фильтрации по жанру
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Книга3')
        collector.add_new_book('Книга4')
        collector.set_book_genre('Книга3', 'Комедии')
        collector.set_book_genre('Книга4', 'Комедии')
        result = collector.get_books_with_specific_genre('Комедии')
        assert len(result) == 2
        assert 'Книга3' in result
        assert 'Книга4' in result

    # Тесты для детских книг
    def test_get_books_for_children(self, collector):
        collector.add_new_book('Детский фильм')
        collector.set_book_genre('Детский фильм', 'Мультфильмы')
        assert 'Детский фильм' in collector.get_books_for_children()

    def test_get_books_for_children_with_age_rating(self, collector):
        collector.add_new_book('Книга для взрослых')
        collector.set_book_genre('Книга для взрослых', 'Ужасы')
        assert 'Книга для взрослых' not in collector.get_books_for_children()

    # Тесты избранного
    def test_add_book_in_favorites(self, collector):
        book_name = 'Любимая книга'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        book_name = 'Книга в избранном'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_add_nonexistent_book_to_favorites(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

        assert len(collector.get_list_of_favorites_books()) == 0

    # Параметризованный тест для проверки граничных значений длины названия книги
    @pytest.mark.parametrize("name, expected", [
        ('a' * 40, 1),    # допустимая длина (40 символов)
        ('a' * 41, 0),    # превышение длины
        ('Valid Name', 1) # нормальное название
    ])
    def test_add_books_with_different_name_lengths(self, collector, name, expected):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == expected

    # Тест для проверки установки жанра после добавления в избранное
    def test_set_genre_after_adding_to_favorites(self, collector):
        book_name = 'Новая книга'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_book_genre(book_name) == 'Фантастика'
        assert book_name in collector.get_list_of_favorites_books()

    # Тест для проверки удаления книги из избранного после удаления книги
    def test_remove_book_from_favorites_after_deletion(self, collector):
        book_name = 'Временная книга'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.books_genre.pop(book_name)  # предполагаем наличие метода удаления
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()




