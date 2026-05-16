import os
import hashlib

def get_real_sha256(file_path):
    try:
        with open(file_path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except: return None

class MedicalBlockchainAI:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.ledger = {}
        files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
        for f in files:
            self.ledger[f] = get_real_sha256(os.path.join(image_folder, f))

    def verify(self, image_name, current_file_path):
        current_hash = get_real_sha256(current_file_path)
        original_hash = self.ledger.get(image_name)
        print(f"\nSCANNING: {current_file_path}")
        if current_hash == original_hash and current_hash is not None:
            print("STATUS: SUCCESS - Hash Matches ")
            print("AI OUTPUT: Verified Diagnosis Provided.")
        else:
            print("STATUS: FAILURE - Hash Mismatch ")
            print("SECURITY: Unauthorized Modification Detected! AI BLOCKED.")

IMAGE_DIR = 'images'
ATTACK_DIR = 'attacked_data'
system = MedicalBlockchainAI(IMAGE_DIR)
all_images = sorted([f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

print("="*50)
print("INTEGRATED MEDICAL BLOCKCHAIN-AI SYSTEM REPORT")
print("="*50)

for img in all_images:
    system.verify(img, os.path.join(IMAGE_DIR, img))
    attacked_path = os.path.join(ATTACK_DIR, f"attacked_{img}")
    if os.path.exists(attacked_path):
        system.verify(img, attacked_path)
        print("-" * 30)

print("\n" + "="*50)
print(f"TEST COMPLETED FOR {len(all_images)} IMAGES")
print("="*50)
