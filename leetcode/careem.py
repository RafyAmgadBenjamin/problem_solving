def solution(s):
    c = s[0]
    if c >= 'A' and c <= 'Z':    # please fix condition
        return "upper"
    elif c >= 'a' and c <= 'z':  # please fix condition
        return "lower"
    elif c >= '0' and c <= '9':  # please fix condition
        return "digit"
    else:
        return "other"

print(solution(s="&"))