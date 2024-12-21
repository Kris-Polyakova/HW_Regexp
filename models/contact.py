class Contact:
    def __init__(self, lastname, firstname, patronymic='', phone=''):
        self.lastname = lastname 
        self.firstname = firstname 
        self.patronymic = patronymic 
        self.phone = phone
        
    def __str__(self):
        return (f'{self.lastname}, {self.firstname}' 
        f', {self.patronymic}, {self.phone}')

    def get_fullname(self):
        return f'{self.lastname} {self.firstname} {self.patronymic}'
    
    def get_phone(self):
        return self.phone
    
    def add_phone(self, new_phone=str):
        if self.phone == '':
            self.phone = new_phone
        else:
            self.phone += f' {new_phone}'
    
    def __eq__(self, other):
        return self.get_fullname() == other.get_fullname()
