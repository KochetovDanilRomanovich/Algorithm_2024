def search_for_less(list_of_numbers):
    stack = []
    result = [-1] * len(list_of_numbers)
    for i in range(len(list_of_numbers)):
        while len(stack) > 0 and list_of_numbers[stack[-1]] > list_of_numbers[i]:
            result[stack.pop()] = i
        stack.append(i)
    
    return result

if __name__ == "__main__":
    number = int(input())
    list_of_numbers = list(map(int, input().split()))
    
    answer = search_for_less(list_of_numbers)
    print(*answer)