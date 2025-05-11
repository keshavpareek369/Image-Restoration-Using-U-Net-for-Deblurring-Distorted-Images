# 🧼 Image Restoration Using U-Net for Deblurring Distorted Images

## 📌 Overview

This project focuses on restoring sharpness and fine details in **distorted or blurred images** using a **U-Net-based deep learning architecture**. After experimenting with CNNs and GANs, U-Net delivered the most reliable and high-fidelity results for the image deblurring task, balancing both performance and training stability.

---

## 🗂️ Dataset

- **Total Images:** 42,000  
  - 21,000 Clear Images  
  - 21,000 Distorted (blurred) Images  
- **Validation Set:**  
  - 3,378 Clear + 3,378 Distorted = 6,756 Images  
- **Image Size:** `128 × 128`
- **Image Format:** PNG
- **Source:** Scraped from [Pexels](https://www.pexels.com)
- **Scraping Keywords:**  
  `Nature`, `Human`, `Science`, `Cat`, `Dog`, `Culture`, `Car`, `History`, `Food`, `Vintage`, `B&W`

> Images were resized and normalized to [0, 1] before feeding to the model.

---

## 🧪 Models Tried & Observations

### 🟠 CNN (Baseline)

- **Architecture:** 5 Conv2D layers with ReLU, MaxPool, and Upsampling.
- **Problem:** Could not reconstruct high-frequency textures or edges.
- **Average PSNR:** 24.84  
- **Total Parameters:** 83,715 (~83K)  
- **Conclusion:** Inadequate for fine-grained deblurring. Good baseline but fails in complex cases.

---

### 🔵 GAN (Pix2Pix-Style)

- **Architecture:** U-Net Generator + PatchGAN Discriminator
- **Average Generator Loss (A_Loss):** 10.9802  
- **Average Discriminator Loss:** 0.3434  
- **Total Parameters:** ~2,075,928 (~2M)  
- **Problems Faced:**  
  - Training instability  
  - Mode collapse in some epochs  
  - Higher GPU memory consumption  
- **Conclusion:** GANs showed promise but required significant tuning and computational cost. Not optimal for fast prototyping.

---

## ✅ Final Model: U-Net

### 📐 Architecture

![U-Net Architecture](U-net.png?raw=true)

U-Net is an encoder-decoder architecture with skip connections, enabling it to retain low-level details while capturing semantic context. Ideal for image-to-image translation tasks like deblurring.

### 🔧 Configuration Tested

Two bottleneck configurations were tested:

| Model Variant     | Bottleneck Channels | Total Parameters | Training Loss | Validation Loss | Best PSNR | Best SSIM |
|-------------------|---------------------|------------------|----------------|------------------|-----------|-----------|
| **U-Net Small**   | 512                 | 7.77M            | 0.0230         | ~0.0213          | 30.85     | 0.9229    |
| **U-Net Large**   | 1024                | 31.04M           | 0.0205         | 0.0198           | 30.90     | 0.9261    |

### 🧠 Key Features

- **Skip Connections:** Preserve spatial features lost in downsampling.
- **Channel Depth Tuning:** Improves representational capacity.
- **Trained on GPU (CUDA):** Major reduction in training time.
- **Scheduler:** `ReduceLROnPlateau` based on validation PSNR.
- **Early Stopping:** Enabled for stability.

---

## ⚙️ Training Details

| Parameter         | Value                        |
|-------------------|------------------------------|
| Epochs            | 100 (with early stopping)    |
| Optimizer         | Adam                         |
| Initial LR        | 1e-4                         |
| Batch Size        | 8 (512) / 4 (1024)           |
| Loss Function     | L1 Loss (Mean Absolute Error)|
| Augmentations     | Flip, Rotation, Brightness   |
| Validation Metric | PSNR, SSIM                   |

> For reproducibility, seed was fixed and PyTorch’s deterministic setting was enabled.

---

## 📈 Training Curves

### Channel-1024 Performance

- **Training vs Validation Loss**

![Loss Curve](Training&ValidationLoss(1024).png?raw=true)

- **PSNR Over Epochs**

![PSNR](PSNR.png?raw=true)

- **SSIM Over Epochs**

![SSIM](SSIM.png?raw=true)

---

## 🖼️ Visual Outputs

### 🔹 U-Net (512 Channels)

![Output](512-1.png?raw=true)  
![Output](512-2.png?raw=true)

### 🔹 U-Net (1024 Channels)

![Output](1024-1.png?raw=true)  
![Output](1024-2.png?raw=true)

> Results show restored details like textures, sharp edges, and fine structures that were lost in the original distorted images.

---

## 📊 Quantitative Summary

| Model     | PSNR ↑ | SSIM ↑ | Parameters ↓ | Speed (1 image) ↓ |
|-----------|--------|--------|---------------|--------------------|
| CNN       | 24.84  | 0.81   | 83K           | Fastest (Low quality) |
| GAN       | ~29.20 | ~0.89  | 2M            | Slow (Unstable)       |
| U-Net-512 | 30.85  | 0.9229 | 7.7M          | Balanced             |
| U-Net-1024| 30.90  | 0.9261 | 31M           | Slowest (Best quality) |

---

## 🔁 Suggested Improvements & Future Work

- ✅ **Multi-scale Loss** (combine L1 with perceptual/VGG loss for better visual quality)
- ✅ **Residual U-Net** or **Attention U-Net** to improve focus on critical regions.
- 🔄 **Use Deformable Convolutions** for handling spatially variant blur.
- 🔄 **Apply FFT-domain losses** to better preserve high-frequency textures.
- 🔄 **Model Quantization/Pruning** for deployment on edge devices.
- ⏳ **Train on Larger Datasets** like GoPro, GOPRO-Large, or Adobe240 for generalization.
- 🌍 **Integrate with Web App** using Streamlit or Flask for live demos.

---

## 🧪 How to Run

### 🔧 Setup

```bash
git clone https://github.com/yourusername/unet-deblurring
cd unet-deblurring
pip install -r requirements.txt
