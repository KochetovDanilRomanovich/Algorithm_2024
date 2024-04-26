def search_for_minimums(list_of_numbers, step):
    deque = []
    result = []

    for i in range(len(list_of_numbers)):
        while len(deque) > 0 and deque[0] < (i - step + 1):
            deque.pop(0)
        while len(deque) > 0 and list_of_numbers[deque[-1]] > list_of_numbers[i]:
            deque.pop()
        
        deque.append(i)

        if i >= step - 1:
            result.append(list_of_numbers[deque[0]])

    return result

if __name__ == "__main__":
    number, step = map(int, input().split())
    list_of_numbers = list(map(int, input().split()))
    
    answer = search_for_minimums(list_of_numbers, step)
    
    for i in answer:
        print(i)