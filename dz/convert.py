import os
import user_answers
from start import lst_stop, lst_see, lst_add, lst_del
from user_answers import PersonalUser, rand_id
from user_answers import user

# try:
#     with open("datafiles/log.txt", "a", encoding="utf-8") as file:
#         data_message = user_answers.user
#         file.write(str(data_message) + "\n")
#         print("Данные успешно были записаны")
# except FileNotFoundError:
#     content = "<<< NOT FOUND: файл не найден >>>"
#     print(content)

try:
    with open("datafiles/log.txt", "a", encoding="utf-8") as file:
        data_message = user_answers.user
        file.write(str(data_message) + "\n")
        print("Данные успешно были записаны")
except FileNotFoundError:
    with open("datafiles/log.txt", "w", encoding="utf-8") as file:
        content = "<<< NOT FOUND: файл не найден, по этому создается новый файл... >>>"
        file.write(content)
        data_message = user_answers.user
        file.write(str(data_message) + "\n")
        print("Данные были записаны успешно")

while True:
    print("Что вы хотите сделать?")
    try:
        user_answer_action = str(input("(добавить/удалить/просмотреть/хватит): "))
    except ValueError:
        print("<<< LITERAL ERROR: ответ должен быть записан буквами >>>")

    if user_answer_action in lst_add:
        # Добовление новых данных
        user = user_answers.User()
        data_message = user.user_answerss()
        with open("datafiles/log.txt", "a", encoding="utf-8") as file:
            file.write(str(data_message) + "\n")
            print("Данные успешно были записаны")

    elif user_answer_action in lst_del:
        # Удаление имеющихся данных
        path = "datafiles/log.txt"
        if os.path.exists(path):
            os.remove(path)
            print("Данные успешно удалены")
        else:
            print("Файл не существует")

    elif user_answer_action in lst_see:
        # Просмотр имеющихся данных
        try:
            with open("datafiles/log.txt", "r", encoding="utf-8") as file:
                reader = file.read()
                print(reader)
        except FileNotFoundError:
            print("<<< NOT FOUND: файл не найден >>>")
    elif user_answer_action in lst_stop:
        break
    else:
        print("Некорректная команда, попробуйте еще раз")
