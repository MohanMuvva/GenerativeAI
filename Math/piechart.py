import matplotlib.pyplot as plt

# Data to plot
labels = ['Category A', 'Category B', 'Category C']
sizes = [40, 30, 30]
colors = ['gold', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0)  # explode 1st slice for emphasis

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

plt.title('Pie Chart Example')
plt.show()
"# mohana" 
