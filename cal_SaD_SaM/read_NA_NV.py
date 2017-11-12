#!/usr/bin/env python3
import sys

''' ----------------------------------------------------------------------------
1. 輸入斷層的位置以及距離即可以得到NA and NV
2. NA and NV包含了, dNA, dNV, mNA and mNV.
3. 程式的想法是用if來先行判斷距離的多少, 再用斷層區域來做進一步的判定其因子為多少.
---------------------------------------------------------------------------- '''

print("\t1. 近車籠埔斷層調整因子 N A 與 NV\n \
       2. 近獅潭與神卓山斷層調整因子 N A 與 NV\n \
       3. 近屯子腳斷層調整因子 N A 與 NV\n \
       4. 近梅山斷層調整因子 N A 與 NV\n \
       5. 近新化斷層調整因子 N A 與 NV\n \
       6. 近大尖山與觸口斷層調整因子 N kA 與 NV\n \
       7. 近花東地區斷層(含米崙、玉里、池上與奇美斷層)調整因子 N A 與 NV")

fault_zone = input("input fault zone, 1 ~ 7:")

if int(fault_zone) > 7:
    print("inputing item is out of range!!")
    exit()

r_distance = input("input distance, ex:2 (km):")

if float(r_distance) <= 2:
    if int(fault_zone) == 1:
        dNA = 1.23
        dNV = 1.36

        mNA = 1.25
        mNV = 1.5
    elif int(fault_zone) == 2:
        dNA = 1.28
        dNV = 1.33

        mNA = 1.26
        mNV = 1.42
    elif int(fault_zone) == 3:
        dNA = 1.28
        dNV = 1.31

        mNA = 1.26
        mNV = 1.42
    elif int(fault_zone) == 4:
        dNA = 1.37
        dNV = 1.44

        mNA = 1.3
        mNV = 1.48
    elif int(fault_zone) == 5:
        dNA = 1.23
        dNV = 1.15

        mNA = 1.29
        mNV = 1.3
    elif int(fault_zone) == 6:
        dNA = 1.15
        dNV = 1.15

        mNA = 1.21
        mNV = 1.42
    else:# int(fault_zone) == 7:
        dNA = 1.42
        dNV = 1.58

        mNA = 1.32
        mNV = 1.58
 
elif 2 < float(r_distance) <= 5:
    if int(fault_zone) == 1:
        dNA = 1.16
        dNV = 1.32

        mNA = 1.2
        mNV = 1.45
    elif int(fault_zone) == 2:
        dNA = 1.2
        dNV = 1.27

        mNA = 1.18
        mNV = 1.32
    elif int(fault_zone) == 3:
        dNA = 1.2
        dNV = 1.25

        mNA = 1.17
        mNV = 1.32
    elif int(fault_zone) == 4:
        dNA = 1.28
        dNV = 1.36

        mNA = 1.2
        mNV = 1.36
    elif int(fault_zone) == 5:
        dNA = 1.06
        dNV = 1.05

        mNA = 1.1
        mNV = 1.15
    elif int(fault_zone) == 6:
        dNA = 1.08
        dNV = 1.1

        mNA = 1.17
        mNV = 1.35
    else:# int(fault_zone) == 7:
        dNA = 1.37
        dNV = 1.53

        mNA = 1.26
        mNV = 1.48
 
elif 5 < float(r_distance) <= 8:
    if int(fault_zone) == 1:
        dNA = 1.07
        dNV = 1.22

        mNA = 1.1
        mNV = 1.3
    elif int(fault_zone) == 2:
        dNA = 1.1
        dNV = 1.1

        mNA = 1.05
        mNV = 1.15
    elif int(fault_zone) == 3:
        dNA = 1.1
        dNV = 1.15

        mNA = 1.05
        mNV = 1.15
 
    elif int(fault_zone) == 4:
        dNA = 1.15
        dNV = 1.2

        mNA = 1.05
        mNV = 1.15
    elif int(fault_zone) == 5:
        dNA = 1
        dNV = 1

        mNA = 1
        mNV = 1
    elif int(fault_zone) == 6:
        dNA = 1
        dNV = 1.03

        mNA = 1.05
        mNV = 1.15
    else:# int(fault_zone) == 7:
        dNA = 1.28
        dNV = 1.38

        mNA = 1.1
        mNV = 1.3

elif 8 < float(r_distance) <= 10:
    if int(fault_zone) == 1:
        dNA = 1.03
        dNV = 1.1

        mNA = 1.03
        mNV = 1.15
    elif int(fault_zone) == 2:
        dNA = 1
        dNV = 1

        mNA = 1
        mNV = 1
    elif int(fault_zone) == 3:
        dNA = 1.1
        dNV = 1.15

        mNA = 1.05
        mNV = 1.15
    elif int(fault_zone) == 4 or int(fault_zone) == 5 or int(fault_zone) == 6:
        dNA = 1
        dNV = 1

        mNA = 1
        mNV = 1
    else:# int(fault_zone) == 7:
        dNA = 1.14
        dNV = 1.2

        mNA = 1.02
        mNV = 1.16
 
elif 10 < float(r_distance) <= 12:
    if int(fault_zone) == 1:
        dNA = 1.03
        dNV = 1.1

        mNA = 1.03
        mNV = 1.15
    elif int(fault_zone) == 2 or int(fault_zone) == 3 or int(fault_zone) == 4 or int(fault_zone) == 5 or int(fault_zone) == 6:
        dNA = 1
        dNV = 1

        mNA = 1
        mNV = 1
    else:# int(fault_zone) == 7:
        dNA = 1.14
        dNV = 1.2

        mNA = 1.02
        mNV = 1.16
 
elif 12 < float(r_distance) <= 15:
    if int(fault_zone) == 1 or int(fault_zone) == 2 or int(fault_zone) == 3 or int(fault_zone) == 4 or int(fault_zone) == 5 or int(fault_zone) == 6:
        dNA = 1
        dNV = 1

        mNA = 1
        mNV = 1
    else:# int(fault_zone) == 7:
        dNA = 1
        dNV = 1

        mNA = 1
        mNV = 1.05
 
elif float(r_distance) > 15:
    if int(fault_zone) == 1 or int(fault_zone) == 2 or int(fault_zone) == 3 or\
            int(fault_zone) == 4 or int(fault_zone) == 5 or int(fault_zone) == 6 or int(fault_zone) == 7:
        dNA = 1
        dNV = 1

        mNA = 1
        mNV = 1
else:
    print("the distance is out of range!!")

print("dNA: ", dNA)
print("dNV: ", dNV)
print("mNA: ", mNA)
print("mNV: ", mNV)
