inp = 'Enter a number: '
total = 0
count = 0

while True:
        s = input(inp)
        if s == 'done':
                break
        try:
                total += float(s)
                count += 1
                average = total / count
        except ValueError:
                print("Invalid Input. Try again: ")
        continue
print('You entered %s numbers whose total is %s and average is %s.' % (str(count), str(total), str(average)))