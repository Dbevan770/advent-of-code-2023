'''
As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''

def get_first_and_last(line):
    first = (0, '')
    last = ''

    # find the first digit in the line and then
    # break from the loop
    for i in range(len(line)):
        if line[i].isdigit():
            first = (i, line[i])
            break

    # from the first digit, loop through the rest of the line
    # and find the last digit
    for j in line[first[0] + 1:]:
        if j.isdigit():
            last = j

    # if the last digit is not empty, then return the first and last
    # digits combined
    if last != '':
        coords = first[1] + last
        return int(coords)
    
    # if the last digit is empty, then return the first digit twice
    coords = first[1] + first[1]
    return int(coords)

def main():
    sum = 0

    # read the input file and loop through each line
    with open('input.txt') as f:
        lines = f.readlines()

        # strip the line of any whitespace and add the first and last
        # digits to the sum
        for line in lines:
            line = line.strip()
            sum += get_first_and_last(line)

    # print the sum
    print(f"sum: {sum}")

        
            

if __name__ == '__main__':
    main()