import re


class Move:
    def __init__(self, id, move, comment=None):
        self.id = id
        self.move = move
        self.comment = [] if comment is None else comment

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
        self.comment = comment if comment is not None else []

    def add_comment(self, new_comment):
        self.comment.append(new_comment)

    def remove_comment(self, comment):
        self.comment.remove(comment)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    your_string = '[Event "Mannheim"] [Site "Mannheim GER"] [Date "1914.08.01"] [EventDate "1914.07.20"] [Round "11"] ' \
                  '[Result "1-0"] [White "Alexander Alekhine"] [Black "Hans Fahrni"] [ECO "C13"] [WhiteElo "?"] [' \
                  'BlackElo "?"] [PlyCount "45"] 1. e4 {Notes by Richard Reti} 1... e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 ' \
                  '5. e5 Nfd7 6. {booo} 6... h4 {This ingenious method of play which has subsequently been adopted by ' \
                  'all modern masters is characteristic of Alekhine’s style.({test}test)} 6... Bxg5 7. hxg5 Qxg5 8. Nh3 {! The ' \
                  'short-stepping knight is always brought as near as possible to the actual battle field. Therefore ' \
                  'White does not make the plausible move 8 Nf3 but 8 Nh3 so as to get the knight to f4.} 8... Qe7 9. ' \
                  'Nf4 Nf8 10. Qg4 f5 {The only move. Not only was 11 Qxg7 threatened but also Nxd5.} 11. exf6 gxf6 ' \
                  '12. O-O-O {He again threatens Nxd5.} 12... c6 13. Re1 Kd8 14. Rh6 e5 15. Qh4 Nbd7 16. Bd3 e4 17. ' \
                  'Qg3 Qf7 {Forced - the sacrifice of the knight at d5 was threatened and after 17...Qd6 18 Bxe4 dxe4 ' \
                  '19 Rxe4 and 20 Qg7 wins.} 18. Bxe4 dxe4 19. Nxe4 Rg8 20. Qa3 {Here, as so often happens, ' \
                  'a surprising move and one difficult to have foreseen, forms the kernel of an apparently simple ' \
                  'Alekhine combination.} 20... Qg7 {After 20.Qe7 21.Qa5+ b6 22.Qc3 would follow.} 21. Nd6 Nb6 22. ' \
                  'Ne8 Qf7 {White mates in three moves.} 23. Qd6+ 1-0 '

    title_regex = r"\[[a-zA-Z\s]*\s\"[^\"]*\"\]\s*"

    verify = 0

    match = re.search(title_regex, your_string)

    if match:
        content = your_string[:match.start()] + your_string[match.end():]
        match = re.search(title_regex, content)
    else:
        print("There is no PGN title")
        content = your_string
        verify += 1

    while match:
        content = content[:match.start()] + content[match.end():]
        match = re.search(title_regex, content)

    result = r'1-0|0-1|1/2-1/2'

    match = re.search(result, content)

    if match:
        win = match.group()
        # content = content without the result

        content = content[:match.start()]
    else:
        print("There is no correct result")
        verify += 1

    move_regex = r"\d+\.\s+(?:\s*\{.*?\})?\s*(\S+)(?:\s*\{.*?\})?\s+(\S+)(?:\s*\{.*?\})?\s*[a-zA-Z]*[1-8]*\s(?:\s*\{.*?\})?\s*(?:(\d+\...\s([a-zA-Z]*[1-8]*\s)*)?)"

    tabMoves = []

    listM = re.search(move_regex, content)

    while listM:
        tabMoves.append(listM.group())
        content = content[:listM.start()] + content[listM.end():]
        listM = re.search(move_regex, content)

    last_move_regex = "\d+\.\s+(?:\s*\{.*?\})?\s*(\S+)(?:\s*\{.*?\})?\s*[a-zA-Z]*[1-8]*\s(?:\s*\{.*?\})?\s*"

    if re.search(last_move_regex, content):
        lastMove = re.search(last_move_regex, content).group()
        content = content[:re.search(last_move_regex, content).start()] + content[re.search(last_move_regex, content).end():]

    else:
        lastMove = ""

    content = content.replace(" ", "")
    content = content.replace("\t", "")
    content = content.replace("\n", "")
    content = content.replace("\r", "")

    if content:
        print("There is some unrecognised characters in the PGN file")
        print(f"Unrecognised characters : {content}")
        verify += 1

    id_regex = r"\d+."
    pre_comment_regex = r"\{.*?\}\s+\d+\.\.\.\s"

    t_MOVE = r'[RNBQK][a-hA-H]+[1-8]\+?'
    t_MOVE_PAWN = r'\sP?[a-h]+[1-8]\+?'
    t_CAPTURE = r'[RNBQK][x][a-hA-H]+[1-8]\+?'
    t_CAPTURE_PAWN = r'\sP?[a-h][x]+[a-h][1-8]\+?'
    t_Castle = r'O-O-O|O-O'

    tabFinal = []
    if lastMove != "":
        idLastMove = int(re.search(id_regex, lastMove).group().replace(".", ""))
    else:
        idLastMove = 0
    for line in tabMoves:
        comment = []
        id = re.search(id_regex, line).group()
        if re.findall(pre_comment_regex, line):
            comment = re.findall(pre_comment_regex, line)
            # delete the comment from the line
            for c in comment:
                line = line.replace(c, "")
        if re.search(r"\{.*\}\s+", line):
            comment.append(re.search(r"\{.*\}\s+", line).group())
            line = line.replace(re.search(r"\{.*\}\s+", line).group(), "")

        line = line.replace(id, "")
        id = int(id.replace(".", ""))
        move = re.findall(t_MOVE, line)
        move_pawn = re.findall(t_MOVE_PAWN, line)
        capture = re.findall(t_CAPTURE, line)
        capture_pawn = re.findall(t_CAPTURE_PAWN, line)
        castle = re.findall(t_Castle, line)

        moveGlobal = move + move_pawn + capture + capture_pawn + castle

        if moveGlobal:
            for deleteMove in moveGlobal:
                line = line.replace(deleteMove, "")

        # delete invisible characters and after check if there is some characters left
        line = line.replace(" ", "")
        line = line.replace("\t", "")
        line = line.replace("\n", "")
        line = line.replace("\r", "")

        if line:
            print("There is some unrecognised characters in the PGN file")
            print(f"At move number {id}")
            print(f"Unrecognised characters : {line}")
            verify += 1

        if len(moveGlobal) != 2:
            if len(moveGlobal) == 1:
                print("There is only one correct move")
                print(f"At move number {id}")
                verify += 1
            elif len(moveGlobal) == 0:
                print("There is no correct move")
                print(f"At move number {id}")
                verify += 1
            else:
                print("There is more than 2 correct moves")
                print(f"At move number {id}")
                verify += 1

        tabFinal.append(Move(id, moveGlobal, comment))

    if tabFinal[0].id != 1:
        print("The PGN file doesn't start with the move 1")
        verify += 1

    for i in range(1, len(tabFinal) - 1):
        if tabFinal[i - 1].id + 1 != tabFinal[i].id:
            verify += 1
            print(f"The PGN file doesn't have increasing moves : Error at move {tabFinal[i].id}")
            break
    if idLastMove != 0:
        if idLastMove != tabFinal[len(tabFinal) - 1].id + 1:
            print(f"The PGN file doesn't have increasing moves : Error at move {idLastMove}")
            verify += 1

        l_MOVE = r'[RNBQK][a-hA-H]+[1-8]\+*'
        l_MOVE_PAWN = r'\sP?[a-h]+[1-8]\+*'
        l_CAPTURE = r'[RNBQK][x][a-hA-H]+[1-8]\+*'
        l_CAPTURE_PAWN = r'\sP?[a-h][x]+[a-h][1-8]\+*'

        latsMove_pawn = re.findall(l_MOVE_PAWN, lastMove)
        lastCapture = re.findall(l_CAPTURE, lastMove)
        lastCapture_pawn = re.findall(l_CAPTURE_PAWN, lastMove)
        lastMove = re.findall(l_MOVE, lastMove)

        moveGlobal = lastMove + latsMove_pawn + lastCapture + lastCapture_pawn

        if len(moveGlobal) > 2:
            print("There is more than 2 correct moves")
            verify += 1

        if len(moveGlobal) == 0:
            print("There is no correct move")
            verify += 1

    if verify != 0:
        print("The PGN file is not correct")
        print(f"There is {verify} errors")
    else:
        print("The PGN file is correct")
