


def part1():
    id_file = open("ids.txt","r")

    current: str = id_file.readline()
    list_0: list[int] = []
    list_1: list[int] = []

    while current:
        ids: list[int] = current.split("   ")
        list_0.append(int(ids[0]))
        list_1.append(int(ids[1]))

        current: str = id_file.readline()


    list_0.sort()
    list_1.sort()

    res: int = 0

    for i in range(len(list_0)):
        dif = abs(list_0[i] - list_1[i])
        res += dif
        
    
    print(res)


def part2():
    id_file = open("ids.txt","r")

    current: str = id_file.readline()
    list_1_counter = {}
    list_0: list[int] = []

    while current:
        ids: list[int] = current.split("   ")
        list_0.append(int(ids[0]))

        try:
            list_1_counter[int(ids[1])] += 1
        except KeyError:
            list_1_counter[int(ids[1])] = 1

        current: str = id_file.readline()
    
    print(list_1_counter)

    res: int = 0
    for num in list_0:
        try:
            res += num * list_1_counter[num]
        except KeyError:
            continue    
    
    print(res)

    

if __name__ == "__main__":
    #part1()

    part2()


