def magic_num(num):
    total_sum = 0
    while num > 0:
        total_sum += num % 10
        num //= 10
    if total_sum > 9:
        return magic_num(total_sum)
    else:
        if total_sum == 1:
            return 1
        else:
            return 0

num=int(input())
print(magic_num(num))
