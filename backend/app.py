from flask import Flask, request, jsonify
from flask_cors import CORS

from utils.preprocess import load_and_clean_data ,build_interaction_matrix
from utils.recommender import compute_item_similarity, recommend_items

#Initialize flask
app = Flask(__name__)
CORS(app)

#Load data + preprocess once at startup
df = load_and_clean_data("data/amazon_clean.csv")
interaction_matrix = build_interaction_matrix(df)
item_sim_matrix = compute_item_similarity(interaction_matrix)

@app.route('/')
def home() :
    return {'message':'Recommender API is running 🚀'}

@app.route('/recommend', methods = ["GET"])
def get_recommendations() :
    user_id = request.args.get("user_id")
    top_n = int(request.args.get("top_n",5))
    
    if user_id not in interaction_matrix.index :
        return jsonify({"error": "user not found"}), 404
    
    recs = recommend_items(user_id , interaction_matrix, item_sim_matrix, top_n=top_n)
    
    # If recs is a Series, convert to dict first
    if hasattr(recs, "to_dict"):
        recs = recs.to_dict()
    
    result = [{"product_id": pid, "score" : float(score)} for pid, score in recs.items()]
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True,port=5000)