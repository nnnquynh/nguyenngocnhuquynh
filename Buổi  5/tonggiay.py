# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:36:37 2024

@author: NguyenNgocNhuQuynh-23711751
"""

gio=int(input("Nhập giờ: "))
phut=int(input("Nhập phút: "))
giay=int(input("Nhập giây: "))
if 0<=gio<23 and 0<=phut<60 and 0<=giay<60:
    tonggiay=3600*gio+60*phut+giay
    print("Tổng giây là: ",tonggiay)