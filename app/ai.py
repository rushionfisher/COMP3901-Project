import os
import codecs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import docx
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import AgglomerativeClustering
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import PyPDF2

stopwords = nltk.corpus.stopwords.words('english')

#Pre Processing
def preprocess_text(text):
    words = nltk.word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word not in stopwords]
    return ' '.join(words)

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    paragraphs = [paragraph.text for paragraph in doc.paragraphs]
    return ' '.join(paragraphs)

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


#function for k means clustering
def cluster_files(folder_path,resume_folder, file_name):

    data = []
    file_names = []

    for filename in os.listdir(folder_path):
        with codecs.open(os.path.join(folder_path, filename), 'r', encoding='utf-8', errors='ignore') as file:
            text = file.read()
            data.append(text)
            file_names.append(filename)
  
    target_file_path = os.path.join(resume_folder, file_name)
    if file_name.endswith('.docx'):
        target_text = extract_text_from_docx(target_file_path)
    elif file_name.endswith('.pdf'):
        target_text = extract_text_from_pdf(target_file_path)
    else:
        return []
    data.append(target_text)
    file_names.append(file_name)

    processed_data = [preprocess_text(text) for text in data]
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(processed_data)
    best_score = -1
    best_k = 2

    for k in range(2, 10):
        kmeans = KMeans(n_clusters=k, init='random', max_iter=400, n_init=10)
        kmeans.fit(X)
        labels = kmeans.labels_
        silhouette_avg = silhouette_score(X, labels)
        print('hello')
        print(f"K = {k}, Silhouette Average: {silhouette_avg}")

        if silhouette_avg > best_score:
            best_score = silhouette_avg
            best_k = k

    print(f"Best K: {best_k}, Best Silhouette Average: {best_score}")

    labels = KMeans(n_clusters=8, init='random', max_iter=400, n_init=10).fit_predict(X)
    cluster_labels = labels[file_names.index(file_name)]
    result = dict(zip(file_names, labels))
    cluster_files = [file_names[i] for i in range(len(file_names)) if labels[i] == cluster_labels]

    return cluster_files
