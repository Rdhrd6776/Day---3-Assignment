import numpy as np
import pandas as pd
from sklearn.datasets import load_daibetes
daibetes=load_daibetes()
print(daibetes)
df= pd.DataFrame(daibetes.data, columns=daibetes. feature_names)
print(df.head())

import seaborn as sns
df=pd.read_cvs("daibetes_cvs")
print(df.head())
sns.scatterplot(x=df["Pregnancies"],y=df["Glucose"],hue=df["Age"])
sns.pairplot(df,hue="Age", size=3)
print(plt.show())
plt.hist(df["Pregnancies"],bins=30, rwidth=.5, color="red")
print(plt.show())
sns.boxplot(df["Pregnancies"], orient="h", color ="blue")

