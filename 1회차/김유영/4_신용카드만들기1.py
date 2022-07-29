import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-03/1회차/김유영/_신용카드만들기1.txt")

T = int(input())
for test_case in range(1 ,T+1):
    credit_num = list(map(int, input().split()))
    # print(credit_num)
    credit_num_sum = 0
    for index in range(len(credit_num)):
        if index % 2 != 0:
            num = len(credit_num[index])* 2
            print(index)
            if num >= 10:
                num = str(num)
                credit_num_sum += int(num[0]+num[1])
                # print(num)
            else:
                credit_num_sum += num
        else:
            credit_num_sum += credit_num[index]
            
    

        

