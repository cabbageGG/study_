# -*- coding: utf-8 -*-

# 2017/11/9 下午12:31

__author__ = 'li yangjin'




def test():
    print('test')
    do_yield()

def do_yield():
    print ('0000')
    yield '1111'
    print('2222')
test()
print (do_yield())
print (do_yield().__next__())

# for item in do_yield():
#     print (item)


# a=do_yield()
# a.__next__()
# a.__next__()

#conclusion : 含有yield的函数是一个生成器，不能直接调用。
    # 如：do_yield() 这样调用，不会有任何结果，，只会得到一个生成器。
    # 生成器都有一个__next__函数，可以使用这个来进行调用。这样实际上会真正执行函数，函数运行到yield，然后返回yield值。

    # 注：下次运行从yield下一句开始运行。 由于此例子中的生成器访问的是只有一个值的list。 所以它第一次执行到yield '1111'，返回值'1111'。接着第二次调用时，从print '2222'开始，但是已经没有next，故报错StopIteration。

    # 执行下述代码
    # a=do_yield()
    # a.__next__()
    # a.__next__()

    #返回结果
    # Traceback (most recent call last):
    # <generator object do_yield at 0x10cbeb620>
    #   File "/Users/dev/Desktop/python_study/python/scrapytest/scrapy_py3/AticleSpider/AticleSpider/spiders/yield_test.py", line 24, in <module>
    # 0000
    #     a.__next__()
    # 1111
    # StopIteration
    # 0000
    # 2222

if __name__ == '__main__':
    json_data = {'r': 0, 'msg': '登录成功'}
    print(json_data)
    if "msg" in json_data and json_data["msg"] == "登录成功":
        print('login success')
    else:
        print('login fail')
    import re
    url = 'https://www.zhihu.com/question/63029405/answer/258850538'
    match_obj = re.match("(.*zhihu.com/question/(\d+)).*", url)
    print(match_obj.group(0))
    print(match_obj.group(1))
    print(match_obj.group(2))