# coding:utf-8
'''
8 kyu
Beginner Series #2 Clock
Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to miliseconds.

#####Example:

past(0, 1, 1) == 61000

Note! h, m and s will be only Natural numbers! Waiting for translations and Feedback! Thanks!
'''
# 兼顾性能，直接乘法太慢了，在codewars无法提交，str与int转换提升一些性能
def past(h, m, s):
    # Good Luck!
    res=int(str(h*36)+'00000')+int(str(m*6)+'0000')+int(str(s)+'000')
    return res