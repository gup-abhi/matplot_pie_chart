# importing matplotlib module for plotting
import matplotlib.pyplot as plt

# creating list of percent
percent = [78, 22, 3]
# creating list of colours
colour = ['blue', 'green', 'red']
# creating list of names for each percent
label = ['Nitrogen', 'Oxygen', 'CO2']

# plotting the pie chart with above data
plt.pie(percent,labels=label, colors = colour)
# showing the pie chart
plt.show()
