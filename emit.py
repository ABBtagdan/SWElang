class Emitter:
    def __init__(self, fullPath):
        self.fullPath = fullPath
        self.code = ''
        self.header = ""
    
    def emit(self, code, indent):
        self.code += " "*indent + code

    def emitLine(self, code, indent):
        self.code += " "*indent+ code + "\n"

    def headerLine(self, code):
        self.header += code + '\n'

    def writeFile(self):
        with open(self.fullPath, "w", encoding="utf-8") as f:
            f.write(self.header + self.code)

    