# -*- coding:utf-8 -*-
'''
 1. ����һ������get_num(num),num�������б����ͣ��ж��б������Ԫ��Ϊ��������
    ���������򱨴����ҷ���һ��ż���б�(�б������Ԫ��Ϊż��)
'''
def get_num(num_list):
	num_list_k = []
	
	if not isinstance(num_list, list):
		return '��������listΪ���͵Ĳ�����'
	
	for x in num_list:
		if not isinstance(x, int):
			return '�б������Ԫ�ر����������͡�'
		elif x % 2 == 0:
			num_list_k.append(x)
	
	return num_list_k

print get_num([1, 2, 3, 5, 6, 8])

assert get_num([1, 2, 5, 6]) == [2, 6]
assert get_num((1, 2, 3, 4)) == "��������listΪ���͵Ĳ�����"
assert get_num([1, 'a', 2, 4]) == "�б������Ԫ�ر����������͡�"

print get_num.__doc__