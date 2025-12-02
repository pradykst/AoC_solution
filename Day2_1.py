def parse_ranges_from_file(filename:str):
    with open(filename, "r", encoding="utf-8") as f:
        text=f.read()

    ranges=[]
    parts=text.replace("\n", "").split(",")

    for part in parts :
        part=part.strip()
        if not part :
            continue
            
        a_str,b_str=part.split("-")
        a,b=int(a_str),int(b_str)
        ranges.append((a,b))

    return ranges


def is_valid_id(n:int)-> bool:
    s=str(n)
    length=len(s)

    if length%2!=0:
        return False
    
    half = length//2
    first_half=s[:half]
    second_half=s[half:]

    return first_half==second_half



def sum_invalid_ids(ranges):
    total=0
    for start,end in ranges:
        for x in range(start,end+1):
            if is_valid_id(x):
                total+=x
    return total


def main():
    ranges=parse_ranges_from_file("input2_1.txt")
    result=sum_invalid_ids(ranges)
    print(f"sum of all invalid ids {result}")

if __name__=="__main__":
    main()