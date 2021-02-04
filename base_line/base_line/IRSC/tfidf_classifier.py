import numpy as np
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from feature_extractors import bow_extractor, tfidf_extractor
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def get_metrics(true_labels, predicted_labels):
    # evaluation metrics    
    print('Accuracy:', np.round(metrics.accuracy_score(true_labels, predicted_labels), 4)) 
    print('Precision:', np.round(metrics.precision_score(true_labels, predicted_labels), 4)) 
    print('Recall:', np.round(metrics.recall_score(true_labels, predicted_labels), 4)) 
    print('F1 Score:', np.round(metrics.f1_score(true_labels, predicted_labels), 4)) 
     

# Running ML algorithms 
def train_predict_evaluate_model(classifier, \
                                 train_features, train_labels,\
                                 test_features, test_labels):
    # build model                                
    classifier.fit(train_features, train_labels)
    # predict using model
    predictions = classifier.predict(test_features) 
    # evaluate model prediction performance
    get_metrics(true_labels=test_labels, predicted_labels=predictions) 
    return predictions  

train_data = []
train_labels = []
with open('./data/train_doc_label', 'r') as corpus:
    for line in corpus: 
        doc, label = line.strip().split('\t')
        train_data.append(doc)
        train_labels.append(int(label))

test_data = []
test_labels = []
with open('./data/test_doc_label', 'r') as corpus:
    for line in corpus: 
        doc, label = line.strip().split('\t')
        test_data.append(doc)
        test_labels.append(int(label))

# tfidf features
tfidf_vectorizer, tfidf_train_features = tfidf_extractor(train_data)  
tfidf_test_features = tfidf_vectorizer.transform(test_data) 

print(type(tfidf_train_features), tfidf_train_features.shape)
print(type(tfidf_test_features), tfidf_test_features.shape)

mnb = MultinomialNB()
svm = SGDClassifier(loss="hinge", penalty="l2", max_iter=20)
svc = SVC(kernel="rbf", C=0.025, probability=True)
dt = DecisionTreeClassifier()
rf = RandomForestClassifier()
gbc = GradientBoostingClassifier()
abc = AdaBoostClassifier()
nusvc = NuSVC(probability=True)
mlp = MLPClassifier(random_state=1, max_iter=300)
# lda = LinearDiscriminantAnalysis()

classifier = abc 
# Multinomial Naive Bayes with tfidf features
# mnb_tfidf_predictions = train_predict_evaluate_model(classifier=mnb,\
#                                                      train_features=tfidf_train_features,\
#                                                      train_labels=train_labels,\
#                                                      test_features=tfidf_test_features,\
#                                                      test_labels=test_labels)

svm_tfidf_predictions = train_predict_evaluate_model(classifier=classifier, \
                                                     train_features=tfidf_train_features, \
                                                     train_labels=train_labels, \
                                                     test_features=tfidf_test_features, \
                                                     test_labels=test_labels)


