class Contact:

    def __init__(self, name, surname, telephone, *args, favourite=False, **kwargs):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.additional = args
        self.favourite = favourite
        if self.favourite is False:
            self.favourite_status = 'нет'
        else:
            self.favourite_status = 'да'
        self.printable = str(
            'Имя: ' + self.name + '\n' +
            'Фамилия: ' + self.surname + '\n' +
            'Телефон: ' + self.telephone + '\n' +
            'В избранных: ' + self.favourite_status + '\n'
        )
        if args:
            for additional_number in args:
                self.printable += str('Дополнительный номер: ' + additional_number + '\n')
        if kwargs:
            self.printable += str('Дополнительная информация: ' + '\n')
            for key in kwargs.keys():
                self.printable += str('\t\t' + key + ': ' + kwargs[key] + '\n')

    def __str__(self):
        return self.printable
