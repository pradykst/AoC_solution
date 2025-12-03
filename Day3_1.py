def best_for_line(line:str)-> int:
    line=line.strip()
    if len(line)<2:
        return 0
    

    digits =[int(c) for c in line]
    n=len(digits)

    max_first=max(digits[:-1])
    
    first_idx=None
    for i in range(n-1):
        if digits[i]==max_first:
            first_idx=i
            break

    

    second_digit=max(digits[first_idx+1:])

    return 10*max_first+second_digit

def main():

    total=0

    with open("input3.txt","r") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue

            total+=best_for_line(line)
    print(total)


if __name__=="__main__":
    main()