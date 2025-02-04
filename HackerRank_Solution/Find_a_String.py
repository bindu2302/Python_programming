def count_substring(main_str,sub_str):
    count = 0
    n = len(main_str) - len(sub_str) + 1
    for i in range(n):
        if(sub_str == main_str[i:len(sub_str)+i]):
            count += 1
    return count


main_str = input()
sub_str = input()
count = count_substring(main_str,sub_str)
print(count)