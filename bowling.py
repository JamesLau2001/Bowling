def bowling_score(score):

    frames_list = score.split(" ")
    total_score = 0
    current_frame_idx = 0

    while current_frame_idx < len(frames_list):
        current_frame = frames_list[current_frame_idx]

        # handling strikes
        if current_frame == "X" and current_frame_idx == len(frames_list) - 1:
            total_score += 10

        elif current_frame == "X":
            next_frame = frames_list[current_frame_idx + 1]        
            total_score += 10 + int(next_frame[0]) + int(next_frame[1])

        # handling spares
        if len(current_frame) == 2 and '/' in current_frame:
            next_frame = frames_list[current_frame_idx + 1]
            first_score_of_next_frame = int(next_frame[0])           
            total_score += 10 + first_score_of_next_frame

        # handling non-strikes and non-spares
        if len(current_frame) == 2 and '/' not in current_frame:           
            total_score += int(current_frame[0]) + int(current_frame[1])
        
        current_frame_idx += 1
    
    return total_score