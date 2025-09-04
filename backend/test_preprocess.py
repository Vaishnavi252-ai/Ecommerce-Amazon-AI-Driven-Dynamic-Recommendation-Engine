from utils.preprocess import load_and_clean_data, build_interaction_matrix

# Step 1: Load cleaned dataset
df = load_and_clean_data("data/amazon.csv")

# Step 2: Build user-item interaction matrix
interaction_matrix = build_interaction_matrix(df, user_col="user_id", item_col="product_id", rating_col="rating")

print("Interaction Matrix Shape:", interaction_matrix.shape)
print(interaction_matrix.head())
