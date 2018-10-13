import pandas as pd 
import matplotlib.pyplot as plt 

csv = "data/titanic.csv"
df = pd.read_csv(csv)

survived = df.loc[:,'Survived']
classNum = df.loc[:, 'Pclass']

classSurvivalCount = [0,0,0,0,0,0] 
c1Labels = 'class1Alive', 'class1Dead'
c2Labels = 'class2Alive', 'class2Dead'
c3Labels = 'class3Alive', 'class3Dead'


for i in range(len(survived)):
	classNumVal = classNum[i]
	if survived[i] == 1:
		classSurvivalCount[classNumVal-1] += 1
	else:
		classSurvivalCount[classNumVal+2] += 1

fig1, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.pie(classSurvivalCount[:4:3], labels=c1Labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


ax2.pie(classSurvivalCount[1:5:3], labels=c2Labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


ax3.pie(classSurvivalCount[2::3], labels=c3Labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('results/titanic_vis.png')
plt.show()
