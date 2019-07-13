data = 0b110011011011110001111000001101111111000011111111101111111001111

# dataビット数
n = 64


def rule126(que):
    ans = 0
    for i in range(n):
        jd = 0
        for j in range(-1, 2):
            jd += que >> ((i + j) % n) & 1

        if 0 < jd < 3:
            ans |= 1 << i

    return ans


result_list = []


def back_rule126(result, ans, dig):
    if dig == n:
        if rule126(result) == ans:
            result_list.append(result)
            result = "%x" % result
            print(result)
        return

    for x in range(2):
        if dig >= 2:
            jd = x

            for j in range(-2, 0):
                jd += result >> ((dig + j) % n) & 1
            if int(0 < jd < 3) != (ans >> (dig - 1) & 1):
                continue
        back_rule126(result | x << dig, ans, dig + 1)


back_rule126(0, 0x66de3c1bf87fdfcf, 0)
print(len(result_list))
