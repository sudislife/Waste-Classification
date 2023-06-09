# Waste-Classification

An application which uses transfer learning in order to perform multi-class classification. The [MobileNetv2](https://keras.io/api/applications/mobilenet/#:~:text=%5Bsource%5D-,MobileNetV2%20function,-tf.keras) model was used for this project. The application will identify the type of waste and can advise the user a method of disposal of the waste type (Adheres to the [Recycling Guide for the City of Greater Geelong](https://www.geelongaustralia.com.au/recycling/guide/default.aspx?c=4268)).

## Dataset

The dataset used to train the model is the [Waste Classification PI](https://www.kaggle.com/datasets/alveddian/waste-classification-data) dataset which contains 8 classes:

1. Battery
2. Biological
3. Cardboard
4. Glass
5. Metal
6. Paper
7. Plastic
8. Trash

## Streamlit Application

I'm using Python 3.10.11 for this project (So that I can utilize tensorflow GPU on Windows 11 witout WSL). In order to use the streamlit application, please run the following command in your prefered conda environment.

```terminal
pip install -r requirements.txt
```

After installing the requirements, simply run...

```terminal
streamlit run image_classification.py
```
