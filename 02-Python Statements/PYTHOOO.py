def removeOuterParentheses(S):
    result = []
    balance = 0
    current_authentic = ""
    
    for char in S:
        if char == '[':
            balance += 1
        else:
            balance -= 1
        
        current_authentic += char
        
        if balance == 0:
            result.append(current_authentic[1:-1])
            current_authentic = ""
    
    return ''.join(result)
print(1+2)