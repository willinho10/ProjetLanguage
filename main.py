# Script to check if the input is a PGN file or not, by lexical analysis and grammar analysis

import ply.lex as lex
import ply.yacc as yacc
import re

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    your_string = '[Event "Mannheim"] [Site "Mannheim GER"] [Date "1914.08.01"] [EventDate "1914.07.20"] [Round "11"] [' \
                  'Result "1-0"] [White "Alexander Alekhine"] [Black "Hans Fahrni"] [ECO "C13"] [WhiteElo "?"] [BlackElo ' \
                  '"?"] [PlyCount "45"] 1. e4 {Notes by Richard Reti} 1... e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 ' \
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
    else:
        print("There is no PNG title")

    # after the last title it's the first move which begin with a 1.
    # so we can check if the first move is 1 or not and if it's not 1 then it's not a PGN file
    # after the first move it's just moves and comments so if there is another thing than a move or
    # a comment then it's not a PGN file

    end_of_title = your_string.find("1.")
    if end_of_title == -1:
        print("There is no first move")
    else:
        print("There is a first move")

    # check if the move is correct or not
    # a move is correct if it's a number in the order of the moves, and it's followed by a dot, and then a move or
    # a comment. A comment is a string between curly brackets.
    # After a comment the move is reminded by his number and 3 dots.

