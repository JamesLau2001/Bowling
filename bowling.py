def bowling_score(score):

    frames_list = score.split()
    total_score = 0
    current_frame_idx = 0
    for current_frame_idx in range(0, len(frames_list)):
    
        current_frame = frames_list[current_frame_idx]
        if current_frame_idx != len(frames_list) - 1:
            next_frame = frames_list[current_frame_idx + 1]

        #handling spare or strike in final frame          
        if current_frame == "XXX": 
            total_score += 30
        elif "X" in current_frame and "/" in current_frame:
            total_score += 20
        elif len(current_frame) == 3 and "/" in current_frame and "X" not in current_frame:
            total_score += 10 + int(current_frame[2])
        elif len(current_frame) == 3 and "X" in current_frame and "/" not in current_frame:
            total_score += 10 + int(current_frame[1]) +int(current_frame[2])
    

        # handling strike as last but not final frame in line
        if current_frame == "X" and current_frame_idx == len(frames_list) - 1:
            break
        # handle strike followed by spare
        elif current_frame == "X" and "/" in next_frame:
            total_score += 20
        elif current_frame == "X" and next_frame == "X" and frames_list[current_frame_idx + 2] == "X":
            total_score += 30
        # handle double strike folowed by spare or open frame
        elif current_frame == "X" and next_frame == "X":
            total_score += 20 + int(frames_list[current_frame_idx + 2][0])
        # handle strike followed by non-spare
        elif current_frame == "X":
            total_score += 10 + int(next_frame[0]) + int(next_frame[1])

        # handling spares
        if '/' in current_frame and next_frame == "X":
            total_score += 20
        elif '/' in current_frame and len(next_frame) < 3:
            next_bowl = int(next_frame[0])           
            total_score += 10 + next_bowl
        
        # handling open frames
        if current_frame.isnumeric():          
            total_score += int(current_frame[0]) + int(current_frame[1])
        
    return total_score