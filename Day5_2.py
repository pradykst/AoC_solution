import bisect

def parse_input():
    with open("input5.txt", "r") as f:
        lines=[line.strip() for line in f]


    

    split_idx=lines.index("")

    range_lines=lines[:split_idx]

    id_lines=lines[split_idx+1:]

    ranges=[]

    for r1 in range_lines:
        a,b=r1.split("-")

        ranges.append((int(a),int(b)))

    
    ids =[int(x) for x in id_lines if x!= ""]

    return ranges


def merge_ranges(ranges):
    if not ranges:
        return []


    ranges.sort()

    merged=[list(ranges[0])]

    for s,e in ranges[1:]:
        last_s,last_e=merged[-1]

        if s<=last_e+1:
            merged[-1][1]=max(last_e,e)
        else:
            merged.append([s,e])
    
    return [(s,e) for s,e in merged]

def count_total_fresh_ids():
    ranges=parse_input()
    merged=merge_ranges(ranges)
    return sum(e-s+1 for s,e in merged)


if __name__=="__main__":
    
    print(count_total_fresh_ids())

