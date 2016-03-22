#! /usr/bin/env python
#coding=utf-8





#数组部分:
#声明一个数组:
array = [1,2,2,3]
print len(array)
print array
#如果超过len-1 会抛出index out of range:
#另外-1指最后一个下标值得元素. -2 就是倒数第二个:
print array[-4]

#append 方法 在末尾追加一个.
array.append("abdc")
print array
#pop 方法 删除末尾的元素:
array.pop()
print array


#insert 方法, 在指定的位置插入.
array.insert(1,"ace")
print array

#pop 也可以删除指定元素
array.pop(1)
print array

doubleMArray = [1,2,3,array]
print doubleMArray
#直接访问二维数组, cool
print doubleMArray[3][1]

#tuple 部分
#主要特征是声明之后的指针就不能改变了. 这个有点像final
tupleT = (1,doubleMArray)
print tupleT
tupleT[1][1] = "aa";
print tupleT


#逻辑控制. 
print "------------------"
print 'logic control'

sum = 0;
for x in range(101):
    sum = sum + x
print sum

#dic 和set
#直接定义没有任何学习成本.
