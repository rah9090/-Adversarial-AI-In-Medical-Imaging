import hashlib
from PIL import Image
import io
import os

def generate_image_hash(image_path):
    try:
        with Image.open(image_path) as img:
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format=img.format)
            return hashlib.sha256(img_byte_arr.getvalue()).hexdigest()
    except Exception as e:
        return f"Error: {e}"

def capture_from_device(image_name):
    path = f"images/{image_name}"
    if os.path.exists(path):
        print(f"[INPUT]: Image {image_name} captured from Medical Device.")
        print("[Security Layer]: Sending to Hyperledger Fabric...")
        img_hash = generate_image_hash(path)
        print(f"[Ledger]: Storing Hash: {img_hash}")
        return img_hash
    else:
        print(f"Error: Device could not find {image_name}")
        return None

if __name__ == "__main__":
    print("==================================================")
    print("    MEDICAL IMAGING DEVICE SIMULATION (DATA INPUT)")
    print("==================================================")
    
    image_dir = "images/"
    
    if os.path.exists(image_dir):
        all_images = sorted(
            [f for f in os.listdir(image_dir) if f.lower().startswith("image") and not f.startswith("Result_") and f.endswith(('.png', '.jpg', '.jpeg', '.JPG'))],
            key=lambda x: int(''.join(filter(str.isdigit, x))) if any(c.isdigit() for c in x) else 0
        )
        
        print(f"Device Initialized. Found {len(all_images)} images ready for ingestion.\n")
        print("-" * 60)
        
        for img_name in all_images:
            capture_from_device(img_name)
            print("-" * 60)
    else:
        print(f"Error: '{image_dir}' directory not found.")
        
    print("==================================================")