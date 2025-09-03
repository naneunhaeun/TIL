# 1, 2, 3 으로 순열 만들기

for i1 in [1, 2, 3]:
    for i2 in [1, 2, 3]:
        if i1 != i2:
            for i3 in [1, 2, 3]:
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3) 
                    # 1 2 3
                    # 1 3 2
                    # 2 1 3
                    # 2 3 1
                    # 3 1 2
                    # 3 2 1