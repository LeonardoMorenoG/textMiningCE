import pandas as pd
import seaborn as sns
import numpy as np

def getPapersHavingKeyword(matrix,keyword):
	return list(matrix[matrix[keyword]>0].index.values)

def getIntersection(col1,col2):
	return len(set(col1)&set(col2))

kc = pd.read_csv("keywordCount.normalized.csv",header=0,index_col=0,sep=';') #kc:= keywords count table

co_ocurrence = pd.DataFrame(data=0.0,columns=kc.columns.values,index=kc.columns.values)

for x in kc.columns.values:
	for y in kc.columns.values:
		p_x = getPapersHavingKeyword(kc,x)
		p_y = getPapersHavingKeyword(kc,y)
		e_xy = getIntersection(p_x,p_y)
		n_x = len(p_x)
		n_y = len(p_y)
		co_ocurrence[y][x] = e_xy**2/(n_x*n_y)

co_ocurrence.to_csv("co-occurrence.csv",header=True,index=True,sep='\t')

ax = sns.clustermap(co_ocurrence,annot=True,cmap="Blues")
ax.ax_row_dendrogram.set_visible(False)
ax.ax_col_dendrogram.set_visible(False)
ax.savefig("co-occurrence.blues.pdf")

