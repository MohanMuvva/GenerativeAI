import pandas as pd

# Example data: colors
colors = ["Red", "Blue", "Green", "Red", "Blue"]

# Creating a categorical variable without any order
colors_cat = pd.Categorical(colors)

# Viewing the categorical data
print(colors_cat)
