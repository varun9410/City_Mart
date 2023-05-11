import pandas as pd
from Shop.models import Product
import tensorflow as tf
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import json
import pandas as pd

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
products = Product.objects.all()
data = {'url': [], 'id': []}
for product in products:
    data['url'].append(product.image.url)  # Assuming 'image' is the field name for the image URL
    data['id'].append(product.id)
features=[]
for index, row in df.iterrows():
    feature = extract_features(row['url'][1:])
    if feature is not None:
        feature_dict = {}
        feature_dict['id'] = row['id']
        feature_dict['feature'] = feature.tolist()
        features.append(feature_dict)
dataframe = pd.DataFrame(features)
dataframe.to_csv('feature.csv', index=False)