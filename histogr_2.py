# %%

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
# %%

cancer_filepath = (r"C:\Users\vitaly.flerin\....\python\sea\cancer.csv")
cancer_data = pd.read_csv(cancer_filepath, index_col = 'Id', )
cancer_data.head(10)

# %%
sns.histplot(data=cancer_data, x='Area (mean)', hue='Diagnosis')
# Add title
plt.title("Histogram of diagnosis")
# %%
# KDE plots for each species
sns.kdeplot(data=cancer_data, x='Radius (worst)', hue='Diagnosis', shade=True)
# %%
