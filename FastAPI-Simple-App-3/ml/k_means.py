from sklearn.cluster import KMeans
import pandas as pd

def perform_kmeans_clustering(user_activity_data):
    user_activities_df = pd.DataFrame(user_activity_data)

    # Convert categorical data to numerical using one-hot encoding
    user_activities_encoded = pd.get_dummies(user_activities_df)

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=3) 
    kmeans.fit(user_activities_encoded)

    # Get cluster labels
    cluster_labels = kmeans.labels_

    return cluster_labels
