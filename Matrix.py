import collections
from tokenizer import *

class MatrixParser:
    '''
    <matrix>    ::= '[' <row> {';' <row>}+ ']'
    <row>       ::= '[' NB {',' NB}+ ']'
    '''
    def __init__(self):
        self.TOKENS_SPEC = [
        ('NB' , r'[+-]?[0-9]+\.?[0-9]*'),
        ('OPEN' , r'\['),
        ('CLOSE' , r'\]'),
        ('SEMI' , r'\;'),
        ('COMMA' , r'\,'),
        ('WS' , r'\s'),
        ('ERROR' , r'[^0-9\s\[\];]')]

    def parse(self, equa):
        self.token_generator = tokenize(equa, self.TOKENS_SPEC)
        self.current_token = None
        self.next_token = None
        self._next()
        print(self._matrix())
        if self.next_token:
            raise Exception('Wrong token sequence busted. Processing stopped at : ' + self.next_token.value)
        

    def _next(self):
        self.current_token, self.next_token = self.next_token, next(self.token_generator, None)

    def _accept(self, token_type):
        if self.next_token and self.next_token.type_ == token_type:
            self._next()
            return True
        else:
            return False

    def _expect(self, token_type):
        if not self._accept(token_type):
            raise Exception('Wrong token sequence busted. Expected : ' + token_type)

    def pt(self):
        print(self.current_token)

    def _matrix(self):
        '''
        <matrix>      ::= '[' <row> {';' <row>}+ ']'
        '''
        matrix = []
        self._expect('OPEN')
        matrix.append(self._row())
        while self._accept('SEMI'):
            matrix.append(self._row())
        self._expect('CLOSE')
        return matrix

    def _row(self):
        '''
        <row>       ::= '[' NB {',' NB}+ ']'
        '''
        row = []
        self._expect('OPEN')
        if self._accept('NB'):
            row.append(float(self.current_token.value))
            while self._accept('COMMA'):
                self._expect('NB')
                row.append(float(self.current_token.value))
        else:
            raise Exception('Expected a NB')
        self._expect('CLOSE')
        return row

def main():
    MP = MatrixParser()
    print('Enter a matrix : ', end='')
    equa = input().strip()
    MP.parse(equa)

if __name__ == "__main__":
    try:
	    main()
    except Exception as e:
        print('Error : ' + str(e))
