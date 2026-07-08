import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel("Spotify.xlsx")


print(df.head())

print(df.describe())

print(df[['Duration','Popularity']].corr())

print(df.nlargest(5,"Popularity"))

print(df.nsmallest(5,"Popularity"))

plt.plot(df["Track_Name"],df["Popularity"])
plt.xlabel("Track_Name")
plt.ylabel("Popularity")
plt.show()

plt.bar(df["Popularity"],df["Track_Name"])
plt.ylabel("Track_Name")
plt.xlabel("Popularity")
plt.show()

plt.barh(df["Artists_Name"],df["Popularity"])
plt.ylabel("Track_Name")
plt.xlabel("Popularity")
plt.show()

plt.hist(df["Duration"],bins=3)
plt.xlabel("Duration")
plt.ylabel("Bins")
plt.show()

plt.scatter(df["Duration"],df["Popularity"])
plt.xlabel("Duration")
plt.ylabel("Popularity")
plt.show()


plt.figure(figsize=(6,4))
plt.boxplot(df["Popularity"])
plt.title("Popularity Distribution")
plt.ylabel("Popularity")
plt.show()

heat=df[['Duration','Popularity']].corr()
sns.heatmap(heat,annot=True,cmap='coolwarm')
plt.show()
