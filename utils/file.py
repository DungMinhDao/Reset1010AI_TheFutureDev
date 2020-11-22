import pickle


def save_model(model, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(vectorizer, f)

def load_model(file_path):
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model
