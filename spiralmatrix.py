# def spiralOrder(matrix):
#     print(matrix)
#     print([*zip(*matrix)])
#     print([*zip(*matrix)][::-1])
#     print(matrix)
#     print(*matrix.pop(0))
#     #return matrix and [*matrix.pop(0)] + spiralOrder([*zip(*matrix)][::-1])


def spiralOrder(matrix):
    ans = []
    s = sum([len(i) for i in matrix])
    while len(ans) < s:
        ans += matrix[0][::] #forwards: all of first array
        if len(matrix) > 1:
            [ans.append(matrix[i][-1]) for i in range(1, len(matrix) - 1)]  # intermediates: last element of interior arrays
            ans += matrix[-1][::-1] #backwards: all of last array, reversed
            del matrix[0], matrix[-1]
            for array in matrix:
                del array[-1]
            if len(ans) == s: return ans
            [ans.append(matrix[i][0]) for i in range(-1,-(len(matrix))-1,-1)] #reverse intermediates: 1st of interiors
            for array in matrix:
                del array[0]
    return ans


def tests():
    examples = ([[1]],[[3],[2]],[['a','b'],['c','d']],[[1,2,3],[4,5,6],[7,8,9]],[['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']],[['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']])
    solutions = [[1],[3,2],['a','b','d','c'],[1,2,3,6,9,8,7,4,5],['a','b','c','d','h','l','p','o','n','m','i','e','f','g','k','j'],['a','b','c','d','e','j','o','t','y','x','w','v','u','p','k','f','g','h','i','n','s','r','q','l','m']]
    for i in range(len(examples)):
        result = spiralOrder(examples[i])
        if result == solutions[i]:
            print(f"Test passed with {examples[i]}: output was {result}")
        else:
            print(f"Test FAILED with {examples[i]}: output was {result} not {solutions[i]}")


tests()