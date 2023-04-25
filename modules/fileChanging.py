import json, os.path, datetime
from modules.view import View

class FileChanging():
    
    def writeInJson(self, data):
        with open('notes.json', 'w') as jsonFile:
            json.dump(data, jsonFile)

    def readJson(self):
        with open('notes.json') as jsonFile:
                data = json.load(jsonFile)
                return data
    

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
            if os.path.exists("notes.json") and os.path.isfile("notes.json"):
                data = self.readJson()
                id = len(data["notes"])+1
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

    def edit(self):
        pass

    def delete(self):
        pass

    def look(self):
        data = self.readJson()
        for x in data['notes']:
            print("\nНомер заметки: ", x["id"])
            print("Заголовок: ", x["заголовок"])
            print("Тело заметки: ", x["тело"])
            print("Дата создания: ", x["date"],"\n")