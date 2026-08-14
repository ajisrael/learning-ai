"""Working example - Milestone 1.3: PCA and k-means (embeddings intuition).

Run:  python3 projects/phase-1/milestone-1.3/example_pca_kmeans.py

Reduces the iris dataset to 2 dimensions with PCA, clusters with k-means, and
prints how much variance each principal component captures. This is your first
taste of the "represent things as vectors" idea that powers Phase 4's RAG and
embeddings.

Modifications to try (from phase-1-classical-ml.md, M1.3.1 - M1.3.4):
  M1.3.1  change n_components (2 -> 4 -> None) and read the variance ratios
  M1.3.2  change n_clusters (2, 4) and look for the elbow in inertia
  M1.3.3  multiply one feature by 1000 -> see PCA break; add StandardScaler
  M1.3.4  re-run the whole thing on a dataset you pick
"""

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load the bundled iris dataset (150 rows, 4 features, 3 known species).
data = load_iris()
X = data.data

# --- PCA: compress 4 features into 2 while keeping the most variance. --------
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print("Explained variance ratio per component:", [f"{v:.3f}" for v in pca.explained_variance_ratio_])
print(f"Total variance kept in 2 components:    {sum(pca.explained_variance_ratio_):.3f}")

# --- k-means: cluster the reduced points into 3 groups. ----------------------
kmeans = KMeans(n_clusters=3, n_init=10, random_state=0)
labels = kmeans.fit_predict(X_reduced)

print(f"\nk-means (k=3) on 2-D PCA space: {len(set(labels))} clusters")
print(f"Inertia (lower is tighter):    {kmeans.inertia_:.1f}")
print()
print("The iris dataset is known to have 3 real species. Does k-means find them?")
print("(Not always - that mismatch is the lesson. See M1.3.2.)")
