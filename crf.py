import nltk
from nltk.corpus import cess_esp
nltk.download('conll2002')
nltk.download('cess_esp')
 
tagged_sentences = nltk.corpus.conll2002.tagged_sents()
tagged_sentences1 = cess_esp.tagged_sents()
 
print(tagged_sentences1[0])
print("Tagged sentences: ", len(tagged_sentences))
print("Tagged words:", len(nltk.corpus.conll2002.tagged_words()))

print("Tagged sentences: ", len(tagged_sentences1))
print("Tagged words:", len(cess_esp.tagged_words()))


from itertools import chain

import nltk
import sklearn
import scipy.stats
from sklearn.metrics import make_scorer
import sklearn_crfsuite
from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics


def features(sentence, index):
    """ sentence: [w1, w2, ...], index: the index of the word """
    return {
        'word': sentence[index],
        'is_first': index == 0,
        'is_last': index == len(sentence) - 1,
        'is_capitalized': sentence[index][0].upper() == sentence[index][0],
        'is_all_caps': sentence[index].upper() == sentence[index],
        'is_all_lower': sentence[index].lower() == sentence[index],
        'prefix-1': sentence[index][0],
        'prefix-2': sentence[index][:2],
        'prefix-3': sentence[index][:3],
        'suffix-1': sentence[index][-1],
        'suffix-2': sentence[index][-2:],
        'suffix-3': sentence[index][-3:],
        'prev_word': '' if index == 0 else sentence[index - 1],
        'next_word': '' if index == len(sentence) - 1 else sentence[index + 1],
        'has_hyphen': '-' in sentence[index],
        'is_numeric': sentence[index].isdigit(),
        'capitals_inside': sentence[index][1:].lower() != sentence[index][1:]
    }


from nltk.tag.util import untag
 
# Split the dataset for training and testing
cutoff = int(.15 * len(tagged_sentences1))
training_sentences = tagged_sentences1[:cutoff]
test_sentences = tagged_sentences1[cutoff:]
 
def transform_to_dataset(tagged_sentences1):
    X, y = [], []
 
    for tagged in tagged_sentences1:
        X.append([features(untag(tagged), index) for index in range(len(tagged))])
        y.append([tag for _, tag in tagged])
 
    return X, y
 
X_train, y_train = transform_to_dataset(training_sentences)
X_test, y_test = transform_to_dataset(test_sentences)
 
print(len(X_train))     
print(len(X_test))         
print(X_train[0])
print(y_train[0])



## Funcion que permite forzar el uso de GPU cuando estan presentes

#import tensorflow as tf
#sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))

from sklearn_crfsuite import CRF
model = CRF()
model.fit(X_train, y_train)

sentence = ['el', 'hombre', 'bajo','canta', 'bajo', 'el', 'puente', 'rojo','en','Sao','Paulo','en','la','escalera', 'baja']
def pos_tag(sentence):
    sentence_features = [features(sentence, index) for index in range(len(sentence))]
    return list(zip(sentence, model.predict([sentence_features])[0]))
 
print(pos_tag(sentence))  # [('I', 'PRP'), ('am', 'VBP'), ('Bob', 'NNP'), ('!', '.')]

from sklearn_crfsuite import metrics
 
y_pred = model.predict(X_test)
print(metrics.flat_accuracy_score(y_test, y_pred))
 
# 0.9602683593122289

i=0
while i<= 1:
    print(y_test[i])
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&COMPARAMOS')
    print(y_pred[i])
    i+=1