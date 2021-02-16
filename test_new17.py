class multifilter:
    def judge_half(pos, neg):
        return True if pos >= neg else False

    def judge_any(pos, neg):
        return True if pos >= 1 else False

    def judge_all(pos, neg):
        return True if neg == 0 else False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iter = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for i in self.iter:
            pos, neg = 0, 0 
            for f in self.funcs: 
                if f(i):
                    pos += 1
                else:
                    neg += 1

            if(self.judge(pos, neg)):
                yield i
            

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)]

print(list(multifilter(a, mul2, mul3, mul5))) 
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 



