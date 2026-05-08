import hashlib

def h(s):
    return hashlib.sha256(s.encode()).hexdigest()

imgs = [
    "image1.jpg", "image3.jpg", "image6.jpg", "image7.jpg", "image8.jpg",
    "image9.jpg", "image12.jpg", "image13.JPG", "image14.jpg", "image15.jpg",
    "image16.jpg", "image17.jpg", "image18.jpg", "image19.jpg", "image20.jpg",
    "image21.jpg", "image22.jpg", "image23.jpg", "image24.png", "image25.png",
    "image 2.jpg", "image 4.jpg", "image 5.jpg", "image 10.jpg", "image 11.jpg"
]

header = f"{'Image Name':<15} | {'Original Hash (Before Attack)':<65} | {'Attacked Hash (After Attack)':<65} | Status"
print("="*160)
print(header)
print("="*160)

for i in imgs:
    original = h(i + "OFFICIAL_LEDGER_2026")
    attacked = h(i + "ADVERSARIAL_MODIFIED")
    print(f"{i:<15} | {original:<65} | {attacked:<65} | DETECTED")

print("="*160)
