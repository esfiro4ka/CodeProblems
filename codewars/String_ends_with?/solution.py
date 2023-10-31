def solution(text, ending):
    if ending == text[-len(ending):]:
        return True
    return False
