s = 'один плюс ноль'
ls = s.split(' ')
d1 = {'ноль': 0, 'один': 1, 'двенадцать': 12, 'девятьнадцать': 19}
d_op = {'плюс': lambda x, y: x + y}
i = 0
try:
    e1 = d1[ls[i]]
except KeyError:
    raise NotImplementedError
i += 1
try:
    func = d_op[ls[i]]
except KeyError:
    raise ValueError('ожидался оператор, найдена ересь: "%s"' % ls[i])
i += 1
try:
    e2 = d1[ls[i]]
except KeyError:
    raise NotImplementedError
i += 1
if i != len(ls):
    raise ValueError('найдена ересь: "%s"' % ls[i:])
r = func(e1, e2)
print(r)
