import numpy as np

# Representasi mesh segitiga
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0.5, 0.5, 1]
])

# Hitung matriks kovariansi
covariance_matrix = np.cov(vertices.T)

# Hitung nilai eigen dan vektor eigen
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

# Definisikan deformasi lokal
deformation_matrix = np.diag(eigenvalues) @ eigenvectors.T

# Terapkan deformasi pada mesh
deformed_vertices = vertices @ deformation_matrix

# Visualisasikan animasi
# ...
