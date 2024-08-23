# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:32:19 2024

@author: NguyenNgocNhuQuynh-23711751
"""
import math

a=float(input("Nhập a: " ))
b=float(input("Nhập b: "))
bt1=math.sqrt(a)-math.sqrt(b)
bt2=a**(1/4)-b**(1/4)
bt3=math.sqrt(a)+(a*b)**(1/4)
bt4=a**(1/4)+b**(1/4)

ketqua=(bt1/bt2)-(bt3/bt4)
print("Kết quả của biểu thức là: ",ketqua)
