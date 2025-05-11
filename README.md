# Image Restoration Using U-Net for Deblurring Distorted Images

## 📌 Overview
This project aims to restore clarity in distorted images using a U-Net based deep learning architecture. We experimented with CNNs and GANs but ultimately found U-Net most effective for preserving fine details and achieving high-quality deblurring results.

---

## 🗂️ Dataset

- **Total Images:** 42,000  
  - 21,000 Clear Images  
  - 21,000 Distorted Images  
- **Validation Set:**  
  - 3,378 Clear + 3,378 Distorted = 6,756 Images
- **Image Size:** 128 × 128
- **Source:** Scraped from [Pexels](https://www.pexels.com)
- **Keywords for Scraping:** `Nature`, `Human`, `Science`, `Cat`, `Dog`, `Culture`, `Car`, `History`, `Food`, `Vintage`, `B&W`

---

## 🧠 Models Tried & Challenges Faced

### 🟠 CNN (Baseline)
- **Issue:** Lacked fine detail preservation.
- **PSNR:** 24.84
- **Total Params:** 83,715(83K)
- **Conclusion:** Poor performance in complex deblurring scenarios.

### 🔵 GAN
- **Training Instability**
- **A_Loss Generator:** 10.9802
- **A_Loss Discriminator:** 0.3434
- **Total Parameters:** ~2,075,928(2M)
- **Conclusion:** High resource demands and unstable performance.

---

## ✅ Final Model: U-Net

### 📐 Architecture
![Architecture](U-net.png?raw=true "U-net_Architecture")

### 🔧 Bottleneck Parameters
- In the U-Net architecture, two configurations were tested for the bottleneck layer:
  - **512 Channels**
  - **1024 Channels**
- These configurations helped analyze the trade-off between performance and GPU memory usage.

- Encoder-Decoder with skip connections.
- Trained using **GPU (CUDA)** for faster execution.
- Used learning rate scheduling and validation-based model saving.
  
### 🧪 Performance-Channel-512
-**Total params:** 7,766,051(7.7M)
-  **Training Loss:** 0.0230
- **Best Validation PSNR:** 30.85
- **Best Validation SSIM:** 0.9229

### 🧪 Performance-channel-1024
-**Total params:**31,043,651(3.1cr)
-  **Best Validation PSNR:** 30.90
- **Validation Loss:** 0.0198
- **Training Loss:** 0.0205
- **Best Validation SSIM:** 0.9261
  

### ⚙️ Technical Considerations
- Reduced batch size to manage GPU memory constraints.
- High memory usage due to deep architecture and multiple channels.
- Long training time on CPU initially, later optimized using GPU.

---

## 🖼️ Outputs
The model successfully reconstructs fine details and restores high-frequency components in distorted images, delivering a significant visual and numerical performance improvement over baseline CNN and GAN methods.

Channel-512:

![Output](512-1.png?raw=true "channel-512") 
![Output](512-2.png?raw=true "channel-512")

Channel-1024:

![Output](1024-1.png?raw=true "channel-1024")
![Output](1024-2.png?raw=true "channel-1024")


---

## 📈 Training & Validation Curves
Training and validation loss curves indicate smooth convergence and no overfitting, validating the reliability of the U-Net model.

Channel-1024

![LossCurve](Training&ValidationLoss(1024).png?raw=true "channel-1024")
![PSNR](PSNR.png?raw=true "channel-1024")
![PSNR](SSIM.png?raw=true "channel-1024")
---


## 📃 License
This project is for academic and non-commercial use only. For commercial use, please contact the Keshavpareek369@gmail.com
