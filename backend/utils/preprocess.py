import pandas as pd
import os

def load_and_clean_data(path="data/amazon_data.csv"):
    df = pd.read_csv(path)

    print("Initial shape:", df.shape)
    print("Columns:", df.columns)

    # Drop duplicates 
    df.drop_duplicates(inplace=True)

    # Drop missing values
    df.dropna(inplace=True)

    # Convert rating column to numeric (force errors to NaN, then drop them)
    if "rating" in df.columns:
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
        df.dropna(subset=["rating"], inplace=True)

    # Rename columns to standard format if needed
    df.rename(columns={
        "userId": "user_id",
        "productId": "product_id",
        "Rating": "rating",
        "timestamp": "timestamp"
    }, inplace=True, errors="ignore")

    print("After Cleaning:", df.shape)
    print(df.head())

    # Save cleaned dataset
    df.to_csv("data/amazon_clean.csv", index=False)
    print("✅ Cleaned dataset saved at: data/amazon_clean.csv")

    return df


def build_interaction_matrix(df, user_col="user_id", item_col="product_id", rating_col="rating"):
    """
    Creates a user-item interaction matrix (users as rows, products as columns)
    """
    interaction_matrix = df.pivot_table(
        index=user_col, 
        columns=item_col, 
        values=rating_col, 
        fill_value=0
    )
    return interaction_matrix





    
    