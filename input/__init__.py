from ply import lex

# define token list
reserved_words = {
    'point': 'POINT',
    'linesegment': 'LINESEGMENT',
    'circle': 'CIRCLE',
    'rectangle': 'RECTANGLE',
    'square': 'SQUARE',
    'rhombus': 'RHOMBUS',
    'pentagon': 'PENTAGON',
    'hexagon': 'HEXAGON',
    'heptagon': 'HEPTAGON',
    'octagon': 'OCTAGON',
    'nonagon': 'NONAGON',
    'decagon': 'DECAGON',
    'semicurve': 'SEMICURVE',
    'curve': 'CURVE',
    'define': 'DEFINE'
}

tokens = ('NUMBER', 'STRING', 'GREATER', 'LESSER', 'LPAREN', 'RPAREN', 'COMMA') + tuple(reserved_words.values())


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'["]([^"\\\n]|\\.|\\\n)*["]'
    t.value = str(t.value)
    return t


t_GREATER = r'>'
t_LESSER = r'<'
t_LPAREN = r'('
t_RPAREN = r')'
t_COMMA = r','


t_ignore_SPACES = r'[ \t]+' # espacos brancos
t_ignore_COMMENT = r'\#.*'  # comentarios


# Error handling rule
def t_error(t):
    t.type = 'ERROR'
    t.value = t.value[0]
    t.lexer.skip(1)
    return t


# EOF handling rule
def t_eof(t):
    r''
    return None


lexer = lex.lex()