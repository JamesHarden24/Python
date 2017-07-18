# -*- coding:utf-8 -*-
'''
 1. 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型
    其他类型则报错，并且返回一个偶数列表：(列表里面的元素为偶数)
'''
def get_num(num_list):
	num_list_k = []
	
	if not isinstance(num_list, list):
		return '请输入以list为类型的参数。'
	
	for x in num_list:
		if not isinstance(x, int):
			return '列表里面的元素必须数字类型。'
		elif x % 2 == 0:
			num_list_k.append(x)
	
	return num_list_k

print get_num([1, 2, 3, 5, 6, 8])

assert get_num([1, 2, 5, 6]) == [2, 6]
assert get_num((1, 2, 3, 4)) == "请输入以list为类型的参数。"
assert get_num([1, 'a', 2, 4]) == "列表里面的元素必须数字类型。"

print get_num.__doc__