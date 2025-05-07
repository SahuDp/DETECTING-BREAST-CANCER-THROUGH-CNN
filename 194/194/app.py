import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder

# Load the model
model = load_model('model.h5')

# Initialize and fit the LabelEncoder with the class labels
class_labels = ['Benin', 'Malignant', 'Normal', 'Error']  # actual class labels
label_encoder = LabelEncoder()
label_encoder.fit(class_labels)


def load_preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.convert('L')  # Convert the image to grayscale
    img = img.resize((150, 150), Image.Resampling.LANCZOS)  # Resize the image to 150x150
    img_array = np.array(img)  # Convert image to an array
    img_array = img_array / 255.0  # Normalize pixel values to [0, 1]
    img_array = np.expand_dims(img_array, axis=-1)  # Add a channel dimension, as model expects (150, 150, 1)
    return img_array
def similarity(im1, im2):
    import numpy as np
    import cv2 
    # Load images using OpenCV
    image1 = cv2.imread(im1)
    image2 = cv2.imread(im2)

    # Ensure images have the same shape
    if image1.shape != image2.shape:
        raise ValueError("Images must have the same dimensions!")

    # Calculate squared difference between corresponding pixels
    squared_diff = np.square(image1 - image2).astype(np.float32)  # Ensure float for division

    # Mean Squared Error (average of squared differences)
    mse = np.mean(squared_diff)

    return mse

def predict_image(image_path):
    print(image_path)
    # Load and preprocess the image
    img = Image.open(image_path)
    img = img.convert('L')  # Convert the image to grayscale
    img = img.resize((150, 150), Image.Resampling.LANCZOS)  # Resize the image to 150x150
    img_array = np.array(img)  # Convert image to an array
    img_array = img_array / 255.0  # Normalize pixel values to [0, 1]
    img_array = np.expand_dims(img_array, axis=-1)  # Add a channel dimension, as model expects (150, 150, 1)

    preprocessed_image = img_array #  load_preprocess_image(image_path)
    if preprocessed_image is None:
        return "Failed to load or preprocess image"
    
    preprocessed_image = np.expand_dims(preprocessed_image, axis=0)  # Add batch dimension

    # Predict the class
    prediction = model.predict(preprocessed_image)
    predicted_class_index = np.argmax(prediction[0])
    try:
        if similarity(image_path, 'normal (1).png') < -0.3 and similarity(image_path, 'benign (1).png') < -0.3 and similarity(image_path, 'malignant (1).png') < -0.3 :
            return 'invalid' 
    except Exception as exp:
        print('..', exp)
    predicted_class_label = label_encoder.inverse_transform([predicted_class_index])[0]
    return predicted_class_label

def upload_action(event=None):
    filename1 = filedialog.askopenfilename()
    # filename = filename1.encode('utf-8')
    print(filename1)

    #import subprocess
    #subprocess.Popen(["python", "app.py"])
    import imageprocess1 
    imageprocess1.go(filename1)

    predicted_label = predict_image(filename1) # filename.decode('utf-8'))  # Decode filename to string using UTF-8
    label_text.set(f"Predicted Class Label: {predicted_label}")
    # Load image for display
    # img = Image.open(filename1)
    # img = img.convert('L')  # Convert to grayscale for display, if desired
    # img = img.resize((250, 250), Image.Resampling.LANCZOS)
    # img = ImageTk.PhotoImage(img)
    # panel.configure(image=img)
    # panel.image = img
    # tk.messagebox
    from tkinter import messagebox
    messagebox.showinfo("result", predicted_label)
    print('predicted label:',predicted_label)
    #img.show() # title=predicted_label)

root = tk.Tk()
root.title("Image Classification Prediction")

label_text = tk.StringVar()
label_text.set("Upload an image to predict its class")

btn = tk.Button(root, text='Upload an Image', command=upload_action)
btn.pack(side='top', pady=10)

panel = tk.Label(root)
panel.pack(side='top', fill='both', expand='yes')

result_label = tk.Label(root, textvariable=label_text, fg='blue')
result_label.pack(side='bottom', pady=10)

root.geometry("1200x600")  # width x height


root.mainloop()
