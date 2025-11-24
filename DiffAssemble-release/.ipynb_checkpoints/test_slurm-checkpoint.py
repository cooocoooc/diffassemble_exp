{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# check the cuda version used by pytorch\n",
    "import torch\n",
    "\n",
    "# The installed PyTorch version\n",
    "print(\"PyTorch version:\", torch.__version__)\n",
    "\n",
    "# Whether CUDA is available\n",
    "print(\"CUDA available:\", torch.cuda.is_available())\n",
    "\n",
    "# The CUDA version PyTorch was built with\n",
    "# CUDA toolkit version PyTorch was compiled against\n",
    "# PyTorch will only use the version it was built with\n",
    "print(\"CUDA version (runtime):\", torch.version.cuda)\n",
    "\n",
    "# The name of the GPU device\n",
    "print(\"Device name:\", torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"No CUDA device\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
