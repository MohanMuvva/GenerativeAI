import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict
import random

class VideoRecommendationSystem:
    def __init__(self, videos: List[str], transitions: Dict[str, Dict[str, float]]):
        self.videos = videos
        self.transitions = transitions
        self.n = len(videos)
        self.video_indices = {video: i for i, video in enumerate(videos)}
        self.pagerank = None

    def create_transition_matrix(self) -> np.ndarray:
        M = np.zeros((self.n, self.n))
        for i, video in enumerate(self.videos):
            if video in self.transitions:
                for next_video, prob in self.transitions[video].items():
                    j = self.video_indices[next_video]
                    M[j, i] = prob
            else:
                M[:, i] = 1 / self.n  # If no transitions, assume equal probability
        return M

    def calculate_pagerank(self, damping_factor: float = 0.85, epsilon: float = 1e-10) -> np.ndarray:
        M = self.create_transition_matrix()
        v = np.ones(self.n) / self.n
        
        while True:
            v_next = (1 - damping_factor) / self.n + damping_factor * M @ v
            if np.sum(np.abs(v_next - v)) < epsilon:
                break
            v = v_next
        
        self.pagerank = v
        return v

    def visualize_recommendations(self, video: str, top_k: int = 5):
        if self.pagerank is None:
            self.calculate_pagerank()
        
        G = nx.DiGraph()
        G.add_node(video, score=self.pagerank[self.video_indices[video]])
        
        related_videos = self.transitions.get(video, {})
        scores = [(v, prob * self.pagerank[self.video_indices[v]]) for v, prob in related_videos.items()]
        scores.sort(key=lambda x: x[1], reverse=True)
        top_recommendations = scores[:top_k]
        
        for rec_video, score in top_recommendations:
            G.add_node(rec_video, score=self.pagerank[self.video_indices[rec_video]])
            G.add_edge(video, rec_video, weight=score)
        
        pos = nx.spring_layout(G)
        plt.figure(figsize=(12, 8))
        
        # Draw nodes
        nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightblue')
        nx.draw_networkx_labels(G, pos, {node: f"{node}\n{G.nodes[node]['score']:.3f}" for node in G.nodes()})
        
        # Draw edges
        edge_weights = [G[u][v]['weight'] * 5 for u, v in G.edges()]  # Multiply by 5 to make edges more visible
        nx.draw_networkx_edges(G, pos, width=edge_weights, edge_color='gray', arrows=True, arrowsize=20)
        
        # Add edge labels
        edge_labels = {(u, v): f"{G[u][v]['weight']:.3f}" for u, v in G.edges()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        plt.title(f"Video Recommendations for {video}")
        plt.axis('off')
        plt.tight_layout()
        plt.show()

# Function to generate interlinked videos
def generate_interlinked_videos(num_videos: int) -> Dict[str, Dict[str, float]]:
    videos = [f"Video {chr(65 + i)}" for i in range(num_videos)]  # Generate video names A, B, C, ...
    transitions = {}
    
    for video in videos:
        transitions[video] = {}
        other_videos = [v for v in videos if v != video]
        probabilities = np.random.dirichlet(np.ones(len(other_videos)))  # Generate random probabilities
        for other_video, prob in zip(other_videos, probabilities):
            transitions[video][other_video] = prob
    
    return videos, transitions

# Set a fixed random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Generate interlinked videos
num_videos = 7  # You can change this number
videos, transitions = generate_interlinked_videos(num_videos)

# Create recommendation system
recommender = VideoRecommendationSystem(videos, transitions)

# Choose a fixed video to get recommendations for
current_video = videos[0]  # Start with the first video
top_k = 3  # Number of top recommendations to show

print(f"Getting recommendations for: {current_video}")
recommender.visualize_recommendations(current_video, top_k)