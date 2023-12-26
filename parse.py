import sys
from lex import *

class Parser:
    def __init__(self, lexer: Lexer, emitter):
        self.lexer = lexer
        self.emitter = emitter
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()
        self.indent = 0
    
    def checkToken(self, kind):
        return kind == self.curToken.kind

    def checkPeek(self, kind):
        return self.peekToken.kind
    
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Excpected " + kind.name + ", got " + self.curToken.kind.name)
        self.nextToken
    
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
    
    def abort(self, message):
        sys.exit("Error. " + message)

    def program(self):
        print("Program")

        self.emitter.headerLine("from goto import with_goto")
        self.emitter.headerLine("@with_goto")
        self.emitter.headerLine("def main():")

        self.indent += 1

        while not self.checkToken(tokenType.EOF):
            self.statement()
        
        self.emitter.emitLine("main()", 0)
        self.emitter.writeFile()

    def statement(self):
        if self.checkToken(tokenType.SKRIV):
            print("Statement-print")
            self.emitter.emit("print(", self.indent)
            self.nextToken()

            if self.checkToken(tokenType.STRING):
                self.emitter.emit('"'+self.curToken.text+'"', 0)
                self.nextToken()
            else:
                self.expression()
            self.emitter.emitLine(")",0)
            
        elif self.checkToken(tokenType.OM):
            print("Statement-if")
            self.emitter.emit("if ", self.indent)
            self.nextToken()
            self.comparison()
            self.match(tokenType.DÅ)
            self.nextToken()
            self.nl()
            self.emitter.emitLine(":",0)
            self.indent += 1
            while not self.checkToken(tokenType.KLAR):
                self.statement()
            self.indent -= 1
            self.nextToken()
        
        elif self.checkToken(tokenType.MEDANS):
            print("Statement-while")
            self.emitter.emit("while ", self.indent)
            self.nextToken()
            self.comparison()
            self.match(tokenType.REPETERA)
            self.nextToken()
            self.nl()
            self.emitter.emitLine(":",0)
            self.indent += 1
            while not self.checkToken(tokenType.KLAR):
                self.statement()
            self.indent -= 1
            self.nextToken()

        elif self.checkToken(tokenType.SEKTION):
            print("Statement-label")
            self.nextToken()
            self.match(tokenType.IDENT)
            self.emitter.emitLine("label ."+self.curToken.text, self.indent)
            self.nextToken()

        elif self.checkToken(tokenType.KÖR):
            print("Statement-goto")
            self.nextToken()
            self.match(tokenType.IDENT)
            self.emitter.emitLine("goto ."+self.curToken.text, self.indent)
            self.nextToken()

        elif self.checkToken(tokenType.IDENT):
            print("Statement-let")
            self.emitter.emit(self.curToken.text+"=", self.indent)
            self.nextToken()
            self.match(tokenType.EQ)
            self.nextToken()
            self.expression()
            self.emitter.emitLine("",0)
        
        elif self.checkToken(tokenType.HÄMTA):
            print("Statement-input")
            
            self.nextToken()
            self.match(tokenType.IDENT)
            self.emitter.emitLine(self.curToken.text+"= float(input())", self.indent)
            self.nextToken()

        self.nl()

    def comparison(self):
        self.expression()
        if self.checkToken(tokenType.GT):
            print("Comparison-GT")
            self.emitter.emit(">", 0)
            self.nextToken()
        elif self.checkToken(tokenType.EQEQ):
            print("Comparison-EQEQ")
            self.emitter.emit("==", 0)
            self.nextToken()
        elif self.checkToken(tokenType.NOTEQ):
            self.emitter.emit("!=", 0)
            print("Comparison-NOTEQ")
            self.nextToken()
        elif self.checkToken(tokenType.GTEQ):
            self.emitter.emit(">=", 0)
            print("Comparison-GTEQ")
            self.nextToken()
        elif self.checkToken(tokenType.LT):
            self.emitter.emit("<", 0)
            print("Comparison-LT")
            self.nextToken()
        elif self.checkToken(tokenType.LTEQ):
            self.emitter.emit("<=", 0)
            print("Comparison-LTEQ")
            self.nextToken()
        else:
            self.abort("Excpected comparison, got: ", self.curToken.text)
        self.expression()

    def expression(self):
        self.term()
        def checkExpression():
            if self.checkToken(tokenType.PLUS):
                print("Expression-PLUS")
                self.emitter.emit("+",0)
                self.nextToken()
            elif self.checkToken(tokenType.MINUS):
                self.emitter.emit("-",0)
                print("Expression-MINUS")
                self.nextToken()
            else:
                return False
            self.term()
            return True
        while checkExpression():
            pass
    
    def term(self):
        self.unary()
        def checkTerm():
            if self.checkToken(tokenType.ASTERISK):
                print("TERM-ASTERISK")
                self.emitter.emit("*",0)
                self.nextToken()
            elif self.checkToken(tokenType.SLASH):
                self.emitter.emit("/",0)
                print("TERM-SLASH")
                self.nextToken()
            else:
                return False
            self.unary()
            return True
        while checkTerm():
            pass

    def unary(self):
        print("unary")
        neg = False
        if self.checkToken(tokenType.MINUS):
            print("negative")
            self.emitter.emit("(-",0)
            neg = True
            self.nextToken()
        self.primary()
        if neg:
            self.emitter.emit(")",0)

    def primary(self):
        print("Primary ("+ self.curToken.text +")")

        if self.checkToken(tokenType.NUMBER):
            self.emitter.emit(" "+self.curToken.text+" ",0)
            self.nextToken()
        elif self.checkToken(tokenType.IDENT):
            self.emitter.emit(" "+self.curToken.text+" ",0)
            self.nextToken()
        else:
            self.abort("Excpected variable or number, got: "+self.curToken.kind.name)

    def nl(self):
        print("Newline")

        self.match(tokenType.NEWLINE)

        while self.checkToken(tokenType.NEWLINE):
            self.nextToken()