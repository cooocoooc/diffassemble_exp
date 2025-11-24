# check the cuda version used by pytorch
import torch

# The installed PyTorch version
print("PyTorch version:", torch.__version__)

# Whether CUDA is available
print("CUDA available:", torch.cuda.is_available())

# The CUDA version PyTorch was built with
# CUDA toolkit version PyTorch was compiled against
# PyTorch will only use the version it was built with
print("CUDA version (runtime):", torch.version.cuda)

# The name of the GPU device
print("Device name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No CUDA device")
