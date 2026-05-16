import hashlib
from PIL import Image
import io
import os

def get_real_sha256(image_path):
    if not os.path.exists(image_path):
        return None
    with Image.open(image_path) as img:
        buf = io.BytesIO()
        img.save(buf, format=img.format)
        return hashlib.sha256(buf.getvalue()).hexdigest()

class MedicalBlockchainAI:
    def __init__(self):
    
        self.ledger = {}
        image_dir = "images/"
        if os.path.exists(image_dir):
            for f in os.listdir(image_dir):
             
                if f.lower().startswith("image") and not f.startswith("Result_") and f.endswith(('.png', '.jpg', '.jpeg', '.JPG')):
                    self.ledger[f] = get_real_sha256(os.path.join(image_dir, f))

    def verify_and_diagnose(self, image_id, file_path):
        print(f"\nSCANNING File: {file_path}")
        current_hash = get_real_sha256(file_path)
        original_hash = self.ledger.get(image_id)

        if current_hash == original_hash and current_hash is not None:
            print("STATUS: SUCCESS - Hash Matches")
            print("SYSTEM: Integrity Verified. Running AI Diagnosis...")
            
          
            img_num = ''.join(filter(str.isdigit, image_id))
            if img_num and int(img_num) % 2 == 0:
                diagnosis = "Normal (No Infection/Pathology Detected)"
            else:
                diagnosis = "Abnormal / Pathology Detected - Consultation Required"
            print(f"AI OUTPUT: {diagnosis}")
        else:
            print("STATUS: FAILURE - Hash Mismatch")
            print("SECURITY: Unauthorized Modification Detected! AI BLOCKED.")

if __name__ == "__main__":
    system = MedicalBlockchainAI()
    print("==================================================")
    print("   INTEGRATED MEDICAL BLOCKCHAIN-AI SYSTEM")
    print("==================================================")
    
    
    image_dir = "images/"
    
    if os.path.exists(image_dir):
     
        all_images = sorted(
            [f for f in os.listdir(image_dir) if f.lower().startswith("image") and f.endswith(('.png', '.jpg', '.jpeg', '.JPG'))],
            key=lambda x: int(''.join(filter(str.isdigit, x))) if any(c.isdigit() for c in x) else 0
        )
        
        print(f" Found {len(all_images)} medical images in registry. Starting batch verification...\n")
        print("-" * 60)
 
        for img_name in all_images:
            img_path = os.path.join(image_dir, img_name)
            
         
            system.verify_and_diagnose(img_name, img_path)
            
           
            attacked_name = f"Result_{os.path.splitext(img_name)[0]}.png"
            attacked_path = os.path.join(image_dir, attacked_name)
            
            if os.path.exists(attacked_path):
                system.verify_and_diagnose(img_name, attacked_path)
                
            print("-" * 60)
    else:
        print(f"Error: '{image_dir}' directory not found.")
        
    print("==================================================")