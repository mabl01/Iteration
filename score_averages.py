def average(scores):
    total = 0
    for n in scores:
        total += n

    return total / len(scores)

def average_cut_lowest_two(scores):
    current_min = scores[0]
    current_min_placement = -1
    for n in scores:
        if n <= current_min:
            current_min = n
    
    scores.remove(current_min):
    current_min2 = scores[0]
    for n in scores:
        if n <= current_min2:
            current_min2 = n

    scores_remove(current_min2)

    sum_cut_lowest_two = 0
    for n in scores:
        sum_cut_lowest_two += n
    
    return sum_cut_lowest_two / len(scores)