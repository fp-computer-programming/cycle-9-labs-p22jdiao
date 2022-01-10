# Author: JD 01/10/2021

def double_stuff(item):
    
    for i, v in enumerate(item):
        item[i] = v*2

    return item

def test_case():
    l1 = [1,2,3,4,5]
    l2 = [0, 1, 1.1, 2.4, 5, 7.8]
    l3 = ["yes", 12, 13, 5.2, 7.5, "wow"]
    print(double_stuff(l1) == [2,4,6,8,10])
    print(double_stuff(l2) == [0,2,2.2,4.8,10,15.6])
    print(double_stuff(l3) == ["yesyes", 24,26,10.4,15,"wowwow"])

test_case()