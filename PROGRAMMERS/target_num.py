def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers :
        return 0
    return solution(numbers[1:], target + numbers[0]) +solution(numbers[1:], target-numbers[0])

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))

