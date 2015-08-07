import sys
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'NAME','NUMBER','STRING','oldspeak','integer_variable','string_variable','un','report','if','then'
    )

literals = ['=','+','-','*','/', '(',')','>','<']

# Tokens

t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_if(t):
    r'if+'
    return t

def t_then(t):
    r'then+'
    return t

def t_report(t):
    r'report+'
    return t

def t_oldspeak(t):
    r'oldspeak+'
    return t

def t_integer_variable(t):
    r'integer_variable+'
    return t

def t_string_variable(t):
    r'string_variable+'
    return t

def t_un(t):
    r'un+'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value.strip('"')
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

precedence = (
    ('left','+','-'),
    ('left','*','/'),
    ('right','UMINUS'),
    )

# dictionary of names
names = { }

def p_statement_assign(p):
    '''statement : oldspeak integer_variable NAME "=" expression
                 | oldspeak string_variable NAME "=" STRING
                 | NAME "=" expression
                 | NAME "=" STRING'''
    if p[1] == 'oldspeak' : names[p[3]] = p[5]
    else : names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : report expression'
    print(p[2])

def p_expression(p):
    'statement : expression'

def p_expression_binp(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression '>' expression
                  | expression '<' expression
                  | '''
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]
    elif p[2] == '>': p[0] = p[1] > p[3]
    elif p[2] == '<': p[0] = p[1] < p[3]

def p_expression_uminus(p):
    '''expression : '-' expression %prec UMINUS
                | un expression %prec UMINUS'''
    try: 
        int(p[2])
        p[0] = -p[2]
    except ValueError:
        print(p[2] + ' is not an integer')

def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_expression_if(p):
    "expression : if expression then statement"
    if(p[2] == True):
        p[0] = p[3]
    else:
        print 'Fail'

def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('newspeak > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)