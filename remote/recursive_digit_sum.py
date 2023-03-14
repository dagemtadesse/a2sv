def superDigit(n, k):
    # Write your code here
   
    digit = str(n)

    
    if len(digit) == 1:
        return digit
    else:
        result = sum(map(lambda x: int(x), [char for char in digit]))
        result *= k
        return superDigit(result, 1)
