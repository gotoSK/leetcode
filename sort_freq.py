# Sort on basis of frquency of repeatation of a character in a string
# String = mississippi
# Result = iiiissssppm

def sort_freq(s: str) -> str:
    unique = []
    result = []

    for x in s:
        found = False
        for y in unique:
            if x == y[0]:
                y[1] += 1
                found = True
                break
        if not found:
            unique.append([x, 1])
    
    unique.sort(key = lambda x: x[1], reverse=True)
    for char, freq in unique:
        for times in range(0, freq):
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    line = input()
    print(sort_freq(line))