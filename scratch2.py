class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if set(p) == {"*"}: # when p = "*", "**", "***", etc
            return True

        if (len(s) != len(p)) and "*" not in p:
            return False

        segs = []
        temp = ""
        a = p.replace("*","")
        a = a.replace("?", "")
        for char in a:
            if char not in temp:
                temp += char
            else:
                segs.append(temp)
                temp = ""
                temp += char

        print(segs)





class Testing:

    from dataclasses import dataclass

    @dataclass
    class Case:
        s: str
        p: str
        output: bool

    cases = [Case("aa", "a", False), Case("aa", "*", True), Case("abcabczzzde","*abc???de*",True), Case("cb", "?a", False), Case("abceb","*a*b",True), Case("acdcb","a*c?b",False), Case("", "******", True), Case("ab","*?*?*", True), Case("hi","*?",True), Case("b","*a*",False), Case("aaaa","***a",True), Case("ho","**ho",True), Case("abce","abc*?",True), Case("mississippi","m*iss*",True),Case("mississippi","m*iss*iss*",True)]
    cases = [Case("abcabczzzde","*abc???de*",True)]


    def Test(self, cases=cases):
        for case in cases:
            ans = Solution.isMatch(Solution,case.s,case.p)
            if ans == case.output:
                print(f'test passed with {case.s}, {case.p}: output was {ans}')
            else:
                print(f'test FAILED with {case.s}, {case.p}: output was {ans} not {case.output}')

Testing.Test(Testing)