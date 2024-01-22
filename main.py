from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if len(self.value) == 10 and len(list(filter(lambda num: num.isnumeric(), self.value))) == 10:
            self.value = value
        else:
            raise ValueError
        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value):
        self.phones.append(Phone(value))
    
    def remove_phone(self, value):
        for elem in self.phones:
            if elem.value == value:
                self.phones.remove(elem)
    
    def edit_phone(self, old_phone, new_phone):
        if old_phone not in map(lambda phone: phone.value, self.phones):
            raise ValueError
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
                self.phones.append(Phone(new_phone))
    
    def find_phone(self, value):
        for elem in self.phones:
            if elem.value == value:
                return elem
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        for record in self.data:
            if name == record:
                return self.data[name]
    
    def delete(self, name):
        for record in self.data:
            if name == record:
                self.data.pop(record)
                break


