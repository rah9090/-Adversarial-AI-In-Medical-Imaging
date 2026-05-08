

- Developed a defense model to preserve medical image integrity against adversarial AI attacks.
- Integrated Blockchain technology for data authenticity.
- Provided a fully reproducible pipeline for future research.


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

##  Dataset Description
- **Source:** Medical Imaging Dataset (Adversarial Samples)
- **Total Samples:** 50 Images+ 3 dataset
- **Features:** Grayscale X-ray/CT images + SHA-256 Hashes+ Blockchain.


//Disply some of images:

| Case Study 01 | Case Study 02 | Case Study 03 |
| :---: | :---: | :---: |
| ![Result 1](results/figures/Result_image1.png) | ![Result 2](results/figures/Result_image20.png) | ![Result 3](results/figures/Result_image3.png) |
| **Case Study 04** | **Case Study 05** | **Case Study 06** |
| ![Result 4](results/figures/Result_image16.png) | ![Result 5](results/figures/Result_image21.png) | ![Result 6](results/figures/Result_image6.png) |
| **Case Study 07** | **Case Study 08** | **Case Study 09** |
| ![Result 7](results/figures/Result_image7.png) | ![Result 8](results/figures/Result_image8.png) | ![Result 9](results/figures/Result_image9.png) |
| **Case Study 10** | **Case Study 11** | **Case Study 12** |
| ![Result 10](results/figures/Result_image18.png) | ![Result 11](results/figures/Result_image17.png) | ![Result 12](results/figures/Result_image12.png) |
| **Case Study 13** | **Case Study 14** | **Case Study 15** |
| ![Result 13](results/figures/Result_image13.png) | ![Result 14](results/figures/Result_image14.png) | ![Result 15](results/figures/Result_image15.png) |



git clone [https://github.com/rah9090/-Adversarial-AI-In-Medical-Imaging](https://github.com/rah9090/-Adversarial-AI-In-Medical-Imaging).

