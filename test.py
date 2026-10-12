import torch

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

# Create a simple tensor to test computation
x = torch.rand(3, 3)
print("Random Tensor:")
print(x)