import ply.lex as lex
import ply.yacc as yacc
import re

# Define tokens
tokens = (
    'MOVE',
    'COMMENT',
    'OPENING',
    'RESULT',
    'TITLE',
)

# Define regular expressions for tokens
t_MOVE = r'[1-9][0-9]*\.'
t_COMMENT = r'{[^}]*}'
t_OPENING = r'[a-zA-Z0-9#?+-=!\(\)/]+'
t_RESULT = r'1-0|0-1|1/2-1/2'
t_TITLE = r'\[[a-zA-Z]+\s+"[^"]*"\]'

# Define rules to ignore whitespace and tabs
t_ignore = ' \t'

# Define error handling rule
def t_error(t):
    print(f"Invalid character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()

# Define grammar rules
def p_game(p):
    '''
    game : tags moves
    '''

def p_tags(p):
    '''
    tags : tag
         | tag tags
    '''

def p_tag(p):
    '''
    tag : TITLE
        | RESULT
        | OPENING
    '''

def p_moves(p):
    '''
    moves : move
          | move moves
    '''

def p_move(p):
    '''
    move : MOVE OPENING COMMENT
         | MOVE OPENING
    '''

def p_error(p):
    if p:
        print(f"Syntax error at position {p.lexpos}")
    else:
        print("Syntax error at end of input")

# Build parser
parser = yacc.yacc()

if __name__ == '__main__':
    your_string = '[Event "Mannheim"] [Site "Mannheim GER"] [Date "1914.08.01"] [EventDate "1914.07.20"] [Round "11"] [' \
                  'Result "1-0"] [White "Alexander Alekhine"] [Black "Hans Fahrni"] [ECO "C13"] [WhiteElo "?"] [BlackElo ' \
                  '"?"] [PlyCount "45"] 1. e4 {Notes by Richard Reti} 1... e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 ' \
                  '6. h4 {This ingenious method of play which has subsequently been adopted by all modern masters is ' \
                  'characteristic of Alekhine’s style.} 6... Bxg5 1-0'

    # Check for title tags
    title_regex = r"\[.* \".*\"\]"
    match = re.search(title_regex, your_string)
    if match:
        print("PGN title tags found")
    else:
        print("PGN title tags not found")

    # Check for first move
    move_regex = r"\b1\."
    match = re.match(move_regex, your_string)
    if match:
        print("First move found")
    else:
        print("First move not found")

    # Parse the input string
    result = parser.parse(your_string)
    if result:
        print("PGN file syntax is correct")
    else:
        print("PGN file syntax is incorrect")
