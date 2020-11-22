import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
re_tok = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')


def text_normalize(text: str):
    text = re.sub("'ll", " ", text)
    text = re.sub("-", " ", text)
    text = re.sub(" +", " ", text)
    return text


def _tokenize(s: str):
    return re_tok.sub(r' \1 ', s).split()


vectorizer = TfidfVectorizer(ngram_range=(1, 2), tokenizer=_tokenize,
                            min_df=3, max_df=0.9, strip_accents='unicode', use_idf=1,
                            smooth_idf=1, sublinear_tf=1)
