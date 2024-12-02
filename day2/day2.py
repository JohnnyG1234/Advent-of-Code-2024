
def part1():
    data_file = open("data.txt","r")

    res: int = 0

    current: str = data_file.readline()

    while current:
        data = current.split(" ")
        
        # if we are increasing then this is 1 if decreasing this is -1
        inc_or_dec = 0
        prev = float('inf')
        is_valid = True

        for s in data:
            num: int = int(s)
            if prev == float('inf'):
                prev = num
                continue
            #print(prev)
            #print(num)
                
            if abs(prev - num) > 3 or prev == num:
                is_valid = False
                break
            
            if inc_or_dec == 0:
                if prev > num:
                    inc_or_dec = -1
                elif prev < num:
                    inc_or_dec = 1
            
            if inc_or_dec == 1 and prev > num:
                is_valid = False
                break

            if inc_or_dec == -1 and prev < num:
                is_valid = False
                break

            prev = num

        
        #print(data)
        #print(is_valid)
        if is_valid:
            res += 1

        current = data_file.readline()

    print(res)


def part2():
    data_file = open("data.txt","r")

    res: int = 0

    current: str = data_file.readline()

    while current:
        data = current.split(" ")
        
        # if we are increasing then this is 1 if decreasing this is -1
        inc_or_dec = 0
        prev = float('inf')
        is_valid = True
        problem_damped = False

        for s in data:
            num: int = int(s)
            if prev == float('inf'):
                prev = num
                continue
            #print(prev)
            #print(num)
                
            if abs(prev - num) > 3 or prev == num:
                if problem_damped == False:
                    problem_damped = True
                    continue
                else:
                    is_valid = False
                    break
            
            if inc_or_dec == 0:
                if prev > num:
                    inc_or_dec = -1
                elif prev < num:
                    inc_or_dec = 1
            
            if inc_or_dec == 1 and prev > num:
                if problem_damped == False:
                    problem_damped = True
                    inc_or_dec = 0
                    prev = num
                    continue
                else:
                    is_valid = False
                    break

            if inc_or_dec == -1 and prev < num:
                if problem_damped == False:
                    problem_damped = True
                    inc_or_dec = 0
                    prev = num
                    continue
                else:
                    is_valid = False
                    break

            prev = num

        
        #print(data)
        #print(is_valid)
        if is_valid:
            res += 1

        current = data_file.readline()

    print(res)

if __name__ == "__main__":
    #part1()
    part2()