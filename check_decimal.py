numbers = [1,5,6,3,4,4,-4,3,-4,-5,-4,-4,4,-4,-4,4,-1,-5,-5,-5,-3,-5,3]
# positives = []
# negatives = []
total = 0
for number in numbers:
    if number < 0:
        total += number
        print(total, number)

print("The total negative numbers",total)