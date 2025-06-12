def bowling_score(score):

    frames_list = score.split()
    total_score = 0
    current_frame_idx = 0

    while current_frame_idx < len(frames_list):
        current_frame = frames_list[current_frame_idx]
        if current_frame_idx != len(frames_list) - 1:
            next_frame = frames_list[current_frame_idx + 1]
            
        # handling strike as last frame in line
        if current_frame == "X" and current_frame_idx == len(frames_list) - 1:
            total_score += 10

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
        if '/' in current_frame and 'X' in next_frame:
            total_score += 20
        
        elif '/' in current_frame:
            next_bowl = int(next_frame[0])           
            total_score += 10 + next_bowl
        
        # handling open frames
        if current_frame.isnumeric():          
            total_score += int(current_frame[0]) + int(current_frame[1])
        
        current_frame_idx += 1
    
    return total_score