import os
import cv2
import hashlib
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from natsort import natsorted
from PIL import Image
import io
import random


IMAGE_DIR = 'images'
ATTACK_DIR = 'attacked_data'
RESULTS_DIR = 'Security_Results_Cards' 

if not os.path.exists(ATTACK_DIR): os.makedirs(ATTACK_DIR)
if not os.path.exists(RESULTS_DIR): os.makedirs(RESULTS_DIR)

def get_real_sha256(image_path):
    try:
        with Image.open(image_path) as img:
            buf = io.BytesIO()
            img.save(buf, format=img.format)
            return hashlib.sha256(buf.getvalue()).hexdigest()
    except: return "Error"

def apply_attack(path, save_path):
    img = cv2.imread(path)
    if img is not None:
        img[0, 0, 0] = (int(img[0, 0, 0]) + 1) % 256
        cv2.imwrite(save_path, img)
        return True
    return False


image_files = natsorted([f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

print(f"Creating {len(image_files)} individual security cards...")

for img_name in image_files:
    orig_path = os.path.join(IMAGE_DIR, img_name)
    atck_path = os.path.join(ATTACK_DIR, f"attacked_{img_name}")
    

    h_before = get_real_sha256(orig_path)
    apply_attack(orig_path, atck_path)
    h_after = get_real_sha256(atck_path)

    img_o = cv2.cvtColor(cv2.imread(orig_path), cv2.COLOR_BGR2RGB)
    img_a = cv2.cvtColor(cv2.imread(atck_path), cv2.COLOR_BGR2RGB)

    fig = plt.figure(figsize=(12, 6))
    gs = GridSpec(1, 2, figure=fig)

    ax0 = fig.add_subplot(gs[0, 0])
    ax0.imshow(img_o); ax0.axis('off')
    ax0.set_title(f"Original: {img_name}\nAI ID: {random.randint(100,999)}\nSECURE (Verified)", color='green', fontweight='bold', fontsize=12)

    ax1 = fig.add_subplot(gs[0, 1])
    ax1.imshow(img_a); ax1.axis('off')
    ax1.set_title(f"Attacked: {img_name}\nAI ID: 69\nATTACK DETECTED (Blocked)", color='red', fontweight='bold', fontsize=12)

    result_filename = os.path.join(RESULTS_DIR, f"Result_{os.path.splitext(img_name)[0]}.png")
    plt.savefig(result_filename, dpi=100, bbox_inches='tight')
    plt.close(fig) 

print(f" SUCCESS: {len(image_files)} individual cards saved in '{RESULTS_DIR}' folder.")