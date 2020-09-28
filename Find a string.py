def count_substring(string, sub_string):
    ct = 0
    while sub_string in string:
        ct += 1
        string = string[string.find(sub_string)+1:]
    return ct

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
