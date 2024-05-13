from _decorators import input_error
from _address_book import AddressBook
from _contacts import Record

@input_error
def add_contact(args, address_book:AddressBook):
    if len(args)!=2:
        raise ValueError 
    name, phone = args
    formatted_name = name.capitalize()
    record=Record(formatted_name)
    record.add_phone(phone)
    address_book.add_record(record)
    return "Contact added."

@input_error
def change_contact(args, address_book:AddressBook):
    if len(args)!=2:
        raise ValueError 
    name, new_phone = args
    record=address_book.find(name)
    if record:
        record.edit_phone(record.phones[0].value,new_phone)
        return f"Contact {name} updated"
    else:
        raise KeyError(f"{name} not found") 
    
@input_error
def show_phone(name,address_book:AddressBook):
    record = address_book.find(name)
    if record:
        return f"Phone number for {record.name}: {record.phones[0]}"
    else:
        raise KeyError(f"{name} not found") 

       
@input_error
def show_all(address_book:AddressBook):
    contacts=address_book.data
    if not contacts:
        return "No contacts saved."
    else:
        result = ""
        for name, record in contacts.items():
            result += f"{record.name}: {', '.join(map(str, record.phones))}\n"
        return result.strip()

@input_error    
def delete_contact(args, address_book: AddressBook):
    if len(args) != 1:
        raise ValueError ("Invalid command. Please provide the name of the contact to delete.")
    name=args[0]
    if name in address_book.data:
        del address_book.data[name]
        return f"Contact {name} delete."     
    else:
        raise KeyError(f"{name} not found")
