from utils.preprocess import load_and_clean_data, build_interaction_matrix
from utils.recommender import compute_user_similarity, compute_item_similarity, recommend_items

# Load and clean data
df = load_and_clean_data("data/amazon_clean.csv")

# Build interaction matrix
interaction_matrix = build_interaction_matrix(df)

# Compute similarities
user_sim = compute_user_similarity(interaction_matrix)
item_sim = compute_item_similarity(interaction_matrix)

#pick a sample user 
sample_user = interaction_matrix.index[0]

#generate recommendation
recommendations = recommend_items(sample_user, interaction_matrix, item_sim_matrix=item_sim, top_n=5)

print("✅ User Similarity Matrix Shape:", user_sim.shape)
print(user_sim.head())

print("\n✅ Item Similarity Matrix Shape:", item_sim.shape)
print(item_sim.head())

print(f"Recommendations for User {sample_user}:")
print(recommendations)


