def best_k_for_line( line: str , k:int =12)->int:
    line=line.strip()

    digits=[int(c) for c in line]

    n=len(digits)

    if n<k:
        raise ValueError("line is too short")

    if n==k:
        return int(line)

    

    chosen=[]

    start=0

    while k>0:

        end=n-k
        max_digit=-1
        max_idx=start

        for i in range(start,end+1):
            d=digits[i]

            if d>max_digit:
                max_digit=d
                max_idx=i

            if d==9:
                pass

        chosen.append(str(max_digit))

        start=max_idx+1
        k-=1

    return int("".join(chosen))


def main():
    total=0
    with open("input3.txt","r") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue

            total+=best_k_for_line(line)

    print(total)



if __name__=="__main__":
    main()

        