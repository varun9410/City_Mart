from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import json
import pandas as pd

app = Flask(__name__)

def extract_features(image_path):
    model = VGG16(weights='imagenet', include_top=False)
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    # Preprocess the input image for the VGG16 model
    x = preprocess_input(img_array)
    # Extract features from the pre-trained VGG16 model
    features = model.predict(np.array([x]))
    # Flatten the features to a 1D vector
    features = features.squeeze()
    return features
@app.route('/find_product', methods=['POST'])
def find_product():
    image_file = request.files['image']
    image_path = 'temp.jpg'  # Temporary file to save the uploaded image
    image_file.save(image_path)
    feature = extract_features(image_path)
    
    result = []
    data = pd.read_csv('feature.csv')
    for i, row in data.iterrows():
        feature2 = np.array(eval(row['feature']))
        cosine_sim = cosine_similarity(feature.reshape(1, -1), feature2.reshape(1, -1)).mean()
        result_dict = {'id': row['id'], 'cosine_similarity': cosine_sim}
        result.append(result_dict)
    result = sorted(result, key=lambda x: x['cosine_similarity'], reverse=True)
    top_5_result = [item['id'] for item in result[:5]]
    return jsonify(top_5_result)
if __name__ == '__main__':
    app.run(debug=True)