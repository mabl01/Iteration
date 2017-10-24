def makeup_to_90(names, scores):
    for i in range (0, len(scores)):
        if scores[i] < 90:
            print names[i] + ", please make test corrections. You can raise your score to a 90 if you wish."
