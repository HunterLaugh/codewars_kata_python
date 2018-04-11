# coding:utf-8

import os

def file_name(file_dir):
	L=[]
	for root,dirs,files in os.walk(file_dir):
		print(root)  #当前目录路径
		print(dirs)	 #当前路径下所有子目录
		print(files) # 当前路径下所有非目录子文件
	
file_name(os.getcwd())		 # os.getcwd()获取当前路径		
				
				