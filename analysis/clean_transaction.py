import pandas as pd 
import os

# def salesPipeline(file_path):
    
#     print("Current directory:", os.getcwd())
#     print("Resolved path:", os.path.abspath(file_path))
#     print("File exists:", os.path.exists(file_path))
    
#     df = pd.read_csv(file_path)
    
#     df = df.drop_duplicates()
#     df = df.dropna()
    
# salesPipeline("../data/raw/upi_transactions_2024.csv")

# df = pd.read_csv(, engine="python")

# print(df.head())


file_path = "../data/raw/upi_transactions_2024.csv"

print("File size:", os.path.getsize(file_path), "bytes")