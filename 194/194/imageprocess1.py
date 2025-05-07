def go(filename):
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
    from PIL import Image, ImageEnhance, ImageFilter

    def load_image(path):
        return cv2.imread(path, cv2.IMREAD_COLOR)

    def noise_reduction(img):
        return cv2.GaussianBlur(img, (5, 5), 0)

    def contrast_enhancement(img):
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    def sharpen_image(img):
        kernel = np.array([[-1, -1, -1], 
                        [-1, 9, -1], 
                        [-1, -1, -1]])
        return cv2.filter2D(img, -1, kernel)

    def edge_detection(img):
        return cv2.Canny(img, 100, 200)

    def region_of_interest(img):
        # Define a simple square ROI
        h, w = img.shape[:2]
        top_left = (int(w*0.25), int(h*0.25))
        bottom_right = (int(w*0.75), int(h*0.75))
        # Create a mask for the ROI
        mask = np.zeros_like(img)
        cv2.rectangle(mask, top_left, bottom_right, (255, 255, 255), -1)
        masked_img = cv2.bitwise_and(img, mask)
        return masked_img

    # Load the image
    image_path = filename # r"C:\Users\asus\Downloads\distal-humeral-fractures-2-_JPEG.rf.39ba3f53047ecb4064613850a1c76fc1.jpg" # Specify the path to your image
    original = load_image(image_path)

    # Apply preprocessing steps
    gaussian_blur = noise_reduction(original)
    contrast = contrast_enhancement(gaussian_blur)
    sharpened = sharpen_image(contrast)
    edges = edge_detection(sharpened)
    roi = region_of_interest(edges)

    # Display results
    def show_image(img, title="Image", cmap=None):
        plt.figure(figsize=(6, 6))
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis('off')
        plt.show()

    # show_image(original, "Original")
    # show_image(gaussian_blur, "Noise Reduced - Gaussian Blur")
    # show_image(contrast, "Contrast Enhanced - Histogram Equalization")
    # show_image(sharpened, "Sharpened Image")
    # show_image(edges, "Edge Detection")
    # show_image(roi, "Region of Interest")

    images=[original, gaussian_blur, contrast, sharpened, edges, roi]
    titles=['original', 'gaussian_blur', 'contrast', 'sharpened', 'edges', 'roi']

    import matplotlib.pyplot as plt 
    # Create a 2x3 grid for subplots
    fig, axes = plt.subplots(2, 3, figsize=(10, 6))

    # Iterate over images and plot them on subplots
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')  # Display each image
        ax.axis('off')  # Turn off axis
        ax.set_title(titles[i])  # Set title for each subplot

        
    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plot
    plt.show()