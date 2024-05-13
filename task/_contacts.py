class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass


class Phone(Field):
    def __init__(self, value):
        if len(value)!=10 or not value.isdigit():
             raise TypeError ("Phone number must be a 10-digit number.")     
        super().__init__(value)   


class Record:
     def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
     def add_phone(self,phone):
        self.phones.append(Phone(phone))

     def remove_phone(self,phone):
        self.phones=[p for p in self.phones if str(p)!=phone ]

     def edit_phone(self,old_phone,new_phone):
        for idx,p in enumerate(self.phones):
             if str(p)==old_phone:
                  self.phones[idx]=Phone(new_phone)
     def find_phone(self,phone):
          return str(Phone(phone)in [str(p) for p in self.phones])

     def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
     

