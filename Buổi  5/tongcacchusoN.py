# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:36:37 2024

@author: NguyenNgocNhuQuynh-23711751
"""

N=int(input("Nhập vào số nguyên dương có 2 chữ số: "))
if 10<=N<=99:
    hangchuc=N//10
    hangdonvi=N%10
    tong=hangchuc+hangdonvi
    print("Tổng các chữ số của N là: ",tong)