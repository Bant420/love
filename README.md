# 👕 VisionWear AI – Fashion Image Classification Web App

VisionWear AI is an end-to-end deep learning project that classifies fashion images into categories such as T-shirt, Dress, Sneaker, Bag, etc. The system is built using an Artificial Neural Network (ANN) and deployed as a web application using Flask.

---

## 📌 Project Overview

This project demonstrates how a deep learning model can be integrated into a real-world application. It covers the full pipeline from model training to deployment.

We trained an ANN model on the Fashion MNIST dataset and integrated it into a Flask web application where users can upload images and get predictions instantly.

---

## ⚙️ How the System Works

1. The user uploads a fashion image through the web interface
2. The image is saved on the server
3. Preprocessing is applied:

   * Convert image to grayscale
   * Resize to 28 × 28 pixels
   * Normalize pixel values (0–1 range)
4. The processed image is passed to the trained ANN model
5. The model predicts the class and confidence score
6. The result is displayed along with the uploaded image

---

## 🧠 Model Details

* Model Type: Artificial Neural Network (ANN)
* Framework: TensorFlow / Keras
* Dataset: Fashion MNIST
* Input Shape: 28 × 28 grayscale image
* Output Classes: 10 categories

  * T-shirt/top
  * Trouser
  * Pullover
  * Dress
  * Coat
  * Sandal
  * Shirt
  * Sneaker
  * Bag
  * Ankle boot

---

## 🚀 Features

* Upload and classify fashion images
* Real-time prediction
* Confidence score display
* Clean and interactive UI
* Multiple image uploads supported
* Ready for deployment (Render / Docker)

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* Flask
* OpenCV
* NumPy
* HTML / CSS

---

## 📂 Project Structure

```
visionwear-ai/
│
├── app.py                # Flask backend
├── ANN.h5               # Trained model
├── requirements.txt     # Dependencies
├── templates/
│     └── index.html     # UI
├── static/
│     └── uploads/       # Uploaded images
```

---

## ▶️ Run the Project Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/visionwear-ai.git
cd visionwear-ai
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## 🐳 Docker (Optional)

```
docker build -t visionwear-app .
docker run -p 5000:5000 visionwear-app
```

---

## 🌐 Deployment

This project can be deployed on:

* Render
* Hugging Face Spaces
* Streamlit Cloud

---

## 📈 Future Improvements

* Use CNN instead of ANN for better accuracy
* Add drag-and-drop upload
* Improve UI/UX
* Add user authentication

---

## 👨‍💻 Author

Name : Vaibhav Chaudhari  
Email : chaudharivaibhav471@gmail.com
linkdin : www.linkedin.com/in/vaibhav-chaudhari1
GitHub : https://github.com/chaudharivaibhav471

---

## ⭐ Conclusion

This project demonstrates how deep learning models can be integrated into real-world applications. It covers the complete pipeline from model training, preprocessing, and prediction to web deployment, making it a strong portfolio project.
