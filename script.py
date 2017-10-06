# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import xlrd
from sklearn import tree
from sklearn.tree import export_graphviz
import pydotplus as plus


dimensions=[[0 for col in range(0,8)] for row in range(0,100)]
classes=[[0 for col in range(0,9)]for row in range(0,100)]


wb=xlrd.open_workbook(".\\workbook_1.xlsx")
ws_1=wb.sheets()[1]
ws_2=wb.sheets()[2]
for i in range(0,100):
    for j in range(0,8):
        dimensions[i][j]=ws_1.cell_value(i,j)

for i in range(0,100):
    for j in range(0,9):
        classes[i][j]=ws_2.cell_value(i,j)

depth=0
k='z'
while len(k)!=1 or k<'a' or k>'i' :
    print("This script file analyzes the relationship between the biological traits and economic value of different varieties of rice through the regression tree algorithm based on the data in workbook_1.xlsx")
    k=input("please input a~i, each of which corresponds to 'brown rice rate', 'milled rice rate', 'head rice rate','chalkiness rate', 'chalkiness', 'adhesiveness of rice starch','percentage of amylose', 'full growth peroid', 'yield'\n")

idx=['brown rice rate','milled rice rate','head rice rate','chalkiness rate','chalkiness','adhesiveness of rice starch','percentage of amylose','full growth period','yield'] 
while int(depth)<=2 or int(depth)>8:
    depth=input("Please input the maximum depth of regression tree, from 2 to 8: ")
    if len(depth)!=1:
        continue

corr={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}
rgr=tree.DecisionTreeRegressor(max_depth=int(depth)).fit(dimensions,[x[corr[k]] for x in classes])

dot_data=export_graphviz(rgr,out_file=None)
graph=plus.graph_from_dot_data(dot_data)
graph.write_pdf(str(idx[corr[k]])+" regression tree(max_depth="+depth+").pdf")




