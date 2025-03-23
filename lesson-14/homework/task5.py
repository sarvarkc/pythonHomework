import numpy as np
from PIL import Image

def flip_image(x):
    with Image.open("birds.jpg") as img:
        if x == 1:
            img_arr = np.array(img)
            flip_img_arr = img_arr[:,::-1]
            flip_img = Image.fromarray(flip_img_arr)
            flip_img.save("birds_reverse.jpg")
        else:
            img_arr = np.array(img)
            flip_img_arr = img_arr[::-1,:]
            flip_img = Image.fromarray(flip_img_arr)
            flip_img.save("birds_updown.jpg")

def add_noise():
    with Image.open("birds.jpg") as img:
        image_array = np.array(img, dtype=np.uint8)

        noise = np.random.randint(-50, 50, image_array.shape, dtype=np.int16)

        noisy_image_array = image_array.astype(np.int16) + noise

        noisy_image_array = np.clip(noisy_image_array, 0, 255).astype(np.uint8)

        noisy_image = Image.fromarray(noisy_image_array)

        noisy_image.save("birds_noisy.jpg")

def brighten():
    with Image.open("birds.jpg") as img:
        image_array = np.array(img)

        brightened_image_array = image_array.copy()

        brightened_image_array[:, :, 0] += 40

        brightened_image_array = np.clip(brightened_image_array, 0, 255)

        brightened_image = Image.fromarray(brightened_image_array.astype(np.uint8))

        brightened_image.save("birds_brightened.jpg")

def mask():
    with Image.open("birds.jpg") as img:
        image_array = np.array(img)

        height, width, _ = image_array.shape

        center_y, center_x = height // 2, width // 2

        mask_size = 100
        start_y, start_x = center_y - mask_size // 2, center_x - mask_size // 2
        end_y, end_x = start_y + mask_size, start_x + mask_size

        image_array[start_y:end_y, start_x:end_x] = [0, 0, 0]

        masked_image = Image.fromarray(image_array.astype(np.uint8))

        masked_image.save("birds_masked.jpg")



flip_image(1)
flip_image(2)
add_noise()
brighten()
mask()
