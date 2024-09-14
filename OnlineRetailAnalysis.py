import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

df = pd.read_excel("C:\\Users\\WIN 10\\Desktop\\project\\Project for CV\\Online Retail.xlsx")
df.head()
# print(df.head())
# print(df.info())
# print(df.isnull().sum())
df = df.dropna(subset=['CustomerID'])
# print(df.isnull().sum())
df = df.drop_duplicates()
# print(f"Duplicates: {df.duplicated().sum()}")
df["CustomerID"] = df["CustomerID"].astype(int)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
# print(df.dtypes)

# Creating a Total Price column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
# extracting Year,Month,Day And Hour from Invoice Date
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["Day"] = df["InvoiceDate"].dt.day
df["Hour"] = df["InvoiceDate"].dt.hour
df.head()
# print(df.head)
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
df.describe()
# print(df.describe())

# summarizing sales by country, customer, product
sales_by_country = df.groupby("Country")["TotalPrice"].sum().reset_index().sort_values(by="TotalPrice", ascending=False)
# print(sales_by_country.head())
sales_by_customer = df.groupby("CustomerID")["TotalPrice"].sum().reset_index().sort_values(by="TotalPrice", ascending=False)
# print(sales_by_customer.head())
sales_by_product = df.groupby("Description")["TotalPrice"].sum().reset_index().sort_values(by= "TotalPrice", ascending= False)
# print(sales_by_product.head())

# sales trend by year
sales_by_year = df.groupby("Year")["TotalPrice"].sum().reset_index()
plt.figure(figsize=(10,6))
sns.lineplot(data=sales_by_year, x= "Year", y= "TotalPrice")
plt.title("total_sales_by_year")
plt.xlabel("Year")
plt.ylabel("total sales")
# plt.show()

# sales trend by month
sales_by_month = df.groupby("Month")["TotalPrice"].sum().reset_index()
plt.figure(figsize=(10,6))
sns.lineplot(data=sales_by_month, x= "Month", y= "TotalPrice")
plt.title("totla sales by month")
plt.xlabel("Month")
plt.ylabel("Totla Sales")
# plt.show()

# sales trend by day
sales_by_day = df.groupby("Day")["TotalPrice"].sum().reset_index()
plt.figure(figsize=(10,6))
sns.lineplot(data=sales_by_day, x= "Day", y= "TotalPrice")
plt.title("Total sales by day")
plt.xlabel("Day")
plt.ylabel("Total sales")
# plt.show()

# Top 10 Countries by total sales
top_countries = sales_by_country.head(10)
plt.figure(figsize=(12,8))
sns.barplot(data=top_countries, x= "TotalPrice", y= "Country")
plt.title("Top 10 countries by Total sales")
plt.xlabel("Total sales")
plt.ylabel("Country")
# plt.show()

# Top 10 Customers by sales
top_customers = sales_by_customer.head(10)
plt.figure(figsize=(12,8))
sns.barplot(data= top_customers ,x= "TotalPrice", y= "CustomerID")
plt.title("Top 10 customer by total")
plt.xlabel("Total Sales")
plt.ylabel("CustomerID")
# plt.show()

# Top 10 products by sales
top_products = sales_by_product.head(10)
plt.figure(figsize=(12,8))
sns.barplot(data=top_products, x= "TotalPrice", y= "Description")
plt.title("Top 10 Product by Total sales")
plt.xlabel("Total sales")
plt.ylabel("Product")
# plt.show()

# sales distribution by hour
sales_by_hour = df.groupby("Hour")["TotalPrice"].sum().reset_index()
plt.figure(figsize=(10,6))
sns.lineplot(data=sales_by_hour,x= "Hour", y= "TotalPrice")
plt.title("Total sales by hour of the day")
plt.xlabel("Hour of the Day")
plt.ylabel("Total Sales")
# plt.show()

# Calculating correlation matrix
correlation_matrix = df[["Quantity","UnitPrice","TotalPrice"]].corr()
print(correlation_matrix)
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# Visualize the distribution of totalprice
plt.figure(figsize=(10,6))
sns.histplot(df["TotalPrice"], bins=50, kde=True)
plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")
plt.show()

# Splitting data into two periods: First half and Second half of the Year
'''first_half = df[df["Month"].isin([1,2,3,4,5,6])]
second_half = df[df["Month"].isin([7,8,9,10,11,12])]
# Calculating the total sales for each period
first_half_sales = first_half["TotalPrice"]
second_half_sales = second_half["TotalPrice"]

# Conduct a t-test to compare the means of the two periods
t_stat, p_value = ttest_ind(first_half_sales, second_half_sales)
print(f"T- Statistic: {t_stat}")
print(f"P- Value: {p_value}")

# Interpreting the result
alpha = 0.05
if p_value < alpha:
    print("We reject the null hypothesis, There is significant difference in sales between the two periods")
else:
    print("We fail to reject null hypothesis, There is no significant difference in sales between the two periods")

# Exporting flies to csv
df.to_csv("Cleaned_online_retial.csv", index=False)
sales_by_country.to_csv("sales_by_country.csv", index=False)
sales_by_customer.to_csv("sales_by_customer.csv", index= False)
sales_by_product.to_csv("sales_by_product.csv", index=False)
sales_by_year.to_csv("sales_by_year.csv", index=False)
sales_by_month.to_csv("sales_by_month.csv", index=False)
sales_by_day.to_csv("sales_by_day.csv", index=False)
sales_by_hour.to_csv("sales_by_hours.csv", index=False)'''