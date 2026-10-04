import pandas as pd

data = {
    "Product Name": ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"],
    "Category": ["Electronics", "Electronics", "Electronics", "Audio", "Accessories"],
    "Price": [50000, 25000, 20000, 3000, 1500],
    "Quantity Sold": [20, 60, 30, 80, 100]
}

df = pd.DataFrame(data)

df["Total Sales"] = df["Price"] * df["Quantity Sold"]

print("Product sales:")
print(df)

print("Product with highest sales:")
print(df.loc[df["Total Sales"].idxmax()])

print("Average product price:")
print(df["Price"].mean())

print("Products with quantity sold greater than 50:")
print(df[df["Quantity Sold"] > 50])

print("Products sorted by total sales:")
print(df.sort_values("Total Sales"))