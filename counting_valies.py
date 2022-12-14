def countingValleys(steps, path):
    altitiude = 0
    inValley = None
    vallies = 0

    for i in range(0, steps):
        current_step = path[i]
        if current_step == 'U': 
            altitiude += 1
        elif current_step == 'D':
            altitiude -= 1
        
        if altitiude < 0:
            inValley = True
        if altitiude == 0 and inValley:
            inValley = False
            vallies += 1
        if altitiude > 0:
            inValley = None
        # print(inValley)
    return vallies


print(countingValleys(12, 'DDUUDDUDUUUD'))