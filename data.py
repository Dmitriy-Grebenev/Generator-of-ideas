"""
1) Основной смысл.
Бот, программа, распознавание нейросетью, генератор и т.д.
Логично после некоторых слов поставить слово "для", "который",
 а для некоторых опустить. То есть "программа для + распознавания + картинок",
 но "генератор картинок".
2) Действие. Распознавание, генерация, дешифрация и т.д.
3) Объект. Картинка, музыка, карта и т. д.
4) Для чего/кого.
Для хакатона, для решения экологической проблемы лесов и т.д.
"""

main_meaning = ['Русификатор ',
                'Генератор ',
                'Программа для ',
                'Бот для ',
                'Нейросеть для ',
                'Проект для ',
                'Приложение для ',
                'Софт для ',
                'Сервис для ',
                'Браузер для ',
                'Программное обеспечение для ',
                'Утилита для ',
                'Пакет для ',
                'Платформа для ']

action = ['распознавания ',
          'генерации ',
          'дешифрации ',
          'идентификации ',
          'расшифровки ',
          'диагностики ',
          'определения ',
          'аутентификации ',
          'исследования ',
          'анализа ',
          'разработки ',
          'разбора ',
          'прогнозирования ',
          'декодирования ',
          'обучения ',
          'поиска ',
          'кодирования ',
          'обучения ',
          'тестирования ',
          'формирования ']

for_whom = ['моделей ',
            'рисунков ',
            'чертежей ',
            'конспектов ',
            'машин ',
            'лекций ',
            'продуктов ',
            'музыки ',
            'роботов ',
            'концептов ',
            'телефонов ',
            'тренажеров ',
            'ресторанов ',
            'магазинов ',
            'картинок ',
            'идей ',
            'ноутбуков ',
            'хакатонов ',
            'леса ',
            'природы ',
            'проектов ',
            'приложений ',
            'концертов ',
            'самолётов ',
            'центра ',
            'изображений ',
            'фильмов ',
            'аниме ',
            'концептов ',
            'картин ',
            'семинаров ',
            'товаров ',
            'мыслей ',
            'выходных ',
            'супермаркетов ',
            'товаров ',
            'трейдинга ',
            'инвестиций ',
            'соцсетей ',
            'светофоров ',
            'дизайна ',
            'настольных игр ',
            'виртуальной реальности ',
            'казино ',
            'букмекеров ',
            'формул ',
            'стратегий ',
            'персонажей в играх ',
            'каршеринга ']

for_what = ['для собак',
            'для бабушек',
            'для инвалидов',
            'для телефонов',
            'для друзей',
            'для родителей',
            'для учителя',
            'для ноутбука',
            'для компьютера',
            'для праздника',
            'для дня рождения',
            'для мамы',
            'для хакатона',
            'для решения экологической проблемы лесов',
            'для поднятия настроения',
            'для хорошего вечера',
            'для развития мышления',
            'для странных идей',
            'для правильной мысли',
            'для отдыха на выходных',
            'для покупки новой куртки',
            'для розыгрыша над другом',
            'для развития инфраструктуры',
            'для хорошего вечера',
            'для студента перед экзаменом',
            'для водителя перед красным светом',
            'для нахождения лучшего музея в городе']
