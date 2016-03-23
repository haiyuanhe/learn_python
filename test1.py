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
dic = {'1':'lala','2':'hahah'}
print dic['1']

#直接能够插入. 爽 .
dic[3]='233'
print dic

#in 的用法返回bool 类型
print '1' in dic
print 'lala' in dic 

#通过get 实现 
print dic.get('1')
#同时能够直接赋予非空的值. 
print dic.get('none','none');

#key是不能变的.hash 变了就难找了. 
set= set([1,1,1,13,2,4,5,2])
print set
set.add(124)
print set


#字符串的不可变性. 都是在内存中直接新创建.
#replace 的例子. 
str = 'hehaiyuan'
print str.replace('a','?')
print str