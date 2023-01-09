import csv
from datetime import datetime

print("Привет! Данная программа позволяет работать с .csv-файлами")
print("Для начала работы введите имя файла и путь к нему")
print("(стандартный файл в репозитории 'Roster.csv')")


def work_with_file(a: str):
    try:
        with open(a, encoding='utf-8') as file:
            print(f'Файл {a} успешно загружен!')
        file.close()
    except FileNotFoundError:
        print("Файл по указанному адресу не нейден\n"
              "Проверьте правильность имени и пути файла и повторите попытку")
        intro()
    else:
        print("Для просмотра файла введите '00'\n"
              "Для добавления строки введите '01'\n"
              "Для удаления строки введите '02'\n"
              "Для редактирования имеющейся строки введите '03'\n"
              "Для поиска по файлу введите '04'\n"
              "Для сохранения информации в отдельный файл введите '05'\n"
              "Для выхода введите 'exit'")
        while True:
            choose = str(input("Введите номер или наименование нужной опции\n"
                               "Для вызова подсказки введите 'help'\n"))
            if choose.upper() == 'EXIT':
                date = str(datetime.now())
                log_file_name = "Автосохранение " + str(a) + " " + date[:19] + ".txt"
                log_file = open(log_file_name, "w+")
                with open(a, encoding='utf-8') as file:
                    file_reader = csv.reader(file, delimiter=",")
                    for row in file_reader:
                        log_file.write("".join(row)+"\n")
                log_file.close()
                file.close()
                print("До свидания!")
                break
            elif choose.upper() == 'HELP':
                print("Для просмотра файла введите '00'\n"
                      "Для добавления строки введите '01'\n"
                      "Для удаления строки введите '02'\n"
                      "Для редактирования имеющейся строки введите '03'\n"
                      "Для поиска по файлу введите '04'\n"
                      "Для сохранения информации в отдельный файл введите '05'\n"
                      "Для выхода введите 'exit'")
            elif choose == '05':
                date = str(datetime.now())
                log_file_name = "Пользовательское сохранение " + str(a) + " " + date[:19] + ".txt"
                log_file = open(log_file_name, "w+")
                with open(a, encoding='utf-8') as file:
                    file_reader = csv.reader(file, delimiter=",")
                    for row in file_reader:
                        log_file.write("".join(row) + "\n")
                log_file.close()
                file.close()
                print("ГОТОВО!")
            elif choose == '04':
                data = []
                date = str(datetime.now())
                log_file_name = "Поиск в " + str(a) + " " + date[:19] + ".txt"
                log_file = open(log_file_name, "w+")
                while True:
                    print("Для поиска по всему файлу введите 'search'\n"
                          "Для выхода из режима поиска введите 'exit'\n")
                    set1 = str(input("Введите нужный параметр\n"))
                    if set1.upper() == "SEARCH":
                        data1 = []
                        with open(a, encoding="utf-8") as s_file:
                            file_reader = csv.reader(s_file, delimiter=",")
                            for row in file_reader:
                                data1.append("".join(row))
                        print("Доступные критерии поиска:")
                        print(data1[0])
                        s_file.close()
                        search_value = str(input("Введите данные для поиска\n"))
                        with open(a, encoding="utf-8") as r_file:
                            file_reader = csv.reader(r_file, delimiter=",")
                            next(file_reader)
                            log_file.write(f'Результаты поиска по параметру "{search_value}":' + "\n")
                            for row in file_reader:
                                for col in row:
                                    if search_value in col:
                                        data.append("".join(row))
                            data1 = set(data)
                            for i in data1:
                                log_file.write(i + "\n")
                            data = []
                            print("Данные поиска сохранены в файл", log_file_name)
                    elif set1.upper() == "EXIT":
                        log_file.close()
                        r_file.close()
                        print("ПОИСК ОКОНЧЕН!")
                        break
                    else:
                        print("Неверно заданы параметры поиска\n"
                              "Повторите попытку")
            elif choose == "03":
                while True:
                    print("Для редактирования файла введите 'edit'\n"
                          "Для выхода из режима редактирования введите 'exit'\n")
                    set1 = str(input("Введите нужный параметр\n"))
                    if set1.upper() == "EDIT":
                        data = []
                        with open(a, encoding="utf-8") as s_file:
                            file_reader = csv.reader(s_file, delimiter=",")
                            for index, row in enumerate(file_reader):
                                print(index, " ".join(row))
                                data.append(row)
                        s_file.close()
                        edit1 = int(input("Чтобы выбрать строку для редактирования введите ее номер:\n"))
                        print("Для редактирования выбрана строка:")
                        print(" ".join(data[edit1]))
                        new_string = list(input("Введите новые данные для выбранной "
                                                "строки через запятую без пробелов\n"
                                                "").split(","))
                        print("Строка после изменения данных:")
                        print(" ".join(new_string))
                        data[edit1] = new_string
                        with open(a, "w", encoding="utf-8") as s_file:
                            file_writer = csv.writer(s_file, quoting=csv.QUOTE_NONNUMERIC)
                            for row in data:
                                file_writer.writerow(row)
                        s_file.close()
                    elif set1.upper() == "EXIT":
                        print("РЕДАКТИРОВАНИЕ ЗАВЕРШЕНО!")
                        break
            elif choose == "02":
                while True:
                    print("Для удаления строки введите 'remove'\n"
                          "Для выхода из режима удаления строк введите 'exit'\n")
                    set1 = str(input("Введите нужный параметр\n"))
                    if set1.upper() == "REMOVE":
                        data = []
                        with open(a, encoding="utf-8") as s_file:
                            file_reader = csv.reader(s_file, delimiter=",")
                            for index, row in enumerate(file_reader):
                                print(index, " ".join(row))
                                data.append(row)
                        s_file.close()
                        edit1 = int(input("Чтобы выбрать строку для удаления введите ее номер:\n"))
                        print("Будет удалена выбрана строка:")
                        print(" ".join(data[edit1]))
                        data.remove(data[edit1])
                        with open(a, "w", encoding="utf-8") as s_file:
                            file_writer = csv.writer(s_file, quoting=csv.QUOTE_NONNUMERIC)
                            for row in data:
                                file_writer.writerow(row)
                        s_file.close()
                    elif set1.upper() == "EXIT":
                        print("УДАЛЕНИЕ ЗАВЕРШЕНО!")
                        break
            elif choose == "01":
                while True:
                    print("Для добавления строки введите 'add'\n"
                          "Для выхода из режима добавления строк введите 'exit'\n")
                    set1 = str(input("Введите нужный параметр\n"))
                    if set1.upper() == "ADD":
                        data = []
                        with open(a, encoding="utf-8") as s_file:
                            file_reader = csv.reader(s_file, delimiter=",")
                            for row in file_reader:
                                data.append(row)
                        s_file.close()
                        new_string = list(input("Введите данные для новой "
                                                "строки через запятую без пробелов\n"
                                                "").split(","))
                        print("Будет добавлена следующая строка:")
                        print(" ".join(new_string))
                        data.append(new_string)
                        with open(a, "w", encoding="utf-8") as s_file:
                            file_writer = csv.writer(s_file, quoting=csv.QUOTE_NONNUMERIC)
                            for row in data:
                                file_writer.writerow(row)
                        s_file.close()
                    elif set1.upper() == "EXIT":
                        print("ДОБАВЛЕНИЕ ЗАВЕРШЕНО!")
                        break
            elif choose == "00":
                with open(a, encoding="utf-8") as s_file:
                    file_reader = csv.reader(s_file, delimiter=",")
                    for row in file_reader:
                        print(" ".join(row))
                s_file.close()


def intro():
    while True:
        file = str(input("Для выхода введите 'exit'\n"))
        new_file = "".join(reversed(file))
        if file.upper() == "EXIT":
            print("До свидания!")
            break
        elif len(file) < 5 or new_file[:4] != "vsc.":
            print("Введен неверный формат файла, пожалуйста повторите ввод")
        else:
            print(f'Загружаю {file}..')
            work_with_file(file)
            break


intro()
