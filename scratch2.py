def b(s):
    return '{:12b}'.format(1 + int(s, 2))


fuck = ['000000000000']


x = '000000000000'
while x != '111111111111':
    x = b(x)
    fuck.append(x)

fuck.append('111111111111')

def check_three_threes(x):
    count = 0
    for char in x:
        if char == "1":
            count += 1
    if count >= 3:
        return 1
    return 0

threethrees = 0
for shit in fuck:
    threethrees += check_three_threes(shit)

print(threethrees)



# count = 0
# for shit in fuck:
#     if (shit[0] == '0' and shit[1] == '0') or (shit[-1] == '1' and shit[-2] == '1' and shit[-3] == '1'):
#         count += 1
#
# print(count)