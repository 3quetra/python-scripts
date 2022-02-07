from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# Numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

# Canvas for graphs
plt.figure(figsize=(12, 8))

# Graph 1
ax1 = plt.subplot(1, 2, 1)
x_values = range(len(months))
plt.plot(x_values, visits_per_month, color = 'Lime', marker = 'o')

# Names
plt.title('Total site visits per month')
plt.xlabel('Months')
plt.ylabel('Total Visits')


# Ticks
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)


# Graph 2
ax2 = plt.subplot(1, 2, 2)
plt.plot(x_values, key_limes_per_month, color = 'Orange', marker = 'o', label = 'Key Lime')
plt.plot(x_values, persian_limes_per_month, color = 'LimeGreen', marker = 's', label = 'Persian Lime')
plt.plot(x_values, blood_limes_per_month, color = 'Maroon', marker = '*', label = 'Blood Lime')

# Legend
plt.legend(loc = 0)

# Names
plt.title('Limes sold per month')
plt.xlabel('Months')
plt.ylabel('Number of limes')

# Ticks
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)

# Adjust
plt.subplots_adjust(wspace = 0.3)

plt.show()

plt.savefig('limes_sale_graphs')

