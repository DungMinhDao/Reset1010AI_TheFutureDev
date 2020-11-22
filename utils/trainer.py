from sklearn.cluster import KMeans

def build_model(n_clusters=30):
    model = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=500, n_init=15)
    return model

def train(model, vectorizer, texts):
    X = vectorizer.transform(list(texts))
    model.fit(X)
    return model

def infer(model, vectorizer, texts):
    X = vectorizer.transform(list(texts))
    pred = model.predict(X)    
    return pred