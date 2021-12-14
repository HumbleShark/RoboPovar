from keras.preprocessing import image
import numpy as np
from keras.applications.inception_v3 import preprocess_input
from keras.models import model_from_json

with open('data/labels.txt', 'r') as f:
    food101 = [l.strip().lower() for l in f]

# load json and create model
json_file = open('saved_models/food101_final_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("saved_models/food101_final_model.h5")

model = loaded_model


def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(299, 299))
    # convert PIL.Image.Image type to 3D tensor with shape (299, 299, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 299, 299, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)


def img_analysis(img_path):
    # process image
    img = path_to_tensor(img_path)
    img = preprocess_input(img)

    # make prediction
    predicted_vec = model.predict(img)
    predicted_label = food101[np.argmax(predicted_vec)]
    return predicted_label


if __name__ == '__main__':
    print(img_analysis('test_imgs/chicken_wings.jpg'))
