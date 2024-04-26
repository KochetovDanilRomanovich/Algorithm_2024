def getting_psp(string):
    stack = []
    extra_character = 0
    for i in string:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                extra_character += 1
    
    return len(stack) + extra_character

if __name__ == "__main__":
    string = input()
    
    print(getting_psp(string))