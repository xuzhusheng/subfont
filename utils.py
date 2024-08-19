from itertools import groupby

def string_to_unicode_ranges(s):
    l = list(set(s))
    codes = list(map(ord, l))
    codes.sort()

    groups = []
    for _, g in groupby(enumerate(codes), lambda x: x[0] - x[1]):
        groups.append([v for _, v in g])

    ranges = []
    for g in groups:
        if len(g) == 1:
            ranges.append(f"U+{g[0]:X}")
        else:
            ranges.append(f"U+{g[0]:X}-{g[-1]:X}")
    return ",".join(ranges)
