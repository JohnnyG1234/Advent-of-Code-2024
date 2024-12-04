

def find_xmas(index: list[int], puzzle: list[str]):
    m_index = find_M(index, puzzle)

    if not m_index:
        return None
    
    print(m_index)
    


def find_M(index: list[int], puzzle: list[str]):
    try:
        if puzzle[index[0]][index[1] + 1] == "M":
            print(puzzle[index[0]][index[1] + 1])
            return [index[0], index[1]]
    except IndexError:
        pass

    try:
        if puzzle[index[0]][index[1] - 1] == "M":
            print(puzzle[index[0]][index[1] - 1])
            return [index[0], index[1]]
    except IndexError:
        pass

    try:
        if puzzle[index[0]+1][index[1]] == "M":
            print(puzzle[index[0]+1][index[1]])
            return [index[0]+1, index[1]]
    except IndexError:
        pass

    try:
        if puzzle[index[0]-1][index[1]] == "M":
            print(puzzle[index[0]-1][index[1]])
            return [index[0]-1, index[1]]
    except IndexError:
        pass

    return None



def part1():
    data_file = open("data.txt","r")
    data = data_file.readline()
    puzzle: list[str] = []

    while data:
        puzzle.append(data)
        data = data_file.readline()

    chars = data_file.read()
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == "X":
                find_xmas([i,j], puzzle)





















if __name__ == "__main__":
    part1()