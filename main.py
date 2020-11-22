import pandas as pd

from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer

from tqdm import tqdm

from utils.text import text_normalize, vectorizer
from utils.file import load_model
from utils.trainer import build_model, train, infer

tqdm.pandas()


def course_retrieval(model, vectorizer, text, n_outputs=10):
    assert n_outputs <= 30, "Number output exceeds the cardi"
    str_input = [text]

    prediction_inp = infer(model, vectorizer, str_input)
    prediction_inp = int(prediction_inp)
    temp_df = course_df.loc[course_df['ClusterPrediction'] == prediction_inp]
    temp_df = temp_df.iloc[:n_outputs]
    outputs = {row["CourseId"]:row["Description"] for index, row in temp_df.iterrows()}
    return outputs

def get_data(file_path="database/courses_data.csv"):
    # process text
    courses_df = pd.read_csv("database/courses_data.csv")
    courses_df = courses_df.dropna(how='any')
    processed_course_df = courses_df.CourseId.str.cat(
        " "+courses_df.CourseTitle.str.cat(" "+courses_df.Description))
    processed_course_df = processed_course_df.progress_apply(text_normalize)
    return processed_course_df


if __name__ == '__main__':

    processed_course_df = get_data("database/courses_data.csv")

    # init and train model
    # vectorizer = TfidfVectorizer(stop_words='english')
    # model = build_model(n_clusters=30)
    # train(model, vectorizer, processed_course_df)

    # save_model(vectorizer, 'database/tf_idf_vectorizer.pkl')
    # save_model(model, 'database/kmeans_model.pkl')

    # load pretrained model + vectorizer
    vectorizer = load_model('database/tf_idf_vectorizer.pkl')
    model = load_model("database/kmeans_model.pkl")

    # inference and cached output
    # course_df = pd.read_csv("database/courses_data.csv")
    # course_df = course_df[course_df.IsCourseRetired == 'no']
    # course_df['InputString'] = course_df.CourseId.str.cat(" "+course_df.CourseTitle.str.cat(" "+course_df.Description))
    # course_df['InputString'] = course_df['InputString'].progress_apply(text_normalize)
    # course_df['ClusterPrediction'] = ""
    # course_df['ClusterPrediction'] = course_df.apply(
    #     lambda x: cluster_predict(course_df['InputString']), axis=0)

    # course_df.to_csv("database/predicted_data.csv", index=False)

    # load cluster text
    course_df = pd.read_csv("database/predicted_data.csv")

    outputs = course_retrieval(model, vectorizer, "A sql server course for beginner level", n_outputs=5)
    for course_id, desc in outputs.items():
        print("*"*50)
        print(course_id)
        print(desc)