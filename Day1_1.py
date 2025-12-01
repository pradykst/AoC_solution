def read_rotations(filename:str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]


def compute_password(rotations: list[str]) -> int:
    position = 50
    zero_count=0

    for instr in rotations:
        direction = instr[0]
        distance = int(instr[1:])

        if direction =="R":
            delta=distance
        elif direction =="L":
            delta=-distance
        else:
            raise ValueError(f"Invalid direction: {direction}")
        
        position = (position+delta) % 100

        if position == 0:
            zero_count +=1

    return zero_count

if __name__=="__main__":
    rotations=read_rotations("input1_1.txt")
    password=compute_password(rotations)
    print(password)
