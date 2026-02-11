import pandas as pd
products = pd.Series(
    data=[700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard'])
print("Full Product Series:")
print(products)
print("\nPrice of Laptop:")
print(products['Laptop'])
print("\nFirst Two Products (Positional Indexing):")
print(products.iloc[:2])
