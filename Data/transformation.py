import pandas as pd

df = pd.read_csv('raw_oreo_data.csv')

new_concepts = pd.DataFrame({
    'Flavor': [
        'Bourbon Pecan Crunch Oreo', 
        'Oreo Milkshake Oreo', 
        'Fudgey Brownie Oreo', 
        'Coconut Cream Pie Oreo'
    ],
    'Category': ['New Concept', 'New Concept', 'New Concept', 'New Concept'],
    'Reviews_Count': [25, 25, 25, 25],
    'Avg_Rating': [4.3, 4.8, 4.6, 3.9],
    'Sentiment_Score': [0.75, 0.95, 0.88, 0.55],
    'Social_Mentions': [12000, 26000, 19000, 8500]
})

combined_df = pd.concat([df, new_concepts], ignore_index=True)

combined_df['Normalized_Rating'] = (combined_df['Avg_Rating'] - combined_df['Avg_Rating'].min()) / (combined_df['Avg_Rating'].max() - combined_df['Avg_Rating'].min())
combined_df['Normalized_Mentions'] = (combined_df['Social_Mentions'] - combined_df['Social_Mentions'].min()) / (combined_df['Social_Mentions'].max() - combined_df['Social_Mentions'].min())
combined_df['Normalized_Sentiment'] = (combined_df['Sentiment_Score'] - combined_df['Sentiment_Score'].min()) / (combined_df['Sentiment_Score'].max() - combined_df['Sentiment_Score'].min())

combined_df['Composite_Score'] = (0.5 * combined_df['Normalized_Rating']) + \
                                 (0.3 * combined_df['Normalized_Sentiment']) + \
                                 (0.2 * combined_df['Normalized_Mentions'])

final_df = combined_df.sort_values(by='Composite_Score', ascending=False).reset_index(drop=True)
final_df = final_df.round(3)

final_df.to_csv('clean_oreo_data.csv', index=False)