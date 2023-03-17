import re


def is_pgn_file(your_string):
    # Check if there is PGN title
    title_regex = r"\[.* \".*\"\]"
    match = re.search(title_regex, your_string)
    if not match:
        return False

    # Check if there is a first move
    move_regex = r"\b1\."
    match = re.search(move_regex, your_string)
    if not match:
        return False

    # Check if the moves are in correct format
    move_regex = r"\d+\.\s*\S+|\{\S+\}"
    moves = re.findall(move_regex, your_string[match.end():])
    for i, move in enumerate(moves):
        if i % 2 == 0:  # check if it's a move number
            if not re.match(r"\d+\.", move):
                return False
        else:  # check if it's a move or comment
            if not re.match(r"\S+|\{.*\}", move):
                return False

    return True


# Example usage
pgn_file = '[Event "Mannheim"] [Site "Mannheim GER"] [Date "1914.08.01"] [EventDate "1914.07.20"] [Round "11"] [' \
           'Result "1-0"] [White "Alexander Alekhine"] [Black "Hans Fahrni"] [ECO "C13"] [WhiteElo "?"] [BlackElo ' \
           '"?"] [PlyCount "45"] 1. e4 {Notes by Richard Reti} 1... e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 ' \
           '6. h4 {This ingenious method of play which has subsequently been adopted by all modern masters is ' \
           'characteristic of Alekhine’s style.} 6... Bxg5 1-0 '
non_pgn_file = '[Event "Mannheim"] [Site "Mannheim GER"] [Date "1914.08.01"] [EventDate "1914.07.20"] [Round "11"] [' \
           'Result "1-0"] [White "Alexander Alekhine"] [Black "Hans Fahrni"] [ECO "C13"] [WhiteElo "?"] [BlackElo ' \
           '"?"] [PlyCount "45"] 2. e4 {Notes by Richard Reti} 2... e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 ' \
           '6. h4 {This ingenious method of play which has subsequently been adopted by all modern masters is ' \
           'characteristic of Alekhine’s style.} 6... Bxg5 1-0 '

print(is_pgn_file(pgn_file))  # Output: True
print(is_pgn_file(non_pgn_file))  # Output: False
