
# %%
import pandas as pd
pd.read_excel(r'C:\Users\vitaly.flerin\Desktop\test.xlsx')
# %%
import seaborn as sns
import matplotlib.pyplot as plt
# read a titanic.csv file
# from seaborn libraray
df = pd.read_excel(r'C:\Users\vitaly.flerin\Desktop\test.xlsx')
# class v / s fare barplot
sns.barplot(x = "kog_ wifi", y = "nps", ci=None, data = df)
# Show the plot
plt.show()
# %%
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel(r'C:\Users\vitaly.flerin\Desktop\test.xlsx')
sns.set_style("darkgrid")
sns.lineplot(data=df, x="kog_ wifi", y="gb")
plt.show()
# %%










import pandas as pd
pd.read_excel(r'C:\Users\vitaly.flerin\Desktop\test.xlsx')
# %%
import seaborn as sns
import matplotlib.pyplot as plt
 # read a titanic.csv file
# from seaborn libraray
df = pd.read_excel(r'C:\Users\vitaly.flerin\Desktop\test.xlsx')
# class v / s fare barplot
sns.barplot(x = "kog_ wifi", y = "nps", ci=None, data = df)
# Show the plot
plt.show()
# %%
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel(r'C:\Users\vitaly.flerin\Desktop\test.xlsx')
sns.set_style("darkgrid")
sns.lineplot(data=df, x="kog_ wifi", y="gb")
plt.show()
# %%
pd.pivot_table(df,
index = ['bucket_num'],
columns = ['report_month'],
values = 'gb',
aggfunc = 'mean')
# %%
df.plot(x = 'region_id', y = 'gb')
# %%
df.plot.hist(x = 'region_id', y = 'gb')
# %%
df.to_csv('WHR_2019.csv')
# %%
