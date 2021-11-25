#accountTypeSpider
#autor:Jade
#创建日期:2020/9/9
#-*- coding:utf-8 -*-

import xlrd,os
import getVerifyInfo
from xlutils.copy import copy
import time

def getTypeInFile(location):
    workbook = xlrd.open_workbook(location)
    wb = copy(workbook)
    sheet = workbook.sheet_by_index(0)
    st = wb.get_sheet(0)
    rowCount = sheet.nrows
    for i in range(1, rowCount):
        user_name = sheet.cell(i, 0).value
        V_icon = getVerifyInfo.get_V_info(user_name)
        # if str(V_icon)=="":
        #     st.write(i, 1, "无")
        # else:
        st.write(i, 1, V_icon)

        time.sleep(1)

    os.remove(location)
    wb.save(location)
