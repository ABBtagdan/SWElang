import enum
import sys

class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind

    def isKeyword(text):
        for kind in tokenType:
            if kind.name == text and kind.value >= 100 and kind.value < 200:
                return kind
        return None

class tokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    #Keywords
    SEKTION = 101
    KÖR = 102
    SKRIV = 103
    HÄMTA = 104
    OM = 106
    DÅ = 107
    MEDANS = 109
    REPETERA = 110
    #operators
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211
    KLAR = 212



class Lexer:
    def __init__(self, source):
        self.source = source + "\n"
        self.curChar = ''
        self.curPos = -1
        self.nextchar()

    def nextchar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = "\0"
        else:
            self.curChar = self.source[self.curPos]

    def peek(self):
        if self.curPos +1 >= len(self.source):
            return "\0"
        return self.source[self.curPos +1]
    
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextchar()

    def getToken(self):
        
        self.skipWhitespace()
        self.skipComment()
        
        token = None

        if self.curChar == "+":
            token = Token(self.curChar, tokenType.PLUS)

        elif self.curChar == "-":
            token = Token(self.curChar, tokenType.MINUS)

        elif self.curChar == "\\":
            token = Token(self.curChar, tokenType.KLAR)

        elif self.curChar == "*":
            token = Token(self.curChar, tokenType.ASTERISK)

        elif self.curChar == "/":
            token = Token(self.curChar, tokenType.SLASH)

        elif self.curChar == "\n":
            token = Token(self.curChar, tokenType.NEWLINE)

        elif self.curChar == "\0":
            token = Token('', tokenType.EOF)

        elif self.curChar == "=":
            if self.peek() == "=":
                self.nextchar()
                token = Token("==", tokenType.EQEQ)
            else:
                token = Token(self.curChar, tokenType.EQ)

        elif self.curChar == "!":
            if self.peek() == "=":
                self.nextchar()
                token = Token("!=", tokenType.NOTEQ)
            else:
                self.abort("Excpected '=' after '!'")

        elif self.curChar == '"':
            text = ""
            while self.peek() != '"':
                if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\t' or self.curChar == '\\' or self.curChar == '%':
                    self.abort("Illegal character in string")
                self.nextchar()
                text += self.curChar
            self.nextchar()
            token = Token(text, tokenType.STRING)

        elif self.curChar.isdigit():
            text = ""
            text += self.curChar
            while self.peek().isdigit():
                self.nextchar()
                text += self.curChar
            if self.peek() == ".":
                self.nextchar()
                if not self.peek().isdigit():
                    self.abort(f"Invalid character - '{self.peek()}' - in number")
                while self.peek().isdigit():
                    self.nextchar()
                    text += self.curChar
            token = Token(text, tokenType.NUMBER)

        elif self.curChar == ">":
            if self.peek() == "=":
                self.nextchar()
                token = Token(">=", tokenType.GTEQ)
            else:
                token = Token(self.curChar, tokenType.GT)

        elif self.curChar == "<":
            if self.peek() == "=":
                self.nextchar()
                token = Token("<=", tokenType.LTEQ)
            else:
                token = Token(self.curChar, tokenType.LT)

        elif self.curChar.isalpha():
            text = ""
            text += self.curChar
            while self.peek().isalnum():
                self.nextchar()
                text += self.curChar
            keyword = Token.isKeyword(text)
            if keyword == None:
                token = Token(text, tokenType.IDENT)
            else:
                token = Token(text, keyword)
            
        else:
            self.abort(f"Unknown token: '{self.curChar}'")

        self.nextchar()
        return token

    def abort(self, message):
        sys.exit("Lexing error. " + message)

    def skipComment(self):
        if self.curChar == '#':
            while self.curChar != '\n':
                self.nextchar()
