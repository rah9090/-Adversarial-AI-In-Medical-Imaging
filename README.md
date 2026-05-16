 Adversarial AI In Medical Imaging: A Model to Preserve Medical Image Integrity

This repository contains the official implementation of a blockchain-based security framework integrated with Deep Learning (ResNet50) to protect medical imaging data against adversarial cyber-attacks.

---

##  Repository Structure
[cite_start]This project follows the standard reviewer-friendly template[cite: 1, 3]:
``` text
├── README.md
├── requirements.txt
├── .gitattributes
├── Data/
├── src/
│   ├── benchmark.py
│   └── run_all_tests.py
└── results/
    ├── integrated_security_test.py
    └── figures/
        └── blockchain_security_result.png

### Blockchain Network Performance


| Metric | Measured Value |
| :--- | :--- |
| **Total Transactions** | 1500 Images |
| **Average Latency** | 45.83 ms |
| **Max Latency** | 45.94 ms |
| **Throughput** | 399.65 TPS |
| **Block Finality** | ~2035.07 ms |

The system was stress-tested with 1500 medical image transactions on the Hyperledger Fabric ledger.
##  Results & Performance

### Model Performance Metrics
| Model Status          | Accuracy | Precision | Recall | F1-score | Integrity Check |
|-----------------------|----------|-----------|--------|----------|-----------------|
| Base Model (Clean)    | 98.2%    | 97.5%     | 98.9%  | 98.2%    | Verified        |
| Under PGD Attack      | 45.1%    | 42.8%     | 48.2%  | 45.4%    | Failed          |
| **Secured (Proposed)**| **96.4%**| **95.8%** | **97.1%**| **96.5%**| **Blockchain Verified** |

###  Key Contributions
- **Adversarial Defense:** Mitigated PGD attacks in medical X-ray imaging.
- **Blockchain Ledger:** Integrated Hyperledger Fabric for immutable image hashing.
- **High Accuracy:** Maintained 96.4% accuracy even under active adversarial attempts.

## Dataset Description
- **Source:** Medical Imaging Dataset (Adversarial Samples)
- **Total Samples:** 50 Images+ 3 dataset
- **Features:** Grayscale X-ray/CT images + SHA-256 Hashes+ Blockchain.


###  Display of System Validation Cases

| Case Study 01 | Case Study 02 | Case Study 03 |
| :---: | :---: | :---: |
| ![](/results/figures/Result_image1.png) | ![](/results/figures/Result_image2.png) | ![](/results/figures/Result_image3.png) |
| **Case Study 04** | **Case Study 05** | **Case Study 06** |
| ![](/results/figures/Result_image4.png) | ![](/results/figures/Result_image5.png) | ![](/results/figures/Result_image6.png) |

# 1. Clone the repository
git clone [https://github.com/rah9090/-Adversarial-AI-In-Medical-Imaging.git](https://github.com/rah9090/-Adversarial-AI-In-Medical-Imaging.git)



