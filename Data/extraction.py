import pandas as pd
import numpy as np

flavors = [
    "OREO Original", "OREO Double Stuff", "OREO Golden", "OREO Mint", 
    "OREO Lemon", "OREO Birthday Cake", "OREO Peanut Butter", "OREO Reese's", 
    "OREO Cookie Dough", "OREO Blueberry Pie", "OREO Cinnamon Bun", 
    "OREO Chocolate", "OREO Firecracker Pop", "OREO BTS"
]

category_map = {
    "OREO Original": "Classic", "OREO Double Stuff": "Classic", "OREO Golden": "Classic", 
    "OREO Chocolate": "Classic", "OREO Mint": "Classic", "OREO Peanut Butter": "Classic", 
    "OREO Lemon": "Classic", "OREO Birthday Cake": "Novelty", "OREO Reese's": "Novelty", 
    "OREO Cookie Dough": "Novelty", "OREO Cinnamon Bun": "Novelty", 
    "OREO Blueberry Pie": "Seasonal", "OREO Firecracker Pop": "Seasonal", 
    "OREO BTS": "Collaboration"
}

df = pd.DataFrame({'Flavor': flavors})
df['Category'] = df['Flavor'].map(category_map)

np.random.seed(42)
df['Reviews_Count'] = np.random.randint(50, 5000, size=len(df))
df['Avg_Rating'] = np.round(np.random.uniform(3.5, 4.9, size=len(df)), 1)
df['Sentiment_Score'] = np.round(np.random.uniform(0.1, 1.0, size=len(df)), 2)
df['Social_Mentions'] = np.random.randint(1000, 25000, size=len(df))

df.to_csv('raw_oreo_data.csv', index=False)