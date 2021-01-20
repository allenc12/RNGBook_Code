#!/usr/bin/env python32

count_table = [0 for x in range(256)]
pattern_table = [0 for x in range(256)]

dis_count_table = [0 for x in range(256)]
dis_pattern_table = [0 for x in range(256)]

for i in range(256):
    abyte = i
    count = 0
    pattern = 0
    dis_count = 0
    dis_pattern = 0
    for j in range(4):
        pair = abyte & 0x03
        abyte = abyte >> 2
        if pair == 1:  # 01 case
            pattern = (pattern << 1) | 0x01
            count = count + 1
        elif pair == 2:  # 10 case
            pattern = pattern << 1
            count = count + 1
        elif pair == 0:  # 00 case
            dis_pattern = dis_pattern << 1
            dis_count = dis_count + 1
        elif pair == 3:  # 11 case
            dis_pattern = (dis_pattern << 1) | 0x01
            dis_count = dis_count + 1
    count_table[i] = count
    pattern_table[i] = pattern
    dis_count_table[i] = dis_count
    dis_pattern_table[i] = dis_pattern

print("Pattern Table")
for y in range(16):
    line = pattern_table[y * 16 : (y * 16) + 16]
    linelist = [("0x%02x" % x) for x in line]
    # for x in line:
    #    linelist.append("0x%02x" % x
    line = ",".join(linelist)
    print(line)

print("Count Table")
for y in range(16):
    line = count_table[y * 16 : (y * 16) + 16]
    linelist = [("%d" % x) for x in line]
    line = ",".join(linelist)
    print(line)

print("Discard Pattern Table")
for y in range(16):
    line = dis_pattern_table[y * 16 : (y * 16) + 16]
    linelist = [("0x%02x" % x) for x in line]
    line = ",".join(linelist)
    print(line)

print("Discard Count Table")
for y in range(16):
    line = dis_count_table[y * 16 : (y * 16) + 16]
    linelist = [("%d" % x) for x in line]
    line = ",".join(linelist)
    print(line)
