def solution(readings):
    counts = {}

    for n in readings:
        # 1. Reduce number to a single digit
        while n >= 10:
            temp_sum = 0
            # Convert to string to iterate digits easily
            for digit in str(n):
                temp_sum += int(digit)
            n = temp_sum

        # 2. Count the frequency of this final single digit
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

    # 3. Find the digit with the highest frequency
    # If there is a tie, pick the higher digit
    best_digit = -1
    max_freq = -1

    for digit, freq in counts.items():
        if freq > max_freq:
            max_freq = freq
            best_digit = digit
        elif freq == max_freq:
            # Tie-breaker: choose the larger digit
            if digit > best_digit:
                best_digit = digit

    return best_digit

b = [3563,3252465,22,5,340,9,990,1,3543,5,2,5,6,4,34,5]
a= solution(b)
print(a)
