
- `Data/`: Raw and processed medical image datasets.
- `src/`: Source code for preprocessing, model training, and evaluation.
- `results/`: Contains performance tables, figures, and logs.
- `models/`: The best-performing saved model.

- Developed a defense model to preserve medical image integrity against adversarial AI attacks.
- Integrated Blockchain technology for data authenticity.
- Provided a fully reproducible pipeline for future research.


| Metric | Measured Value |
| :--- | :--- |
| **Min Latency** | 45.35 ms |
| **Max Latency** | 45.94 ms |
| **Average Latency** | 45.83 ms |
| **Throughput** | 400.6 TPS |
| **Total Transactions** | 1500 |
| **Block Finality** | 2035.07 ms |


- **Confusion Matrix:** Displays classification performance under attack.
![Confusion Matrix](results/figures/confusion_matrix.png)


git clone [https://github.com/rah9090/-Adversarial-AI-In-Medical-Imaging](https://github.com/rah9090/-Adversarial-AI-In-Medical-Imaging)
pip install -r requirements.txt
python src/train.py
python src/evaluate.py
