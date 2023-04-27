from modules.view import View
from modules.fileChanging import FileChanging

class Controller():

    def start(self):
        # список доступных команд
        command = ["add", "edit", "del", "look", "ex"]
        # создание экземпляра класса ввода/вывода информации 
        view = View()
        view.firstStep()
        while(True):
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
        view = View()
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

            # просотр заметок
            case "look":
                match view.lookMenu():
                    case "id":
                        id = view.noteID()
                        file.lookId(id = id)
                    case "dt":
                        date = view.noteDate()
                        file.lookDate(date = date)
                    case "all":
                        file.look()
                

                
            
            # выход из программы
            case "ex":
                quit()
