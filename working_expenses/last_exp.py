import pandas as pd
import xlwings as xw
import datetime

book = xw.Book('expenses.xlsx')
shit=book.sheets('Sheet1')

now = datetime.datetime.now()
time = now.strftime("%d %m %y")

reference = 0
totality = 0
x = 0
main_frame = pd.read_excel('expenses.xlsx',name='Sheet1')

item = []
money = []
j = int(input("Enter the number of expenditures"))
for iter in range(j):
    item.append(str(input("Enter the expenditure")))
    money.append(int(input("Enter the money lost")))

Date = list(main_frame['Date'])
total = list(main_frame['Total'])
describe1 = list(main_frame['Description'])
des1 = []
cost1 = []
cost2 = []
total1 = []
cost = list(main_frame['Cost'])
sum1 = 0
sum2 = 0

def printing():
    shit.range('A' + str(len(Date) + 2)).value = time
    shit.range('C' + str(len(describe1) + 2)).options(transpose=True).value = item
    shit.range('B' + str(len(cost) + 2)).options(transpose=True).value = money

def list_cut(list,i):
    fin_list = list[i:]
    return fin_list

def list_sum(list):
    y = 0
    for i in range(len(list)):
        y = y + list[i]
    return y


if len(Date):
    for iter in range(len(Date)):
        if time in Date:
            if Date[iter] == time:
                des1 = list_cut(describe1,iter)
                cost1 = list_cut(cost,iter)
                totality = list_sum(cost1)
                reference = iter
                break
        else:
            printing()
            sum1 = list_sum(money)
            print(sum1)
            shit.range('D' + str(len(describe1) + 2)).value = sum1
            break
else:
    printing()
    sum2 = list_sum(money)
    print(sum2)
    shit.range('D' + str(2)).value = sum2
"""
if des in des1:
        if des1[iter] == des:
        """

for iter in range(len(des1)):
    for iter1 in range(len(item)):
        if item[iter1] in des1:
            if item[iter1] == des1[iter]:
                cost1[iter] = cost1[iter] + money[iter1]
                shit.range('B' + str(reference + iter + 2)).value = cost1[iter]
        else:
            shit.range('C' + str(len(describe1) + 2)).value = item[iter1]
            shit.range('B' + str(len(cost) + 2)).value = money[iter1]


"""
for iter in range(len(Date)):
    if time in Date:
            if Date[iter] == time:
                cost2 = list_cut(cost,iter)
                total2 =list_cut(total,iter)
                totality = iter

sum = 0
for i in range(len(cost2)):
    sum = sum + cost2[i] + x

"""

totality = totality + list_sum(money)
print(totality)
shit.range('D' + str(reference + 2)).value = totality


"""
totality = sum1 + list_sum(money)
print(totality)
shit.range('D' + str(reference + 2)).value = totality
"""


book.save()



