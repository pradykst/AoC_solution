def parse_points(path):
    points=[]

    with open(path,"r") as f:
        for line in f:
            line=line.strip()

            if not line :
                continue
        
                
            x_str,y_str=line.split(",")
            x=int(x_str)
            y=int(y_str)

            points.append((x,y))

    return points


def max_rectangle_area(points):
    n=len(points)
    max_area=0

    for i in range(n):
        x1,y1=points[i]

        for j in range(i+1,n):
            x2,y2=points[j]

            width=abs(x1-x2)+1
            height=abs(y1-y2)+1

            area=width*height
            max_area=max(max_area,area)

    return max_area 

def main():
    points=parse_points("input9.txt")
    result=max_rectangle_area(points)
    print(result)


if __name__=="__main__":
    main()
