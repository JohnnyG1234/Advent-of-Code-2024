import re
PATTERN= re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)")

def try_mul(input_str: str):
    if PATTERN.match(input_str):
        nums:  list[str] = re.findall(r'\d+',input_str)
        product: int = int(nums[0])  * int(nums[1])
        print(product)
        return product
    else:
        return 0
    

def part1():
    data_file = open("data.txt","r")

    res: int = 0
    data: str = data_file.read()
    input_str: str = ""

    for i in range(len(data)):
        input_str = ""
        if data[i] == "m":
            j: int = i
            while data[j] != ")":
                input_str += data[j]
                j +=  1
            input_str +=  data[j]

        response = try_mul(input_str)
        if response == 0:
            continue
        res += response
    
    print(res)




            







if __name__  == "__main__":
    part1()