from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model yang sudah disimpan
try:
    model = pickle.load(open('iris_decision_tree_model.pkl', 'rb'))
except FileNotFoundError:
    print("Error: File model 'iris_decision_tree_model.pkl' tidak ditemukan. Pastikan file ini ada di direktori yang sama dengan app.py.")
    model = None

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST' and model:
        print("Data dari formulir:", request.form) # Tambahkan baris ini
        try:
            sepal_length = float(request.form['sepal_length'])
            sepal_width = float(request.form['sepal_width'])
            petal_length = float(request.form['petal_length'])
            petal_width = float(request.form['petal_width'])

            features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            predicted_class = model.predict(features)[0]
            iris_names = ['setosa', 'versicolor', 'virginica']
            prediction = iris_names[predicted_class]
        except ValueError:
            prediction = "Masukkan nilai numerik yang valid untuk semua fitur."
        except Exception as e:
            prediction = f"Terjadi kesalahan saat melakukan prediksi: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)