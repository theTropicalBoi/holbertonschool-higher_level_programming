def multiple_returns(sentence):
    if sentence == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
