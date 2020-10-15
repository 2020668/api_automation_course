# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/8/28

E-mail:keen2020@outlook.com

=================================


"""

import openpyxl


class Case(object):
    # 用这个类来存储用例
    def __init__(self, attrs=None):
        """
        初始化用例
        :param attrs: zip类型--> [（key1,value1),（key2,value2)....]
        """
        for item in attrs:
            setattr(self, item[0], item[1])


class ExcelLibrary(object):
    ROBOT_LIBRARY_VERSION = 1.0

    # 必须要写默认值 给None也行
    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name

    def keyword(self):
        pass

    def read_excel_by_id(self, id):

        self.wb = openpyxl.load_workbook(self.file_path)  # 打开工作簿，传入的指定文件名
        self.sheet = self.wb[self.sheet_name]  # 选取表单，传入的指定表单

        rows_data = list(self.sheet.rows)

        titles = []
        for title in rows_data[0]:
            if title.value:
                titles.append(title.value)

        for case in rows_data[1:]:
            data = []
            for cell in case:
                data.append(cell.value)
            case_data = zip(titles, data)
            case_obj = Case(case_data)
            if case_obj.case_id == id:
                break
        self.wb.close()
        return case_obj



if __name__ == '__main__':
    import os
    from common.constant import DATA_DIR
    file_path = os.path.join(DATA_DIR, 'api_automation_course.xlsx')
    print(file_path)
    wb = ExcelLibrary(file_path, 'login')
    data = wb.read_excel_by_id(1)
    print(data.title)
