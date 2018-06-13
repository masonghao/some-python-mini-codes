# a = [[x for x in range(y, y+4)] for y in range(16) if y%4==0]
# print('a = %s' % str(a))
# b = [[x for x in range(y, y+4)] for y in range(16, 32) if y%4==0]
# print('b = %s' % str(b))
import time, threading, sys

result = 0 # 定义全局变量，线程通信共享

# 计算整数区间的和（不包含ends值）
# 参数（开始数值，结束数值）
def numadds(starts, ends):
    a = 0
    for x in range(starts, ends):
        a += x
    global result
    print('result is %d, %d--%d is %d' % (result, starts, ends-1, a))
    result += a
    time.sleep(1)

# 大区间拆分小区间分线程处理累加
# 参数（调用的函数，开始数字，结束数字，线程数目）
def chaifenqi(funs, starts, ends, counts):
    lens = ends-starts # 计算作业长度
    nums = lens/counts # 计算单份作业长度
    nums = int(nums) # 转化整数
    base = starts #定义迭代起始，开始分线执行

    # 线程预装载
    threadarr = []
    for x in range(counts):
        base2 = base+nums
        
        threads = myThread(counts, funs, base, base2)
        threadarr.append(threads)
        base = base2
    else:
        if base < ends:
            threads = myThread(counts+1, funs, base, ends)
            threadarr.append(threads)

    # 线程执行等待开启
    for x in threadarr:
        res = x.start()

    # 等待所有线程执行结束
    for t in threadarr:
        t.join()

    print('Exit main threadarr')

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, func, *param):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.func = func
        self.param = param
    # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
    def run(self):
        return self.func(*self.param)

if __name__ == '__main__':
    # 计算累加值 1到100的和
    startnum = 1
    endnum = 100
    count = 50   # 希望拆分线程数量
    chaifenqi(numadds, startnum-1, endnum+1, count)

    print('---result is %d' % result)
