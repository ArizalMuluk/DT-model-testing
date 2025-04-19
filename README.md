# Iris Flower Prediction Application

A simple web application to predict the species of iris flowers based on sepal and petal measurements using a Decision Tree Classifier model.

## Description

This application is built using Flask as the web framework and utilizes a machine learning model trained on the famous Iris dataset. The Iris dataset contains measurements of three different species of iris flowers (setosa, versicolor, and virginica).

The Decision Tree Classifier model is trained using scikit-learn and saved using pickle for use in the web application.

## Features

- A simple web interface for entering iris flower measurements.
- Real-time prediction of iris flower species based on the entered measurements.
- Error handling for invalid input.

## How the Model Works

The machine learning model is trained with the Iris dataset through the following steps:
1. Load the Iris dataset from scikit-learn.
2. Split the data into features (X) and target (y).
3. Split the dataset into training and testing data (81% training, 19% testing).
4. Train the Decision Tree Classifier model on the training data.
5. Evaluate the model using the testing data.
6. Save the model in pickle format for use in the web application.

## How to Use

1. Make sure all dependencies are installed by running:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser and go to `http://127.0.0.1:5000/`.

4. Enter the sepal and petal measurements (length and width) in the provided form.

5. Click the "Predict" button to see the predicted species of the iris flower.

## Project Structure

- `app.py` - The main file for the Flask application.
- `iris_decision_tree_model.pkl` - The trained machine learning model.
- `templates/index.html` - The HTML template for the web interface.
- `pert1.ipynb` - Jupyter notebook containing the model training process.

## Technologies Used

- Python 3
- Flask
- scikit-learn
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Pickle

## Notes

Ensure that the model file `iris_decision_tree_model.pkl` is located in the same directory as `app.py` for the application to run smoothly.

## Disclaimer

This project is created for educational purposes only and is intended for practice. 

## Reference

For more information about the Iris dataset, visit: [Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
