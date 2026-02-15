import numpy as np
from PIL import Image

def extract_full_width_flag(filename):
    W_TOTAL = 800
    CHANNEL = 1

    with open(filename, "rb") as f:
        raw = f.read()

    data = np.frombuffer(raw, dtype=np.uint8)
    num_pixels = len(data) // 4
    num_lines = num_pixels // W_TOTAL

    frame = data[:num_lines * W_TOTAL * 4].reshape((num_lines, W_TOTAL, 4))
    
    lsb_data = (frame[:, :, CHANNEL] & 1) * 255
    
    final_image = Image.fromarray(lsb_data.astype(np.uint8), 'L')
    final_image.save("flag_complet.png")
    
    print(f"Image générée : flag_complet.png ({W_TOTAL}x{num_lines})")
    print("Le flag devrait apparaître quelque part au milieu de l'image.")

if __name__ == "__main__":
    extract_full_width_flag("signal2.bin")
