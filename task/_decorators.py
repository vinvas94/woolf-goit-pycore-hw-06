from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid command😮 Please provide the name and phone number😊"
        except KeyError as e:
            return f"{e.args[0]}.😮 Please provide the name of an existing contact.😊"
        except IndexError:
            return "Invalid command😮 Please provide a valid contact name.😊"

    return inner