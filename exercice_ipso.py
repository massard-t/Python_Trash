#!/usr/bin/python3
import sys


def RequestedList(Curr_list):
    if (len(Curr_list) == 0) or (len(Curr_list) > 100):
        print("0 < L <= 100")
        return False
    if (min(Curr_list) < 0) or (max(Curr_list) >= 100):
        print("0 <= N < 100")
        return False
    q, r = divmod(sum(Curr_list), len(Curr_list))
    if r != 0:
        return False
    return q


def MoveOne(Curr_list, Objective):
    for i in range(0, len(Curr_list)-1):
        if Curr_list[i+1] > Objective:
            Curr_list[i+1] = Curr_list[i+1] - 1
            Curr_list[i] = Curr_list[i] + 1
        elif Curr_list[i+1] < Objective:
            Curr_list[i] = Curr_list[i] - 1
            Curr_list[i+1] = Curr_list[i+1] + 1
        elif Curr_list[i] > Objective:
            Curr_list[i] = Curr_list[i] - 1
            Curr_list[i+1] = Curr_list[i+1] + 1
        elif Curr_list[i] < Objective:
            Curr_list[i+1] = Curr_list[i+1] - 1
            Curr_list[i] = Curr_list[i] + 1
    return (Curr_list)


def ListIterate(Base_list):
    Objective = RequestedList(Base_list)
    if Objective is False:
        print(-1)
        return (1)
    Curr_list = Base_list
    ObjectiveList = [Objective] * len(Curr_list)
    count = AffList(0, Curr_list)
    while Curr_list != ObjectiveList:
        Curr_list = MoveOne(Curr_list, Objective)
        count = AffList(count, Curr_list)
    return (0)


def AffList(count, Curr_list):
    print(count, " : ", end="")
    print(*Curr_list)
    return (count + 1)


def main():
    if len(sys.argv) != 2:
        print("Missing parameter")
        return (1)
    StringList = sys.argv[1]
    StringList = StringList.split()
    IntList = [int(ele) for ele in StringList]
    return (ListIterate(IntList))


if __name__ == '__main__':
    main()
