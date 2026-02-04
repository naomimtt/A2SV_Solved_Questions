def swap_case(s):
    s2=''
    for i in s:
        if i.islower():
            s2+=i.upper()
        else:
            s2+=i.lower()
    return s2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
