def bowling_score(score):
    if score == "X":
        return 10
    elif len(score) == 2:
        split_score = list(score)
        total_score = int(split_score[0]) + int(split_score[1])
        return total_score 
    else:
        return 0
