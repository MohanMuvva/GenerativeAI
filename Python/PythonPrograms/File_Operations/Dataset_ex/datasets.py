import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load the dataset
df = pd.read_csv('C:/Users/ASUS/gen-ai/emails.csv')

# Assuming the last column is the label (1 for spam, 0 for not spam)
labels = df.iloc[:, -1]

# Calculate the total word count for each email
word_counts = df.iloc[:, 1:-1].sum(axis=1)

# Calculate mean and standard deviation
mean = np.mean(word_counts)
std = np.std(word_counts)

# Create a normal distribution
x = np.linspace(mean - 4*std, mean + 4*std, 100)
y = stats.norm.pdf(x, mean, std)

# Plot the histogram and the normal distribution
plt.figure(figsize=(10, 6))
plt.hist(word_counts, bins=50, density=True, alpha=0.7, color='skyblue')
plt.plot(x, y, 'r-', lw=2)
plt.title('Normal Distribution of Word Counts in Emails')
plt.xlabel('Total Word Count')
plt.ylabel('Density')

# Get the name of the column containing word counts
word_count_column = df.columns[df.dtypes == 'int64'][0]  # Assuming word count is an integer column

# Modify the x-axis ticks and labels
max_word_count = df[word_count_column].max()
plt.xticks(range(0, max_word_count + 1, 2000), [f'{x:,}' for x in range(0, max_word_count + 1, 2000)])

# Add text box with mean and std
textstr = f'Mean: {mean:.2f}\nStd Dev: {std:.2f}'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=14,
         verticalalignment='top', bbox=props)

plt.show()

# Print some statistics
print(f"Mean word count: {mean:.2f}")
print(f"Standard deviation of word count: {std:.2f}")
print(f"Number of spam emails: {sum(labels)}")
print(f"Number of non-spam emails: {len(labels) - sum(labels)}")
