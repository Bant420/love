
# from flask import Flask, render_template, request
# import numpy as np
# import cv2
# import os
# from tensorflow.keras.models import load_model

# app = Flask(__name__)

# # Load model
# # model = load_model("ANN.h5", compile=False)
# model = load_model("ANN.keras", compile=False)

# # Class names
# class_names = [
#     "T-shirt/top", "Trouser", "Pullover", "Shirt", "Coat",
#     "Sandal", "T-shirt/top", "Sneaker", "Bag", "Ankle boot"
# ]

# # Upload folder
# UPLOAD_FOLDER = "static/uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # auto create folder

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# # Home route
# @app.route('/')
# def home():
#     return render_template("index.html")


# # Prediction route
# @app.route('/predict', methods=['POST'])
# def predict():
#     file = request.files['image']

#     if file:
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(filepath)

#         # Read and preprocess image
#         img = cv2.imread(filepath)
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         img = cv2.resize(gray, (28, 28))
#         img = img / 255.0
#         img = np.expand_dims(img, axis=0)

#         # Prediction
#         pred = model.predict(img)
#         confidence = round(np.max(pred) * 100, 2)
#         result = class_names[np.argmax(pred)]

#         return render_template(
#             "index.html",
#             prediction=result,
#             confidence=confidence,
#             image_path=filepath
#         )

#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=10000)

# from flask import Flask, render_template, request
# import numpy as np
# import cv2
# import os
# import requests
# from tensorflow.keras.models import load_model

# app = Flask(__name__)

# # ==============================
# # MODEL DOWNLOAD FROM HUGGING FACE
# # ==============================

# MODEL_PATH = "ANN.keras"
# MODEL_URL = "https://huggingface.co/vaibhav7025/visionwear-model/resolve/main/ANN.keras"

# # Download model if not exists
# if not os.path.exists(MODEL_PATH):
#     print("Downloading model from Hugging Face...")
#     r = requests.get(MODEL_URL)
#     with open(MODEL_PATH, "wb") as f:
#         f.write(r.content)

# # Load model
# model = load_model(MODEL_PATH, compile=False)

# # Class labels (Fashion MNIST)
# class_names = [
#     "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
#     "Sandal", "T-shirt/top", "Sneaker", "Bag", "Ankle boot"
# ]

# # ==============================
# # ROUTES
# # ==============================

# @app.route('/')
# def home():
#     return render_template("index.html")


# @app.route('/predict', methods=['POST'])
# def predict():
#     file = request.files['file']

#     # Create upload folder if not exists
#     upload_folder = "static/uploads"
#     if not os.path.exists(upload_folder):
#         os.makedirs(upload_folder)

#     filepath = os.path.join(upload_folder, file.filename)
#     file.save(filepath)

#     # Read image
#     img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
#     img = cv2.resize(img, (28, 28))
#     img = img / 255.0
#     img = img.reshape(1, 28, 28, 1)

#     # Prediction
#     pred = model.predict(img)
#     confidence = round(np.max(pred) * 100, 2)
#     result = class_names[np.argmax(pred)]

#     return render_template(
#         "index.html",
#         prediction=result,
#         confidence=confidence,
#         image_path=filepath
#     )

# if __name__ == "__main__":
#     app.run(debug=True)
# ==============================
# RUN APP (FOR RENDER)
# ==============================

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=10000)

# import os

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 10000))
#     app.run(host="0.0.0.0", port=port)






# from flask import Flask, render_template, request
# import numpy as np
# import cv2
# import os
# import requests
# from tensorflow.keras.models import load_model

# app = Flask(__name__)

# # ==============================
# # MODEL DOWNLOAD FROM HUGGING FACE
# # ==============================

# MODEL_PATH = "ANN.keras"
# MODEL_URL = "https://huggingface.co/vaibhav7025/visionwear-model/resolve/main/ANN.keras"

# # Download model if not exists
# if not os.path.exists(MODEL_PATH):
#     print("Downloading model from Hugging Face...")
#     r = requests.get(MODEL_URL)
#     r.raise_for_status()   # ✅ Important: ensures download success
#     with open(MODEL_PATH, "wb") as f:
#         f.write(r.content)

# # Load model
# print("Loading model...")
# model = load_model(MODEL_PATH, compile=False)
# print("Model loaded successfully!")

# # Class labels (Fashion MNIST)
# class_names = [
#     "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
#     "Sandal", "T-shirt/top", "Sneaker", "Bag", "Ankle boot"
# ]
# # class_names = [
# #     "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
# #     "Sandal", "T-shirt/top", "Sneaker", "Bag", "Ankle boot"
# # ]

# # ==============================
# # ROUTES
# # ==============================

# @app.route('/')
# def home():
#     return render_template("index.html")


# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get file
#         file = request.files.get('file')

#         if file is None or file.filename == "":
#             return render_template("index.html", prediction="No file uploaded")

#         # Create upload folder
#         upload_folder = "static/uploads"
#         os.makedirs(upload_folder, exist_ok=True)

#         filepath = os.path.join(upload_folder, file.filename)
#         file.save(filepath)

#         # Read image
#         img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

#         if img is None:
#             return render_template("index.html", prediction="Invalid image")

#         img = cv2.resize(img, (28, 28))
#         img = img / 255.0
#         img = img.reshape(1, 28, 28, 1)

#         # Prediction
#         pred = model.predict(img)
#         confidence = round(np.max(pred) * 100, 2)
#         result = class_names[np.argmax(pred)]

#         return render_template(
#             "index.html",
#             prediction=result,
#             confidence=confidence,
#             image_path=filepath
#         )

#     except Exception as e:
#         return render_template("index.html", prediction=f"Error: {str(e)}")


# # ==============================
# # IMPORTANT: NO app.run() FOR RENDER
# # ==============================

# # DO NOT add app.run()
# # Render uses: gunicorn app:app




# # new code 


# from flask import Flask, render_template, request
# import numpy as np
# import cv2
# import os
# import requests
# from tensorflow.keras.models import load_model

# app = Flask(__name__)

# # ==============================
# # MODEL DOWNLOAD FROM HUGGING FACE
# # ==============================

# MODEL_PATH = "model.h5"
# MODEL_URL = "https://huggingface.co/vaibhav7025/visionwear-model/resolve/main/model.h5"

# # Download model if not exists
# if not os.path.exists(MODEL_PATH):
#     print("Downloading model from Hugging Face...")
#     r = requests.get(MODEL_URL)
#     r.raise_for_status()  # ensure download success
#     with open(MODEL_PATH, "wb") as f:
#         f.write(r.content)

# # ==============================
# # LOAD MODEL SAFELY (VERY IMPORTANT)
# # ==============================

# try:
#     print("Loading model...")
#     model = load_model(MODEL_PATH, compile=False)
#     print("Model loaded successfully!")
# except Exception as e:
#     print("Model loading failed:", str(e))
#     model = None   # prevent crash

# # Class labels (Fashion MNIST)
# class_names = [
#     "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
#     "Sandal", "T-shirt/top", "Sneaker", "Bag", "Ankle boot"
# ]

# # ==============================
# # ROUTES
# # ==============================

# @app.route('/')
# def home():
#     return render_template("index.html")


# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Check model
#         if model is None:
#             return render_template("index.html", prediction="Model not loaded")

#         # Get file
#         file = request.files.get('file')

#         if file is None or file.filename == "":
#             return render_template("index.html", prediction="No file uploaded")

#         # Create upload folder
#         upload_folder = "static/uploads"
#         os.makedirs(upload_folder, exist_ok=True)

#         filepath = os.path.join(upload_folder, file.filename)
#         file.save(filepath)

#         # Read image
#         img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

#         if img is None:
#             return render_template("index.html", prediction="Invalid image")

#         img = cv2.resize(img, (28, 28))
#         img = img / 255.0
#         img = img.reshape(1, 28, 28, 1)

#         # Prediction
#         pred = model.predict(img)
#         confidence = round(np.max(pred) * 100, 2)
#         result = class_names[np.argmax(pred)]

#         return render_template(
#             "index.html",
#             prediction=result,
#             confidence=confidence,
#             image_path=filepath
#         )

#     except Exception as e:
#         return render_template("index.html", prediction=f"Error: {str(e)}")






# from flask import Flask, render_template, request
# import numpy as np
# import cv2
# import os
# import requests
# from tensorflow.keras.models import load_model

# app = Flask(__name__)

# # ==============================
# # MODEL DOWNLOAD FROM HUGGING FACE
# # ==============================

# MODEL_PATH = "model.h5"
# MODEL_URL = "https://huggingface.co/vaibhav7025/visionwear-model/resolve/main/model.h5"

# # Download model if not exists
# if not os.path.exists(MODEL_PATH):
#     print("Downloading model from Hugging Face...")
#     r = requests.get(MODEL_URL)
#     r.raise_for_status()
#     with open(MODEL_PATH, "wb") as f:
#         f.write(r.content)

# print("Model file exists:", os.path.exists(MODEL_PATH))
# print("Model file size:", os.path.getsize(MODEL_PATH))

# # ==============================
# # LOAD MODEL SAFELY
# # ==============================

# try:
#     print("Loading model...")
#     model = load_model(MODEL_PATH, compile=False)

#     # Important fix for .h5 models
#     model.make_predict_function()

#     print("✅ Model loaded successfully!")

# except Exception as e:
#     print("❌ Model loading failed:", str(e))
#     model = None

# # Class labels
# class_names = [
#     "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
#     "Sandal", "T-shirt/top", "Sneaker", "Bag", "Ankle boot"
# ]

# # ==============================
# # ROUTES
# # ==============================

# @app.route('/')
# def home():
#     return render_template("index.html")


# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         if model is None:
#             return render_template("index.html", prediction="Model not loaded")

#         file = request.files.get('file')

#         if file is None or file.filename == "":
#             return render_template("index.html", prediction="No file uploaded")

#         upload_folder = "static/uploads"
#         os.makedirs(upload_folder, exist_ok=True)

#         filepath = os.path.join(upload_folder, file.filename)
#         file.save(filepath)

#         img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

#         if img is None:
#             return render_template("index.html", prediction="Invalid image")

#         img = cv2.resize(img, (28, 28))
#         img = img / 255.0
#         img = img.reshape(1, 28, 28, 1)

#         pred = model.predict(img)
#         confidence = round(np.max(pred) * 100, 2)
#         result = class_names[np.argmax(pred)]

#         return render_template(
#             "index.html",
#             prediction=result,
#             confidence=confidence,
#             image_path=filepath
#         )

#     except Exception as e:
#         return render_template("index.html", prediction=f"Error: {str(e)}")

# # # ==============================
# # # ❌ DO NOT ADD app.run()
# # # Render uses: gunicorn app:app





from flask import Flask, render_template, request
import numpy as np
import cv2
import os
import requests
from tensorflow.keras.models import load_model

app = Flask(__name__)

# ==============================
# MODEL DOWNLOAD FROM HUGGING FACE
# ==============================

MODEL_PATH = "model_final.h5"
MODEL_URL = "https://huggingface.co/vaibhav7025/visionwear-model/resolve/main/model_final.h5"

# Download model if not exists
if not os.path.exists(MODEL_PATH):
    print("⬇️ Downloading model from Hugging Face...")
    r = requests.get(MODEL_URL)
    r.raise_for_status()
    with open(MODEL_PATH, "wb") as f:
        f.write(r.content)

print("✅ Model file exists:", os.path.exists(MODEL_PATH))
print("📦 Model file size:", os.path.getsize(MODEL_PATH))

# ==============================
# LOAD MODEL SAFELY
# ==============================

try:
    print("🔄 Loading model...")
    model = load_model(MODEL_PATH, compile=False)

    # Fix for .h5 models
    model.make_predict_function()

    print("✅ Model loaded successfully!")

except Exception as e:
    print("❌ Model loading failed:", str(e))
    model = None

# ==============================
# CLASS LABELS
# ==============================

class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

# ==============================
# ROUTES
# ==============================

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check model
        if model is None:
            return render_template("index.html", prediction="Model not loaded")

        file = request.files.get('file')

        if file is None or file.filename == "":
            return render_template("index.html", prediction="No file uploaded")

        # Save image
        upload_folder = "static/uploads"
        os.makedirs(upload_folder, exist_ok=True)

        filepath = os.path.join(upload_folder, file.filename)
        file.save(filepath)

        # Read image
        img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

        if img is None:
            return render_template("index.html", prediction="Invalid image")

        # Preprocess
        img = cv2.resize(img, (28, 28))
        img = img / 255.0
        img = img.reshape(1, 28, 28, 1)

        # Predict
        pred = model.predict(img)
        confidence = round(np.max(pred) * 100, 2)
        result = class_names[np.argmax(pred)]

        return render_template(
            "index.html",
            prediction=result,
            confidence=confidence,
            image_path=filepath
        )

    except Exception as e:
        return render_template("index.html", prediction=f"Error: {str(e)}")

# ==============================
# IMPORTANT: DO NOT USE app.run()
# Render uses gunicorn
# ==============================
# # # ==============================
