import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('/Users/gurpartapsohal/Desktop/President Heights/president_heights.csv')
df = pd.DataFrame(data)
#print(data.head(5))
#print(data.columns[1])

height = np.array(data["height(cm)"])
#print(height)
print("Average height (cm) :", np.mean(height))
print("Height Standard Deviation (cm) :", np.std(height))
print("Maximum recorded height (cm) :", np.max(height))
print("Smallest recorded height (cm) :", np.min(height))
sns.set()

plt.boxplot(height, vert=False)
plt.title('Presedential Height Box and Whisker plot')
# Adds x axis label
plt.xlabel('')
# Adds y axis label
plt.ylabel('Height (cm)')
plt.show()

plt.hist(height)
plt.title('Presidential Height')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.show()