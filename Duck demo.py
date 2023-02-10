#Duck Typing
class VSCode:

    def execute(self):
        print("Compile")
        print("Run")

class MyEditor:
    def execute(self):
        print("Spell check")
        print("Convertion check")
        print("Compile")
        print("Run")

class Notepad:
    def show():
        print("Showing")

class laptop:
    def code(self, ide):
        print("Coding..")
        
        ide = VSCode()
        ide.execute()

lap1 = laptop()
lap1.code()
