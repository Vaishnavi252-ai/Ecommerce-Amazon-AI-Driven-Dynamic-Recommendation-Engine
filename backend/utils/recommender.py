import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def compute_user_similarity(interaction_matrix):
    
    similarity = cosine_similarity(interaction_matrix)
    
    user_sim_matrix = pd.DataFrame(
        similarity,
        index = interaction_matrix.index,
        columns = interaction_matrix.index
    )
    return user_sim_matrix

def compute_item_similarity(interaction_matrix):

    # remove items (columns) where all values are 0
    interaction_matrix = interaction_matrix.loc[:, (interaction_matrix != 0).any(axis=0)]

    similarity = cosine_similarity(interaction_matrix.T)

    item_sim_matrix = pd.DataFrame(
        similarity,
        index=interaction_matrix.columns,
        columns=interaction_matrix.columns
    )
    return item_sim_matrix

def recommend_items(user_id, interaction_matrix, item_sim_matrix, top_n = 5):
    
    if user_id not in interaction_matrix.index:
        return[]   # user not found
    
    # User’s ratings
    user_ratings = interaction_matrix.loc[user_id]
    
    # Scores = similarity * rating
    scores = item_sim_matrix.dot(user_ratings).div(item_sim_matrix.sum(axis=1))
    
    #remove item that already rated 
    already_rated = user_ratings[user_ratings>0].index
    scores = scores.drop(already_rated,errors="ignore")
    
    #pick first top 5 items 
    recommended_items = scores.sort_values(ascending=False).head(top_n)
    
    return recommend_items
    
    