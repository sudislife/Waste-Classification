# Waste-Classification

An application which uses transfer learning in order to perform multi-class classification. The [MobileNetv2](https://keras.io/api/applications/mobilenet/#:~:text=%5Bsource%5D-,MobileNetV2%20function,-tf.keras) model was used for this project. The application will identify the type of waste and can advise the user a method of disposal of the waste type (Adheres to the [Recycling Guide for the City of Greater Geelong](https://www.geelongaustralia.com.au/recycling/guide/default.aspx?c=4268)).

## Streamlit Application

I'm using Python 3.10.11 for this project (So that I can utilize tensorflow GPU on Windows 11 witout WSL). In order to use the streamlit application, please run the following command in your prefered conda environment.

```terminal
pip install -r requirements.txt
```

After installing the requirements, start the application with...

```terminal
streamlit run image_classification.py
```

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

## What's the notebook?
This is my Deep Learning (SIT744) Assignment 2 for Trimester 1 of 2023. In case this assignment is reused in the future, feel free to take inspiration but **do not copy this** cause you will fall into trouble.

The notebook includes the following:

### SMOTE Preprocessing
For preprocessing, the [SMOTE](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html) technique was used in order to balance the classes. Additionally, the tensorflow ImageDataGenerator pipeling is used where a wide range of augmentation operations have been performed.

### Training the model
Used Early Stopping which monitors validation loss and accuracy

### Compare's Performance (Augmented vs Unaugmented Data) under equal time
Shows the difference in the amount of time the model takes to complete 1 epoch when SMOTE is and isn't applied.

