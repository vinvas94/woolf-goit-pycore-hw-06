from collections import UserDict


class AddressBook(UserDict):
    def add_record(self,record):
           self.data[str(record.name)]=record
          
    def find(self,name):
        return self.data.get(name)
    
    def delete(self,name):
        if name in self.data:
            del self.data[name]

