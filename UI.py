import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk
from tensorflow import keras

model = keras.models.load_model(r"C:\Users\ACER\Desktop\Jupyter\App\Model of Jv2.13 [99.27% acc] Dataset 5.1.1, Arch 1, 100 epoch, 16 batch size.h5")

# Defining the labels and image size
labels = ['PNEUMONIA', 'NORMAL', 'TUBERCULOSIS', 'COVID19']
img_size = 150

# Function to predict the class and display the result
def predict_class():
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return

    img_arr = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    resized_arr = cv2.resize(img_arr, (img_size, img_size))
    preprocessed_img = np.array(resized_arr) / 255.0
    preprocessed_img = preprocessed_img.reshape(-1, img_size, img_size, 1)
    prediction = model.predict(preprocessed_img)
    predicted_class = labels[np.argmax(prediction)]
    result_label.config(text=f"Predicted class: {predicted_class}")

    # Display the image in the image_label widget
    img = Image.fromarray(cv2.cvtColor(img_arr, cv2.COLOR_BGR2RGB))
    img.thumbnail((400, 400))  # Resize the image to fit within a specific size
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

# Create the main application window
app = tk.Tk()
app.title("Pneumonia Detection")
app.geometry("1920x720")

# Set the thick frame and background color for the window
frame_width = 50
app.config(borderwidth=frame_width, relief="groove", bg="black")

# Add a background image to the window
background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\ACER\Desktop\Jupyter\App\Background(1).png"))
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add a heading label
heading_label = tk.Label(app, text="Pneumonia Detection System using X-Ray Images", font=('Calibri', 20, 'bold'), bg='white')
heading_label.config(fg='black', padx=10, pady=5)
heading_label.pack(pady=20)

# Create the image label
image_label = tk.Label(app)
image_label.pack(pady=50)

# Create a custom rounded button style
def set_rounded_button_style(widget):
    widget.config(
        font=('Calibri', 16),
        background='#4CAF50',
        foreground='white',
        relief='solid',
        borderwidth=0,
        highlightthickness=0,
        padx=10,
        pady=5
    )
    widget.bind("<Enter>", lambda e: widget.config(background='#45a049'))
    widget.bind("<Leave>", lambda e: widget.config(background='#4CAF50'))

# Create the "Upload Image" button with custom styling
upload_button = tk.Button(app, text="Upload Image", command=predict_class)
set_rounded_button_style(upload_button)
upload_button.pack(pady=10)
upload_button.config(borderwidth=0, highlightthickness=0, padx=10, pady=5)

# Create a label to display the prediction result
result_label = tk.Label(app, text="", font=("Arial", 16))
result_label.config(fg='black', bg='#FFFFFF', padx=10, pady=5)
result_label.pack(pady=10)

app.mainloop()