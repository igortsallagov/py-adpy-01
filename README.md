# Домашнее задание к лекции 1.1 «Function 2.0 *args, \**kwargs»

1. Разработать свою реализацию функции print - adv_print. Она ничем не должна отличаться от классической функции кроме трех новых необязательных аргументов:
- start - с чего начинается вывод. По умолчанию пустая строка;
- max_line - максимальная длин строки при выводе. Если строка превыщает max_line, то вывод автоматически переносится на новую строку;
- in_file - аргумент, определяющий будет ли записан вывод ещё и в файл.

2. Создать приложение телефонная книга.
класс Contact имеет следующие поля:
- Имя, фамилия, телефонный номер - обязательные поля;
- избранный контакт - необязательное поле. По умолчанию False;
- Дополнительная информация(email, список дополнительных номеров, ссылки на соцсети) - необходимо использовать *args, \**kwargs.

Переопределить "магический" метод __str__ для красивого вывода контакта.
Вывод контакта должен быть следующим
```
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(jhon)
```
Вывод 
```
Имя: Jhon
Фамилия: Smith
Телефон: +71234567809
В избранных: нет
Дополнительная информация:
	 telegram : @jhony
	 email : jhony@smith.com
```

класс PhoneBook:
- Название телефоной книги - обязательное поле.

Методы:
- Вывод контактов из телефонной книги;
- Добавление нового контакта;
- Удаление контакта по номеру телефона;

3. Добавить два метода для поиска контактов в телефонной книге
- Поиск всех избранных номеров
- Поиск контакта по имени и фамилии
