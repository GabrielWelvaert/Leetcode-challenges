
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if set(p) == {"*"}: # when p = "*", "**", "***", etc
            return True

        if (len(s) != len(p)) and "*" not in p:
            return False

        d = {}
        for i, char in enumerate(p):
            if char == "*":
                d[i] = char
            else:
                d[i] = None

        p = p.replace("*","")

        for i in range(len(p)):
            print(f"{p[i]} and {s[i]}")
            if p[i] != "?" and p[i] != "*" and p[i] not in s:
                return False
            if not (p[i] == s[i] or p[i] == "?"):
                if d[i+1] != "*":
                    return False

        return True









class Testing:

    from dataclasses import dataclass

    @dataclass
    class Case:
        s: str
        p: str
        output: bool

    cases = [Case("aa", "a", False), Case("aa", "*", True), Case("abcabczzzde","*abc???de*",True), Case("cb", "?a", False), Case("abceb","*a*b",True), Case("acdcb","a*c?b",False), Case("", "******", True), Case("ab","*?*?*", True), Case("hi","*?",True), Case("b","*a*",False), Case("aaaa","***a",True), Case("ho","**ho",True), Case("abce","abc*?",True), Case("mississippi","m*iss*",True),Case("mississippi","m*iss*iss*",True)]
    #cases = [Case("abcabczzzde","*abc???de*",True)]


    def Test(self, cases=cases):
        for case in cases:
            ans = Solution.isMatch(Solution,case.s,case.p)
            if ans == case.output:
                print(f'test passed with {case.s}, {case.p}: output was {ans}')
            else:
                print(f'test FAILED with {case.s}, {case.p}: output was {ans} not {case.output}')

Testing.Test(Testing)