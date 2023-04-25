class View():

    def commandMenu(self,command):
        print(f"Введите комманду({', '.join(str(x) for x in command)}):")
    
    
    def headNote(self):
        return input("Введите заголовок заметки:")
    
    def bodyNote(self):
        return input("Введите тело заметки:")
    

    def successWriteInFile(self):
        print("\033[32m {}".format("Success"))

    def errorWriteInFile(self):
        print("\033[31m {}".format("ERROR!"))

