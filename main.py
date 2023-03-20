# Script to check if the input is a PGN file or not, by lexical analysis and grammar analysis

import ply.lex as lex
import ply.yacc as yacc
import re


class Move:
    def __init__(self, id, move, comment):
        self.id = id
        self.move = move
        self.comment = comment

    def __str__(self):
        return "id: " + str(self.id) + ", move: " + self.move + ", comment: " + self.comment

    def __repr__(self):
        return "id: " + str(self.id) + ", move: " + self.move + ", comment: " + self.comment

    def __eq__(self, other):
        return self.id == other.id and self.move == other.move and self.comment == other.comment

    def __hash__(self):
        return hash((self.id, self.move, self.comment))

    def get_id(self):
        return self.id

    def get_move(self):
        return self.move

    def get_comment(self):
        return self.comment

    def set_id(self, id):
        self.id = id

    def set_move(self, move):
        self.move = move

    def set_comment(self, comment):
        self.comment = comment


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    your_string2 = '1. e4 d5 {Scandinavian defence (often follows 2. exd5 Da5 {not often 2... c6})}'
    your_string = '1. e4 {Notes by Richard Reti} 1... e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 ' \
                  '6. h4 {This ingenious method of play which has subsequently been adopted by all modern masters is ' \
                  'characteristic of Alekhine’s style.} 6... Bxg5 7. hxg5 Qxg5 8. Nh3 {! The short-stepping knight is ' \
                  'always brought as near as possible to the actual battle field. Therefore White does not make the ' \
                  'plausible move 8 Nf3 but 8 Nh3 so as to get the knight to f4.} 8... Qe7 9. Nf4 Nf8 10. Qg4 f5 {The ' \
                  'only move. Not only was 11 Qxg7 threatened but also Nxd5.} 11. exf6 gxf6 12. O-O-O {He again threatens ' \
                  'Nxd5.} 12... c6 13. Re1 Kd8 14. Rh6 e5 15. Qh4 Nbd7 16. Bd3 e4 17. Qg3 Qf7 {Forced - the sacrifice of ' \
                  'the knight at d5 was threatened and after 17...Qd6 18 Bxe4 dxe4 19 Rxe4 and 20 Qg7 wins.} 18. Bxe4 ' \
                  'dxe4 19. Nxe4 Rg8 20. Qa3 {Here, as so often happens, a surprising move and one difficult to have ' \
                  'foreseen, forms the kernel of an apparently simple Alekhine combination.} 20... Qg7 {After 20.Qe7 ' \
                  '21.Qa5+ b6 22.Qc3 would follow.} 21. Nd6 Nb6 22. Ne8 Qf7 {White mates in three moves.} 23. Qd6+ 1-0 '

    first_regex = r"\[.* \".*\"\]"

    match = re.search(first_regex, your_string)

    if match:
        print("There is PNG title")
        content = your_string[match.end():]
        print(content)
    else:
        print("There is no PNG title")
        content = your_string

    # after the last title it's the first move which begin with a 1.
    # so we can check if the first move is 1 or not and if it's not 1 then it's not a PGN file
    # after the first move it's just moves and comments so if there is another thing than a move or
    # a comment then it's not a PGN file

    begin_regex = r" *1\. .*"

    match = re.search(begin_regex, content)

    if match:
        print("There is a first move")

    else:
        print("There is no first move")

    # check if the move is correct or not
    # a move is correct if it's a number in the order of the moves, and it's followed by a dot, and then a move or
    # a comment. A comment is a string between curly brackets.
    # After a comment the move is reminded by his number and 3 dots.

    result = r'1-0|0-1|1/2-1/2'

    match = re.search(result, content)

    if match:
        print("There is a result")
        win = match.group()
        print(win)
        # content = content without the result

        content = content[:match.start()]
    else:
        print("There is no result")

    # create an array of moves objects which contain the id of the move, the id is the number of the move,
    # the move and eventually the comment

    # split the content by the moves

    lines = []
    move_regex = r"\d+\.\s+(\S+)(?:\s*\{.*?\})?\s+(\S+)(?:\s*\{.*?\})?\s*[a-zA-Z]*[1-8]*\s(?:\s*\{.*?\})?\s*"

    tabMoves = []

    listM = re.search(move_regex, content)

    while listM:
        tabMoves.append(listM.group())
        content = content[listM.end():]
        listM = re.search(move_regex, content)

    print(tabMoves)

    id_regex = r"\d+."
    comment_regex = r"\{.*?\}"
    t_MOVE = r'[RNBQK][a-hA-H]+[1-8]\+*'
    t_MOVE_PAWN = r'\sP?[a-h]+[1-8]\+*'
    t_CAPTURE = r'[RNBQK][x][a-hA-H]+[1-8]\+*'
    t_CAPTURE_PAWN = r'\sP?[a-h][x]+[a-h][1-8]\+*'

    moveVariable = Move(0, "", "")
    for line in tabMoves:
        id = re.search(id_regex, line).group()
        if re.search(comment_regex, line):
            comment = re.search(comment_regex, line).group()
            # delete the comment from the line
            line = line[:re.search(comment_regex, line).start()] + line[re.search(comment_regex, line).end():]
        else:
            comment = ""

        print(id)
        move = re.findall(t_MOVE, line)
        move_pawn = re.findall(t_MOVE_PAWN, line)
        capture = re.findall(t_CAPTURE, line)
        capture_pawn = re.findall(t_CAPTURE_PAWN, line)

        if move:
            print(f'it is a move : {move}')
        if move_pawn:
            print(f'it is a move pawn : {move_pawn}')
        if capture:
            print(f'it is a capture : {capture}')
        if capture_pawn:
            print(f'it is a capture pawn : {capture_pawn}')

