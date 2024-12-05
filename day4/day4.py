

def find_xmas(index: list[int], puzzle: list[str]):
    m_indexs = find_letter(index, puzzle, "M")

    if m_indexs == []:
        return 0
    
    a_indexs = []
    for m_index in m_indexs:
        a_indexs.append(find_letter(m_index, puzzle, "A"))

    if a_indexs == []:
        return 0
    
    s_indexs = []
    for a_index in a_indexs:
        s_indexs.append(find_letter(a_index, puzzle, "S"))

    if s_indexs == []:
        return 0
    
    return  len(s_indexs)    


def find_letter(pos: list[int], puzzle: list[str], letter: str):
    indexes: list[list[int]] = []

    try:
        if puzzle[pos[0]][pos[1] + 1] == letter:
            #print(puzzle[index[0]][index[1] + 1])
            indexes.append([pos[0], pos[1] + 1])
    except IndexError:
        pass

    try:
        if puzzle[pos[0]][pos[1] - 1] == letter:
            #print(puzzle[index[0]][index[1] - 1])
            indexes.append[pos[0], pos[1] - 1]
    except IndexError:
        pass

    try:
        if puzzle[pos[0]+1][pos[1]] == letter:
            #print(puzzle[index[0]+1][index[1]])
            indexes.append[pos[0]+1, pos[1]]
    except IndexError:
        pass

    try:
        if puzzle[pos[0]-1][pos[1]] == letter:
            #print(puzzle[index[0]-1][index[1]])
            indexes.append[pos[0]-1, pos[1]]
    except IndexError:
        pass

    return indexes



def part1():
    data_file = open("data.txt","r")
    data = data_file.readline()
    puzzle: list[str] = []
    res = 0

    while data:
        puzzle.append(data)
        data = data_file.readline()

    chars = data_file.read()
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == "X":
                res += find_xmas([i,j], puzzle)
    
    print(res)





















if __name__ == "__main__":
    part1()