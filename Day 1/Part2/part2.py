import re

num_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def match_nums(line):
    foundNums = []
    found_num_dict = {
        'start': 0,
        'val': 0,
        'end': 0,
    }
    for num in num_dict:
        new_dict = found_num_dict.copy()
        
        for match in re.finditer(num, line, re.DOTALL):
            new_dict['start'] = match.start()
            new_dict['val'] = num_dict[num]
            new_dict['end'] = match.end()
            foundNums.append(new_dict.copy())

    return foundNums

def get_last_num(line):
    last = (0, '')

    for idx, num in enumerate(line):
        if num.isdigit():
            last = (idx, int(num))

    foundNums = match_nums(line)

    if len(foundNums) > 0:
        foundNums.sort(key=lambda x: x['start'])
        if foundNums[-1]['start'] > last[0]:
            last = foundNums[-1]
    
    return last

def get_first_num(line):
    first = (0, '')

    for i in range(len(line)):
        if line[i].isdigit():
            first = (i, line[i])
            break

    foundNums = match_nums(line)

    if len(foundNums) > 0:
        foundNums.sort(key=lambda x: x['start'])
        if foundNums[0]['start'] < first[0]:
            first = foundNums[0]

    return first

def get_coords(line):
    first = get_first_num(line)
    last = get_last_num(line)

    if isinstance(first, dict):
        first = first['val']
    else:
        first = first[1]

    if isinstance(last, dict):
        last = last['val']
    else:
        last = last[1]

    return str(first) + str(last)

def main():
    sum = 0
    with open('Day 1/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            sum += int(get_coords(line))

    print(sum)
    

if __name__ == '__main__':
    main()