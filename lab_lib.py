from faker import Faker
import random

class Lab:
    def __init__(self):
        pass

    def _execute_public_methods(obj):
        methods = [getattr(obj, method) for method in dir(obj) if
                   callable(getattr(obj, method)) and not method.startswith('_')]
        for method in methods:
            print(method.__name__)
            method()
            print("____________________________________________________________")

    @staticmethod
    def _validate_input_for_digits(value):
        return not value.isdigit()

    def _get_value_from_stdin(self, value):
        pass

    def __call__(self, *args, **kwargs):
        self._execute_public_methods()

class Student:
    def __init__(self, *args):
        if not args:
            fake = Faker('uk_UA')
            self.gender = random.choice(["male", "female"])
            if self.gender == "male":
                self.name = str(fake.first_name_male())
                self.middle_name = str(fake.middle_name_male())
            else:
                self.name = str(fake.first_name_female())
                self.middle_name = str(fake.middle_name())
            self.surname = str(fake.last_name())
            self.age = random.randint(18,99)
            self.course = random.randint(1,6)
        else:
            pass


