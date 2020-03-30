'''
描述
round() 方法返回浮点数x的四舍五入值。

语法
以下是 round() 方法的语法:
round( x [, n]  )

参数
x -- 数字表达式。
n -- 表示从小数点位数，其中 x 需要四舍五入，默认值为 0。

返回值
返回浮点数x的四舍五入值。
'''

print ("round(70.23456) : ", round(70.23456))
print ("round(56.659,1) : ", round(56.659,1))
print ("round(80.264, 2) : ", round(80.264, 2))
print ("round(100.000056, 3) : ", round(100.000056, 3))
print ("round(-100.000056, 3) : ", round(-100.000056, 3))

'''
输出结果...
round(70.23456) :  70
round(56.659,1) :  56.7
round(80.264, 2) :  80.26
round(100.000056, 3) :  100.0
round(-100.000056, 3) :  -100.0
'''