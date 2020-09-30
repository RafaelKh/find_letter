arr = ["K", "E", "F", "Y", "M", "A"]
ascii_codes = {}
for i in range(len(arr)):
    ascii_codes[i] = ord(arr[i])
el = ord("Y")


def liner_search (lis, element):
    for i in range(len(lis)):
        if lis[i] == element:
            return i
    return -1


print(liner_search(list(ascii_codes.values()), el))