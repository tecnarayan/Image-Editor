from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
panda = np.array(Image.open('./albert.jpg').resize((3840, 2160)))

# Define a function to apply the red effect
def apply_red_effect(image):
    red_image = image.copy()
    red_image[:, :, 1:3] = np.zeros((2160, 3840, 2))
    return red_image

# Define a function to apply the blue effect
def apply_green_effect(image):
    green_image = image.copy()
    green_image[:, :, 0] = np.zeros((2160, 3840))
    green_image[:, :, 2] = np.zeros((2160, 3840))
    return green_image

# Define a function to apply the green effect
def apply_blue_effect(image):
    blue_image = image.copy()
    blue_image[:, :, 0] = np.zeros((2160, 3840))
    blue_image[:, :, 1] = np.zeros((2160, 3840))
    return blue_image

# Define a function to apply the black-and-white effect
def apply_black_and_white_effect(image):
    bw_image = image.copy()
    bw_image = bw_image[:, :, 0:3]
    bw_image[:, :, 0] = np.mean(bw_image, axis=2)
    bw_image[:, :, 1] = np.mean(bw_image, axis=2)
    bw_image[:, :, 2] = np.mean(bw_image, axis=2)
    return bw_image

# Define a function to apply the negative effect
def apply_negative_effect(image):
    negative_image = 255 - image
    return negative_image

# Define a function to create a sketch effect
def apply_sketch_effect(image, alpha_black=40):
    draw = image.copy()
    draw = draw[:, :, 0]
    
    # Pad the image to simplify the sketch effect calculations
    draw_pad0 = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
    draw_pad0[1:image.shape[0] + 1, 1:image.shape[1] + 1] = draw
    draw_pad = draw_pad0.copy()

    for h in range(image.shape[0]):
        for b in range(image.shape[1]):
            draw[h, b] = 0
            if np.abs(draw_pad[h+1, b+1] - draw_pad[h, b+1]) < alpha_black:
                pass
            else:
                draw[h, b] += np.abs(draw_pad[h+1, b+1] - draw_pad[h, b+1]) / 0.01

            if np.abs(draw_pad[h+1, b+1] - draw_pad[h+1, b]) < alpha_black:
                pass
            else:
                draw[h, b] += np.abs(draw_pad[h+1, b+1] - draw_pad[h+1, b]) / 0.01

            if np.abs(draw_pad[h+1, b+1] - draw_pad[h+2, b+1]) < alpha_black:
                pass
            else:
                draw[h, b] += np.abs(draw_pad[h+1, b+1] - draw_pad[h+2, b+1]) / 0.01

            if np.abs(draw_pad[h+1, b+1] - draw_pad[h+1, b+2]) < alpha_black:
                pass
            else:
                draw[h, b] += np.abs(draw_pad[h+1, b+1] - draw_pad[h+1, b+2]) / 0.01
            draw[h, b] = int(draw[h, b])
            draw[h, b] = min(draw[h, b], 255)

    draw_3 = np.zeros_like(image)
    draw_3[:, :, 0] = draw
    draw_3[:, :, 1] = draw
    draw_3[:, :, 2] = draw

    negative_sketch = 255 - draw_3
    return negative_sketch


# Apply the red effect
red_image = apply_red_effect(panda)
plt.imsave('red_effect.jpg', red_image.astype(np.uint8))

# Apply the blue effect
blue_image = apply_blue_effect(panda)
plt.imsave('blue_effect.jpg', blue_image.astype(np.uint8))

# Apply the green effect
green_image = apply_green_effect(panda)
plt.imsave('green_effect.jpg', green_image.astype(np.uint8))

# Apply the black-and-white effect
bw_image = apply_black_and_white_effect(panda)
plt.imsave('black_and_white_effect.jpg', bw_image.astype(np.uint8))

# Apply the negative effect
negative_image = apply_negative_effect(panda)
plt.imsave('negative_effect.jpg', negative_image.astype(np.uint8))

# Apply the sketch effect
sketch_image = apply_sketch_effect(panda)
plt.imsave('sketch_effect.jpg', sketch_image.astype(np.uint8))
