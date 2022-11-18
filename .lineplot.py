# %%

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")



# %%
# Path of the file to read
spotify_filepath = r"C:\Users\.....\Desktop\spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)
# %%
spotify_data
# %%
# Line chart 
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)
# %%

# Change the style of the figure to the "dark" theme
#(1)"darkgrid", (2)"whitegrid", (3)"dark", (4)"white", and (5)"ticks"
sns.set_style("whitegrid") 
# Line chart 
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)

# %%
