a=10
b=11


_v=vars()
_a=list(_v)
for _b in _a:
    if len(_b)>0:
        if _b[0:1]!="_":
            print(_b)