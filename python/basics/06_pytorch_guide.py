# PyTorch Complete Guide for Beginners
# PyTorch is a deep learning library for building neural networks

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

print("=" * 60)
print("PYTORCH FUNDAMENTALS GUIDE")
print("=" * 60)

# ============================================================================
# 1. TENSORS - The basic data structure in PyTorch
# ============================================================================
print("\n1. CREATING TENSORS")
print("-" * 60)

# Create tensors from lists
tensor_1d = torch.tensor([1, 2, 3, 4, 5])
print(f"1D Tensor: {tensor_1d}")

tensor_2d = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(f"2D Tensor (Matrix):\n{tensor_2d}")

# Create tensors with specific values
zeros = torch.zeros(3, 3)
print(f"\nZeros tensor:\n{zeros}")

ones = torch.ones(2, 4)
print(f"\nOnes tensor:\n{ones}")

random_tensor = torch.rand(2, 3)
print(f"\nRandom tensor:\n{random_tensor}")

# Create tensors from numpy arrays
numpy_array = np.array([1, 2, 3])
tensor_from_numpy = torch.from_numpy(numpy_array)
print(f"\nTensor from numpy: {tensor_from_numpy}")

# ============================================================================
# 2. TENSOR PROPERTIES
# ============================================================================
print("\n\n2. TENSOR PROPERTIES")
print("-" * 60)

t = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
print(f"Shape: {t.shape}")
print(f"Data type: {t.dtype}")
print(f"Number of dimensions: {t.ndim}")
print(f"Total elements: {t.numel()}")

# ============================================================================
# 3. TENSOR OPERATIONS
# ============================================================================
print("\n\n3. TENSOR OPERATIONS")
print("-" * 60)

a = torch.tensor([1, 2, 3], dtype=torch.float32)
b = torch.tensor([4, 5, 6], dtype=torch.float32)

print(f"Tensor a: {a}")
print(f"Tensor b: {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Power (a ** 2): {a ** 2}")

# Dot product
dot_product = torch.dot(a, b)
print(f"Dot product: {dot_product}")

# Matrix multiplication
matrix_a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
matrix_b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
matrix_product = torch.matmul(matrix_a, matrix_b)
print(f"\nMatrix multiplication:\n{matrix_product}")

# ============================================================================
# 4. TENSOR RESHAPING AND INDEXING
# ============================================================================
print("\n\n4. TENSOR RESHAPING AND INDEXING")
print("-" * 60)

t = torch.arange(1, 13)  # Create tensor [1, 2, ..., 12]
print(f"Original tensor: {t}")
print(f"Shape: {t.shape}")

# Reshaping
reshaped = t.reshape(3, 4)
print(f"\nReshaped to (3, 4):\n{reshaped}")

# Indexing
print(f"\nFirst element: {t[0]}")
print(f"Last element: {t[-1]}")
print(f"Slice t[2:5]: {t[2:5]}")
print(f"2D indexing reshaped[0, :]: {reshaped[0, :]}")
print(f"2D indexing reshaped[:, 1]: {reshaped[:, 1]}")

# ============================================================================
# 5. DEVICE (CPU vs GPU)
# ============================================================================
print("\n\n5. DEVICE (CPU vs GPU)")
print("-" * 60)

# Check if GPU is available
print(f"GPU available: {torch.cuda.is_available()}")
print(f"Device: {torch.device('cuda' if torch.cuda.is_available() else 'cpu')}")

# Create tensor on CPU
cpu_tensor = torch.tensor([1, 2, 3])
print(f"CPU tensor device: {cpu_tensor.device}")

# Move tensor to GPU (if available)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
gpu_tensor = cpu_tensor.to(device)
print(f"GPU tensor device: {gpu_tensor.device}")

# ============================================================================
# 6. AUTOGRAD - Automatic differentiation (for computing gradients)
# ============================================================================
print("\n\n6. AUTOGRAD - AUTOMATIC DIFFERENTIATION")
print("-" * 60)

# Create tensors with requires_grad=True to track operations
x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

# Perform operations
z = x**2 + y**3

print(f"x: {x.item()}")
print(f"y: {y.item()}")
print(f"z = x^2 + y^3 = {z.item()}")

# Compute gradients
z.backward()

print(f"\nGradient of z with respect to x: {x.grad}")
print(f"Gradient of z with respect to y: {y.grad}")
print("(dz/dx = 2x = 4, dz/dy = 3y^2 = 27)")

# ============================================================================
# 7. BUILDING A SIMPLE NEURAL NETWORK
# ============================================================================
print("\n\n7. BUILDING A SIMPLE NEURAL NETWORK")
print("-" * 60)

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(10, 5)      # Input: 10, Output: 5
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(5, 1)       # Input: 5, Output: 1
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Create model
model = SimpleNN()
print("Model created:")
print(model)

# Create sample input
sample_input = torch.randn(1, 10)  # Batch size: 1, Features: 10
output = model(sample_input)
print(f"\nInput shape: {sample_input.shape}")
print(f"Output: {output}")

# ============================================================================
# 8. TRAINING A SIMPLE NEURAL NETWORK
# ============================================================================
print("\n\n8. TRAINING A SIMPLE NEURAL NETWORK")
print("-" * 60)

# Generate sample dataset
X = torch.randn(100, 10)  # 100 samples, 10 features
y = torch.randn(100, 1)   # 100 labels

# Create model
model = SimpleNN()

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

print("Training the model for 5 epochs...")
print(f"{'Epoch':<10} {'Loss':<15}")
print("-" * 25)

# Training loop
for epoch in range(5):
    # Forward pass
    output = model(X)
    loss = criterion(output, y)
    
    # Backward pass
    optimizer.zero_grad()  # Clear gradients
    loss.backward()        # Compute gradients
    optimizer.step()       # Update weights
    
    if (epoch + 1) % 1 == 0:
        print(f"{epoch + 1:<10} {loss.item():<15.6f}")

print("\nTraining completed!")

# Make predictions on new data
with torch.no_grad():
    test_input = torch.randn(5, 10)
    predictions = model(test_input)
    print(f"Predictions for 5 new samples:\n{predictions}")

# ============================================================================
# 9. SAVING AND LOADING MODELS
# ============================================================================
print("\n\n9. SAVING AND LOADING MODELS")
print("-" * 60)

# Save model
model_path = "simple_nn.pth"
torch.save(model.state_dict(), model_path)
print(f"Model saved to {model_path}")

# Load model
loaded_model = SimpleNN()
loaded_model.load_state_dict(torch.load(model_path))
print("Model loaded successfully")

# ============================================================================
# 10. USEFUL FUNCTIONS
# ============================================================================
print("\n\n10. USEFUL TENSOR FUNCTIONS")
print("-" * 60)

t = torch.tensor([1, 5, 3, 8, 2, 9])
print(f"Tensor: {t}")
print(f"Sum: {t.sum().item()}")
print(f"Mean: {t.float().mean().item():.2f}")
print(f"Max: {t.max().item()}")
print(f"Min: {t.min().item()}")
print(f"Sorted: {t.sort()[0]}")

# Concatenate tensors
t1 = torch.tensor([1, 2, 3])
t2 = torch.tensor([4, 5, 6])
concatenated = torch.cat([t1, t2])
print(f"\nConcatenate: {concatenated}")

# Stack tensors
stacked = torch.stack([t1, t2])
print(f"Stacked:\n{stacked}")

print("\n" + "=" * 60)
print("END OF PYTORCH GUIDE")
print("=" * 60)
