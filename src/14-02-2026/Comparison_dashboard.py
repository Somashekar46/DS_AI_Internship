import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
revenue = [1000, 1200, 1500, 1300, 1700]
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.subplot(1, 2, 2)
plt.plot(months, revenue, marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
