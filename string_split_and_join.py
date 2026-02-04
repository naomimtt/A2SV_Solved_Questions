def split_and_join(line):
    split= line.split(' ')
    output='-'.join(split) 
    return output
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
