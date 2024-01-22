import time
from random import randint
from start import start_message


class PersonalUser:
    def __init__(self):
        self.name = None

    def user_personal_answer(self, message):
        self.name = str(input("Как вас зовут: "))
        message = f"Привет {self.name}"
        return message

    def __str__(self):
        return self.name


personal_user = PersonalUser()
personal_user.user_personal_answer(message=None)

print(start_message)
time.sleep(1)
rand_id = randint(100, 999)
print(f"Привет {personal_user}#{rand_id}")


class User:
    def __init__(self):
        self.user_input_name = None
        self.user_input_firstname = None
        self.user_input_age = None
        self.user_input_phone = None
        self.user_input_email = None

    def user_answerss(self):
        try:
            self.user_input_name = str(input("Введите имя пользователя: "))
            self.user_input_firstname = str(input("Введите фамилию пользователя: "))
            self.user_input_age = int(input("Введите возраст пользователя: "))
            self.user_input_phone = int(input("Введите номер телефона пользователя: "))
            self.user_input_email = input("Введите почту пользователя: ")
        except ValueError:
            print("<<ОШИБКА>>\nВведены не корректные значения")
        return f"{self.user_input_name}, {self.user_input_firstname}, {self.user_input_age}, {self.user_input_phone}, {self.user_input_email}"

    def __str__(self):
        return self.user_input_name, self.user_input_firstname, self.user_input_age, self.user_input_phone, self.user_input_email


user = User().user_answerss()
# user.user_answerss()
