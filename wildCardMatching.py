
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if set(p) == {"*"}: # when p = "*", "**", "***", etc
            return True

        if (len(s) > len(p)) and "*" not in p:
            return False

        if len(s) == 0: #recursive exit
            if len(p) > 0:
                return False
            return True


        if p[0] == "*":
            if p[1] == "*" or p[1] == "?" and (len(s) < len(p)):
                return Solution.isMatch(self, s, p[1::])
            if p[1] == "*":
                return Solution.isMatch(self,s[s.rfind(p[1])::], p[1::])
            if p[1] in s:
                temp = ""
                for i in range(1,len(p)):
                    if p[i] != "?" and p[i] != "*":
                        temp += p[i]
                    else:
                        return Solution.isMatch(self, s[s.rfind(temp)::], p[1::])
                return Solution.isMatch(self, s[s.rfind(temp)::], p[1::])
            if p[1] == "?" and p[-1] == "?":
                return Solution.isMatch(self, s[1::], p[1::])
            if p[1] not in s and p[1] != "?":
                return False
            return Solution.isMatch(self,s[1::],p[2::])

        if s[0] == p[0] or p[0] == "?":
            return Solution.isMatch(self, s[1::], p[1::])

        return False




class Testing:

    from dataclasses import dataclass

    @dataclass
    class Case:
        s: str
        p: str
        output: bool

    cases = [Case("aa", "a", False), Case("aa", "*", True), Case("cb", "?a", False), Case("abceb","*a*b",True), Case("acdcb","a*c?b",False), Case("", "******", True), Case("ab","*?*?*", True), Case("hi","*?",True), Case("b","*a*",False), Case("aaaa","***a",True), Case("ho","**ho",True), Case("abce","abc*?",True), Case("mississippi","m*iss*",True), Case("adceb","*a*b",True),Case("mississippi","m*iss*iss*",True),Case("abcabczzzde","*abc???de*",True)]
    #cases = [cases[-1]]
    print(len(cases))

    def Test(self, cases=cases):
        for case in cases:
            ans = Solution.isMatch(Solution,case.s,case.p)
            if ans == case.output:
                print(f'test passed with {case.s}, {case.p}: output was {ans}')
            else:
                print(f'test FAILED with {case.s}, {case.p}: output was {ans} not {case.output}')

Testing.Test(Testing)
