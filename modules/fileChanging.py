import json, os.path, datetime
from modules.view import View

class FileChanging():
    # запись в файл
    def writeInJson(self, data):
        with open('notes.json', 'w') as jsonFile:
            json.dump(data, jsonFile)
    # чтение файла
    def readJson(self):
        with open('notes.json') as jsonFile:
                data = json.load(jsonFile)
                return data
    
    # проверка наличия файла в системе
    def isFile(self):
        return os.path.exists("notes.json") and os.path.isfile("notes.json")
                
    # добавление заметки
    def add(self):
        view = View()
        try:
            # создание словаря с заметками
            data ={}
            data["notes"] = []
            # создание переменных с начальным значением
            head = view.headNote()
            bodyNote = view.bodyNote()
            id = 1
            date = str(datetime.datetime.now())
            
            # изменение переменных в случае существования файла
            if self.isFile() :
                data = self.readJson()
                if len(data['notes'])>0:
                    id = int(data['notes'][-1]["id"])+1
            # добавление заметок в словарь
            data["notes"].append({
                "id" : id,
                "заголовок" : head,
                "тело" : bodyNote,
                "date" : date
                })
            # запись в файл
            self.writeInJson(data)
            view.successWriteInFile()
        except:
            view.errorWriteInFile()

    # изменение заметки
    def edit(self):
        view = View()

        try:
            if self.isFile():
                data = self.readJson()
                while (True):
                    id = view.noteID()
                    edit = False
                    for x in data['notes']:
                        if x["id"] == int(id):
                            x["заголовок"] = view.headNote()
                            x["тело"] = view.bodyNote()
                            self.writeInJson(data)
                            edit = True
                    if edit:  
                        view.successWriteInFile()
                        return
            else:
                view.errorWriteInFile()
        except:
            view.errorWriteInFile()

    # удаление заметки
    def delete(self):
        view = View()

        # try:
        if self.isFile():
            data = self.readJson()
            while (True):
                id = view.noteID()
            
                delete = True
                for x in range(0, len(data['notes'])):
                    # сравнение id заметки с введенным id
                    if data['notes'][x]["id"] == int(id):
                        # удаление элемента из списка
                        del data['notes'][x]
                        x-=1
                        self.writeInJson(data)
                        delete = True
                if delete:  
                    view.successWriteInFile()
                    return

        else:
            view.errorWriteInFile()
        
        # except:
        #     view.errorWriteInFile()
    
    # просмотр заметок
    def look(self):
        if self.isFile():
            data = self.readJson()
            for x in data['notes']:
                print("\nНомер заметки: ", x["id"])
                print("Заголовок: ", x["заголовок"])
                print("Тело заметки: ", x["тело"])
                print("Дата создания: ", x["date"],"\n")
    
    def lookDate(self, date):
        view = View()

        try:
            if self.isFile():
                data = self.readJson()
                for x in data['notes']:
                        xDate = datetime.datetime.strptime(x["date"], '%Y-%m-%d %H:%M:%S.%f').date()
                        
                        if str(xDate) == date:
                            print("\nНомер заметки: ", x["id"])
                            print("Заголовок: ", x["заголовок"])
                            print("Тело заметки: ", x["тело"])
                            print("Дата создания: ", x["date"],"\n")
        except:
            view.errorWriteInFile()


    def lookId(self, id):
        view = View()

        try:
            if self.isFile():
                data = self.readJson()
                for x in data['notes']:
                        if x["id"] == int(id):
                            print("\nНомер заметки: ", x["id"])
                            print("Заголовок: ", x["заголовок"])
                            print("Тело заметки: ", x["тело"])
                            print("Дата создания: ", x["date"],"\n")
        except:
            view.errorWriteInFile()