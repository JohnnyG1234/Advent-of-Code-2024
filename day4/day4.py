
#
def findM(index:int):
    print(index)


def part1():
    data_file = open("data.txt","r")
    data = data_file.read()
    for i in range(len(data)):
        if data[i] == "X":
            findM(i)





















if __name__ == "__main__":
    part1()