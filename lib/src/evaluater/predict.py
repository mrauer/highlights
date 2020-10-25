import argparse
import glob
import json
import os

from handlers.data_generator import TestDataGenerator
from handlers.model_builder import Nima
from utils.utils import calc_mean_score

TECHNICAL_HDF5 = 'weights_mobilenet_technical_0.11.hdf5'


def image_file_to_json(img_path):
    img_dir = os.path.dirname(img_path)
    img_id = os.path.basename(img_path).split('.')[0]

    return img_dir, [{'image_id': img_id}]


def image_dir_to_json(img_dir, img_type='jpg'):
    img_paths = glob.glob(os.path.join(img_dir, '*.'+img_type))

    samples = []
    for img_path in img_paths:
        img_id = os.path.basename(img_path).split('.')[0]
        samples.append({'image_id': img_id})

    return samples


def predict(model, data_generator):
    return model.predict_generator(
        data_generator, workers=8, use_multiprocessing=True, verbose=1)


def store_output(filename, output):
    f = open('/'.join(['/src/output', filename]), 'w')
    f.write(output)
    f.close()


def main(base_model_name, weights_file, image_source,
         predictions_file, img_format='jpg'):
    # load samples
    if os.path.isfile(image_source):
        image_dir, samples = image_file_to_json(image_source)
    else:
        image_dir = image_source
        samples = image_dir_to_json(image_dir, img_type='jpg')

    # build model and load weights
    nima = Nima(base_model_name, weights=None)
    nima.build()
    nima.nima_model.load_weights(weights_file)

    # initialize data generator
    data_generator = TestDataGenerator(
        samples, image_dir, 64, 10,
        nima.preprocessing_function(),
        img_format=img_format)

    # get predictions
    predictions = predict(nima.nima_model, data_generator)

    # calc mean scores and add to samples
    for i, sample in enumerate(samples):
        sample['mean_score_prediction'] = calc_mean_score(predictions[i])

    output = json.dumps(samples, indent=2)
    print(output)

    filename = 'technical.txt' if os.environ['PREDICT_MODEL'].find(
        TECHNICAL_HDF5) != -1 else 'aesthetic.txt'

    store_output(filename, output)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--base-model-name', help='CNN base model name', required=True)
    parser.add_argument('-w', '--weights-file', help='path of weights file', required=True)
    parser.add_argument('-is', '--image-source', help='image directory or file', required=True)
    parser.add_argument('-pf', '--predictions-file', help='file with predictions',
                        required=False, default=None)

    args = parser.parse_args()

    main(**args.__dict__)
