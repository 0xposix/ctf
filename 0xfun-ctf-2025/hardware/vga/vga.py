import numpy as np
from PIL import Image

TOTAL_WIDTH = 800
TOTAL_HEIGHT = 525
ACTIVE_WIDTH = 640
ACTIVE_HEIGHT = 480
BYTES_PER_PIXEL = 5

with open("signal.bin", "rb") as f:
    raw = f.read()

data = np.frombuffer(raw, dtype=np.uint8)

expected_size = TOTAL_WIDTH * TOTAL_HEIGHT * BYTES_PER_PIXEL
data = data[:expected_size]

frame = data.reshape((TOTAL_HEIGHT, TOTAL_WIDTH, BYTES_PER_PIXEL))

rgb_frame = frame[:, :, :3]

active = rgb_frame[0:ACTIVE_HEIGHT, 5:5+ACTIVE_WIDTH]

image = Image.fromarray(active, 'RGB')
image.save("vga.png")

print("Image reconstruite sauvegardée sous vga.png")
