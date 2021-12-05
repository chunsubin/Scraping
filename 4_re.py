import re

# pattern
# 점 (.)  : 하나의 문자를 의미
# ^       : 문자열의 시작
# $ (se$) : 문자열의 끝   ex) case, base
p = re.compile("c.re")  

m = p.match("case")


def print_match(m):
    if m:
        print("m.grpup: ",m.group())
        print("m.string: ",m.string)
        print("m.start: ",m.start())
        print("m.end: ",m.end())
        print("m.span: ",m.span())
    else:
        print("매칭되지 않음")



# search : 주어진 문자열중에 일치하는게 있는지 확인
m = p.search("good care")


print_match(m)