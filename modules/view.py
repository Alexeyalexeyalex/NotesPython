class View():

    # приветствие, вызывается при запуске программы
    def firstStep(self):
        print("""
                            Добро пожаловать в заметки
Вам доступны команды:

add - добавление заметки
edit - изменение заметки по индексу
del - удаление заметки по индексу
look - просмотр заметок
ex - выход из программы
        """)
    # вывод строки ввода команды
    def commandMenu(self,command):
        print("\033[0m {}".format(f"Введите комманду({', '.join(str(x) for x in command)}):"))
    
    # вывод строки ввода заголовка
    def headNote(self):
        return input("Введите заголовок заметки:\n")
    
    # вывод строки ввода тела заметки
    def bodyNote(self):
        return input("Введите тело заметки:\n")
    
    # вывод информации об успехе команды
    def successWriteInFile(self):
        print("\033[32m {}".format("Success"))

    # вывод информации об ошибке команды
    def errorWriteInFile(self):
        print("\033[31m {}".format("ERROR!"))

    # вывод строки ввода ID заметки
    def noteID(self):
        return input("Введите ID заметки:\n")

    def noteDate(self):
        return input("Введите дату заметки:\n")
    
    def lookMenu(self):
        return input("""
Введите команду для просмотра:\n
all - все заметки
id - заметка с определенным id 
dt - заметка с определенной датой (2023-04-26)
""")
