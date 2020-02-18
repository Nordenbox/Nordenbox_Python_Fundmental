import time

time_start = time.time()
for x1 in range(1, 10):
    loops = 0
    for x2 in range(1, 10):
        for x3 in range(1, 10):
            for y1 in range(1, 10):
                for y2 in range(1, 10):
                    for y3 in range(1, 10):
                        for z1 in range(1, 10):
                            for z2 in range(1, 10):
                                for z3 in range(1, 10):

                                    judge_list = [x1, x2, x3, y1, y2, y3, z1, z2, z3]

                                    row1 = x1 + x2 + x3
                                    row2 = y1 + y2 + y3
                                    row3 = z1 + z2 + z3
                                    column1 = x1 + y1 + z1
                                    column2 = x2 + y2 + z2
                                    column3 = x3 + y3 + z3
                                    diagonal1 = x1 + y2 + z3
                                    diagonal2 = x3 + y2 + z1

                                    print("%d+%d+%d=%d" % (x1, x2, x3, row1))
                                    print("%d+%d+%d=%d" % (y1, y2, y3, row2))
                                    print("%d+%d+%d=%d" % (z1, z2, z3, row3))
                                    print("------")
                                    loops += 1

                                    if (
                                        row1 == 15
                                        and row2 == 15
                                        and row3 == 15
                                        and column1 == 15
                                        and column2 == 15
                                        and column3 == 15
                                        and diagonal1 == 15
                                        and diagonal2 == 15
                                        and len(judge_list) == len(set(judge_list))
                                    ):
                                        print("OK!!!!!!计算", loops, "次数之后，生成幻方如下：")
                                        print(x1, "|", x2, "|", x3)
                                        print("---------")
                                        print(y1, "|", y2, "|", y3)
                                        print("---------")
                                        print(z1, "|", z2, "|", z3)
                                        time_end = time.time()
                                        print("消耗时间", round(time_end - time_start), "秒")
                                        a = False
                                        exit()
