import pandas as pd

# 1. Read the dataset
df = pd.read_csv('INvideos.csv')

# 2. Data Cleaning: Keep only necessary columns and drop rows with missing values
cols_to_keep = ['views', 'likes', 'dislikes', 'comment_count']
df = df[cols_to_keep].dropna()

# 3. Convert types to integer (ensure no errors)
df = df.astype(int)

# 4. Perform Aggregation
total_views = df['views'].sum()
total_likes = df['likes'].sum()
total_dislikes = df['dislikes'].sum()
total_comments = df['comment_count'].sum()

# 5. Display Results
print(f"Total Views: {total_views}")
print(f"Total Likes: {total_likes}")
print(f"Total Dislikes: {total_dislikes}")
print(f"Total Comments: {total_comments}")