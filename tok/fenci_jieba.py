#! -*- coding:utf-8 -*-
import jieba

f1 = open("test_set\\pc.en.in",'r',encoding='utf-8')
f2 = open('test_set\\am_pc.true.en','w',encoding='utf-8')
lines = f1.readlines()
for line in lines:
    seg_list = jieba.cut(line)
    temp=' '.join(seg_list)
    f2.write(temp)
f2.close()
f1.close()