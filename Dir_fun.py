def Fun(*args):
    print('输入的设定参数：{}'.format(args))
    T = {args.index(k)+1 : k for k in args}
    return T
r = Fun('hu','英','hui')
print('输出为字典形式：{}'.format(r))
