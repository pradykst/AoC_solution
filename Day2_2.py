def parse_ranges_from_file(filename:str):
    with open(filename, "r", encoding="utf-8") as f:
        text=f.read()
    

    text=text.replace("\n","")

    ranges=[]

    parts=text.split(",")

    for part in parts:
        part=part.strip()
        if not part:
            continue
        a_str,b_str=part.split("-")
        start=int(a_str)
        end=int(b_str)

        ranges.append((start,end))
    
    return ranges   




def is_valid_id_2(n:int)->bool:

    s=str(n)
    L=len(s)

    for p_len in range(1,L//2+1):
        if L%p_len!=0:
            continue

    
        pattern=s[:p_len]
        repeats=L//p_len

        if repeats>=2 and pattern*repeats==s:
            return True
    return False



def sum_invalid_ids_2(ranges):
    total=0
    for start,end in ranges:
        for x in range(start,end+1):
            if is_valid_id_2(x):
                total+=x
    return total



def main():
    ranges=parse_ranges_from_file("input2_1.txt")
    result=sum_invalid_ids_2(ranges)
    print(f"sum of all invalid ids {result }")


if __name__=="__main__":
    main()