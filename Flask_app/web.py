
from flask import Flask,render_template,request
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

app=Flask(__name__)
model=pickle.load(open('classifier.pkl','rb'))
loaded_vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    data =request.values['message']
    data = re.sub('[^a-zA-Z]', ' ', data)
    data=data.lower()
    data=data.split()
    lemmatizer=WordNetLemmatizer()
    data = [lemmatizer.lemmatize(word) for word in data if not word in stopwords.words('english')]
    data = ' '.join(data)
    data = [data]
    vect = loaded_vectorizer.transform(data).toarray()
    my_prediction = model.predict(vect)
    return render_template('result.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run()