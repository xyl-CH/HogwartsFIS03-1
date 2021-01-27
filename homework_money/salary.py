#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
"""

saved_money = 1000

# 位置参数salary为发放的工资金额
def send_money(salary):
    global saved_money
    print(f"您发工资前的存款为：{saved_money}")
    saved_money += salary
    print(f"您现在的存款为：{saved_money}")

# 位置参数salary为发放的工资金额
def select_money(salary):
    print(f"此次发放工资为：{salary}")


if __name__ == '__main__':
    send_money(1000)
    select_money(1000)
