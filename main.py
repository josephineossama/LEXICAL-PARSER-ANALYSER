import re

import nltk

input_program = input("Enter Your Code: ");
input_program_tokens = nltk.wordpunct_tokenize(input_program);

print(input_program_tokens);


RE_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|inline|int|long|register|restrict|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|Alignas|Alignof|Atomic|Alignof|Atomic|bool|Complex|Generic|Imaginary|noreturn|static_assert|thread_local|fun|string|class|struc|include"
RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
RE_Numerals = "^(\d+)$"
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_Headers = "([a-zA-Z]+\.[h])"

datatype = []
tokens = []

# To Categorize The Tokens

for token in input_program_tokens:
    if re.findall(RE_Keywords, token):
        print(token, "-------> Keyword")
        datatype.append('keyword')
        tokens.append(token)
    elif re.findall(RE_Operators, token):
        print(token, "-------> Operator")
        datatype.append('operator')
        tokens.append(token)
    elif re.findall(RE_Numerals, token):
        print(token, "-------> Numeral")
        datatype.append('numeral')
        tokens.append(token)
    elif re.findall(RE_Special_Characters, token):
        print(token, "-------> Special Character/Symbol")
        datatype.append('special character/symbol')
        tokens.append(token)
    elif re.findall(RE_Identifiers, token):
        print(token, "-------> Identifiers")
        datatype.append('identifier')
        tokens.append(token)
    else:
        print("Unknown Value")


def jump_statement(tokens, datatype):
    for i, j in enumerate(tokens):
        if j == 'continue' or j == 'break':
            if tokens[i + 1] == ';':
                print('syntax is correct')
            else:
                print('syntax is not correct! KEYWORD SHOULD BE FOLLOWED BY ";"')
        if j == 'return':
            if datatype[i + 1] == 'numeral' or datatype[i + 1] == 'identifier':
                if tokens[i + 2] == ';':
                    print('syntax is correct')
                else:
                    print('syntax is not correct!it should be followed by  ";"')
            else:
                print('syntax is not correct ! it should be followed by " identifier OR VALUE "')
        if j == 'goto':
            if datatype[i + 1] == 'identifier':
                if tokens[i + 2] == ';':
                    print('syntax is correct')
                else:
                    print('syntax is not correct !KEYWORD SHOULD BE FOLLOWED BY ";" ')
            else:
                print('syntax error!KEYWORD SHOULD BE FOLLOWED BY "IDENTIFIER"')


#jump_statement(tokens, datatype)

def unary_operator(tokens, datatype):
    for i, j in enumerate(tokens):
        if datatype[i] == 'identifier' or datatype[i] == 'numeral':
            if datatype[i + 1] == 'operator':
                if datatype[i + 2] == 'identifier' or datatype[i + 2] == 'numeral':
                    if tokens[i + 3] == ';':
                        print('syntax is correct')
                    else:
                        print('syntax is not correct it should be follow by ";"')
                else:
                    print('syntax is not correct it must be follow by "identifier or numeral"')
            # else:
            # print('syntax is not correct it must be follow by"an operator"')


#unary_operator(tokens, datatype)

def int_fun(tokens, datatype):
    for i, j in enumerate(tokens):
        if j == 'int':
            if datatype[i + 1] == 'identifier':
                if tokens[i + 2] == '=':
                    if datatype[i + 3] == 'numeral':
                        if tokens[i + 4] == ';':
                            print('correct syntax')
                        else:
                            print('incorrect syntax')
                    else:
                        print('incorrect syntax')
                else:
                    print('incorrect syntax')
            else:
                print('incorrect syntax')


int_fun(tokens, datatype)

def enumeration_constant(tokens, datatype):
    for i, j in enumerate(tokens):
        if j == 'enumerate':
            if datatype[i + 1] == 'identifier':
                if tokens[i + 2] == ';':
                    print('correct syntax')
                else:
                    print('incorrect syntax! KEYWORD SHOULD BE FOLLOWED BY ";"')
            else:
                print('incorrect syntax! KEYWORD SHOULD BE FOLLOWED BY "identifier"')


# enumeration_constant(tokens, datatype)


def if_stmt(tokens, datatype):
    for i, j in enumerate(tokens):
        if j == 'if':
            if tokens[i + 1] == '(':
                if datatype[i + 2] == 'identifier':
                    if datatype[i + 3] == 'operator':
                        if datatype[i + 4] == 'identifier':
                           if tokens[i+5] == ')':
                                print('correct syntax')
                           else:
                                print('incorrect syntax it shoud ble follow by ")" ')
                        else:
                            print('incorrect 1')
                    else:
                        print('incorrect 2' )
                else:
                    print('incorrect 3')
            else:
                print('incorrect 4 ')



#if_stmt(tokens, datatype)
