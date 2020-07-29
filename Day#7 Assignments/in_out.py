Tuple1 = [(1,2,3) , [1,2] , ['a' , 'hit' , 'less']]

t = [a[0] for a in Tuple1]

t1 = [b[1] for b in Tuple1]

t2 = [c[-1] for c in Tuple1]

Tuple2 = t + t1 + t2

print(Tuple2)
