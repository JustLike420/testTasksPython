def main(n):
    sqrt_num = 0
    i = 0
    while sqrt_num < n:
        i += 1
        sqrt_num = i * i
    if sqrt_num == n:
        return i
    else:
        return None



if __name__ == "__main__":
    print(main(121))  # 11
    print(main(122))  # None
