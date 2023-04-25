from modules.view import View
from modules.fileChanging import FileChanging

class Controller():

    def start(self):
        # список доступных команд
        command = ["add", "edit", "del", "look", "exit"]
        # создание экземпляра класса ввода/вывода информации 
        view = View()
        view.commandMenu(command)
        
        self.checkCommandMenu(input(),command)


    # проверка правильности ввода команды 
    def checkCommandMenu(self, choice, commands):
        if choice in commands: self.checkCommands(choice) 
        else: 
            print("Введите команду заново:")
            self.checkCommandMenu(input(),commands)
            return


    # определение действий для введенной команды
    def checkCommands(self, command):
        file = FileChanging()
        # изменение заметок в файле
        match command:
            # добавление
            case "add":
                file.add()

            # изменение
            case "edit":
                file.edit()

            # удаление
            case "del":
                file.delete()

            case "look":
                file.look()

            case "exit":
                pass
