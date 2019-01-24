from phonebook import PhoneBook

phone_book_name = 'Fun'
phone_book_01 = PhoneBook(phone_book_name)
phone_book_01.add_contact('Igor', 'Tsallagov', '+79162208682', Telegram='@ionathz', Email='igor.tsallagov@gmail.com',
               Twitter='@chrismexx', Instagram='@chrismexx')


def add_contact(phone_book):
    name = str(input('Введите имя: '))
    surname = str(input('Введите фамилию: '))
    telephone = str(input('Введите телефон в формате +70001112233: '))
    phone_book.add_contact(name, surname, telephone)
    print('Контакт добавлен.')


def delete_contact(phone_book):
    number = str(input('Введите номер телефона в формате +70001112233: '))
    phone_book.delete_contact(number)
    print('Контакт удалён')


def print_phone_book(phone_book):
    return phone_book.print_list()


def print_favourites(phone_book):
    phone_book.print_favourites()


def search_by_name(phone_book):
    name = str(input('Введите имя или фамилию: '))
    phone_book.search_by_name(name)


def ask_commands():
    message = 'Доступные команды: a - добавить контакт, d - удалить контакт, p - ' \
              'показать все записи в телефонной книге, f - показать избранные контакты, s - искать контакты.'
    print(message)
    while True:
        command = input('Введите команду: ')
        if command == 'a':
            add_contact(phone_book_01)
            print()
        elif command == 'd':
            delete_contact(phone_book_01)
        elif command == 'p':
            print_phone_book(phone_book_01)
        elif command == 'f':
            print_favourites(phone_book_01)
        elif command == 's':
            search_by_name(phone_book_01)
        else:
            print('Команда введена неверно.')


if __name__ == '__main__':
    ask_commands()
