#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length < 1:
        return length, None
    else:
        chF = sentence[0]
        return length, chF
