# %%

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
# %%
# Path of the file to read
candy_filepath = (r"C:\Users\....n\Desktop\python\sea\candy.csv")
# %%
# Read the file into a variable insurance_data
candy_data = pd.read_csv(candy_filepath, index_col = 'id')  ##sep = ';'
# %%
candy_data.head()
# %%
sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])
# %%
sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])
# %%
sns.scatterplot(x=candy_data['pricepercent'], y=candy_data['winpercent'], hue=candy_data['chocolate'])  
# %%
sns.lmplot(x="pricepercent", y="winpercent", hue="chocolate", data=candy_data)
# %%
sns.swarmplot(x=candy_data['chocolate'],
              y=candy_data['winpercent'])
# %%
