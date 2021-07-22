# Importing the Libraries

from tensorflow.keras.models import load_model
import numpy as np
import pickle

def Predict_Next_Words(text,m):
    """
        In this function we are using the tokenizer and models trained
        and we are creating the sequence of the text entered and then
        using our model to predict and return the the predicted word.

    """
    # Load the model and tokenizer
    model = load_model('Model.h5')
    tokenizer = pickle.load(open('Data.pkl', 'rb'))

    print(text)
    listPredict = []

    sequence = tokenizer.texts_to_sequences([text])[0]
    for i in range(m):
        sequence = np.array(sequence)
        preds = model.predict_classes(sequence+i)
        predicted_word = ""
        for key, value in tokenizer.word_index.items():
            if value == preds:
                predicted_word = key
                listPredict.append(key)
                break

        k = len(listPredict)
    return listPredict

def run():
    while (True):

        text = input("Enter your line: ")

        if text == "stop the script":
            print("Ending The Program.....")
            break

        else:
            try:
                text = text.split(" ")
                text = text[-1]
                text = ''.join(text)
                m=Predict_Next_Words(text,5)
            except:
                continue
