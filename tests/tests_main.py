from unittest import TestCase

from main import find_unique_names, find_three_popular_names, sort_course_by_duration, add_folder_yandex, check_folder_yandex

# Задание 1 Тесты на 3 любые задачи из темы "Коллекция данных"

class Test_HW_datacollection(TestCase):

    def setUp(self) -> None:
        self.mentors = [
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
        ]
        self.courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
        self.durations = [14, 20, 12, 20]

        return super().setUp()
    
    def test_find_unique_names(self):
        res = find_unique_names(self.mentors)
        expected = ['Адилет', 'Азамат', 'Александр', 'Алексей', 'Алена', 'Анатолий', 'Анна', 'Антон', 'Вадим', 'Валерий', 'Владимир', 'Денис', 'Дмитрий', 'Евгений', 'Елена', 'Иван', 'Илья', 'Кирилл', 'Константин', 'Максим', 'Михаил', 'Никита', 'Николай', 'Олег', 'Павел', 'Ринат', 'Роман', 'Сергей', 'Татьяна', 'Тимур', 'Филипп', 'Эдгар', 'Юрий']
        self.assertEqual(res, expected)

    def test_find_three_popular_names(self):
        res = find_three_popular_names(self.mentors)
        expected = ['Александр: 10 раз(а)', 'Евгений: 5 раз(а)', 'Максим: 4 раз(а)']
        self.assertEqual(res, expected)

    def test_sort_course_by_duration(self):
        res = sort_course_by_duration(self.courses, self.mentors, self.durations)
        expected = ['Python-разработчик с нуля - 12 месяцев', 'Java-разработчик с нуля - 14 месяцев', 'Fullstack-разработчик на Python - 20 месяцев', 'Frontend-разработчик с нуля - 20 месяцев']
        self.assertEqual(res, expected)

# Задание 2 
token = '' #требуется ввести токен
name_folder = 'HomeWorkTests'

class Test_yandex_disk (TestCase):
    def setUp(self) -> None:
        self.token = token
        self.folder = name_folder
        return super().setUp()
    
   
    def test_add_folder (self):
        res = add_folder_yandex(self.token, self.folder)
        expected = 201
        self.assertEqual(res, expected)

    def test_check_folder (self):
        res = check_folder_yandex(self.token, self.folder)
        expected = 200
        self.assertEqual(res, expected)

    def test_add_folder_if_exsists(self):
        res = add_folder_yandex(self.token, self.folder)
        self.assertEqual(res, 409)
        
