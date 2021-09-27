# Document-Topic-Prediction

## Dataset
Here I used the bbc news dataset which contained 5 topics (business, entertainment, tech, sport, politics). Under each topic, data was provided as separate text file for each news. First of all, I processed the files using Python to generate an excel file which contained details of document topic, document title and document content. The prepared excel data was used for building the model. 
## Model Building
* During the ML model building, first the textual data(document content) was preprocessed by removing unnecessary characters and stopwords. After lemmatization, bag of words model was used for vectorizing the textual data. The vectorizer was saved as pickle file for the implementation in flask.
* The target (document topic) contained 5 values(multi-class classification problem) and it was label encoded by using the map function.
* Then data was splitted in train and test set in the 80-20 % ratio.
* 3 models( Multinomial NB, SVM and Decision Tree) used for making prediction. The best model obtained was Multinomial NB (best accuracy and least no.of miss classifications) and created a pickle file of the model
* Here Flask app is implemented using these pickle files.
