def find_short(s):
    nr = 1000
    for ss in (s.split(" ")):
        if len(ss) < nr:
            nr = len(ss) 
    return nr


print(find_short("bitcoin take over the world maybe who knows perhaps"))
