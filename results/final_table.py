import hashlib
import os
import numpy as np
from PIL import Image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

model = ResNet50(weights='imagenet')

def get_sha256(path):
    if not os.path.exists(path): return None
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def get_ai_stats(path):
    if not os.path.exists(path): return "N/A", "0%"
    img = Image.open(path).convert('RGB').resize((224, 224))
    x = preprocess_input(np.expand_dims(np.array(img), axis=0))
    preds = model.predict(x, verbose=0)
    class_id = np.argmax(preds[0])
    confidence = np.max(preds[0]) * 100
    return class_id, f"{confidence:.2f}%"

LEDGER = {
    "chest": get_sha256("images/xray_chest.png"),
    "neck":  get_sha256("images/xray_neck.png")
}

test_files = [
    ("images/xray_chest.png", "chest"),
    ("images/attacked_xray_chest.png", "chest"),
    ("images/xray_neck.png", "neck"),
    ("images/attacked_xray_neck.png", "neck")
]

fmt = "{:<30} | {:<12} | {:<10} | {:<15}"
print("\n" + fmt.format("Target Image", "Blockchain", "Class ID", "AI Confidence"))
print("-" * 75)

for file_path, category in test_files:
    current_hash = get_sha256(file_path)
    original_hash = LEDGER.get(category)
    
    status = "VALID" if current_hash == original_hash and current_hash is not None else "ATTACKED"
    class_id, conf = get_ai_stats(file_path)
    
    print(fmt.format(file_path, status, str(class_id), conf))
