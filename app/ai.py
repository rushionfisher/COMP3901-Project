import os
import codecs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import docx
import textract

stopwords = nltk.corpus.stopwords.words('english')


def preprocess_text(text):
    words = nltk.word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word not in stopwords]
    return ' '.join(words)
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    paragraphs = [paragraph.text for paragraph in doc.paragraphs]
    return ' '.join(paragraphs)

def extract_text_from_pdf(file_path):
    text = textract.process(file_path).decode('utf-8')
    return text


def cluster_files(folder_path, file_name):
    data = []
    file_names = []
    #doc_to_text()
    for filename in os.listdir(folder_path):
        with codecs.open(os.path.join(folder_path, filename), 'r', encoding='utf-8', errors='ignore') as file:
            text = file.read()
            data.append(text)
            #print(text)
            file_names.append(filename)
    
    target_file_path = os.path.join("C:/Users/Shanice/Documents/COMP3901-Project/COMP3901-Project/resume_files", file_name)
    if file_name.endswith('.docx'):
        target_text = extract_text_from_docx(target_file_path)
    elif file_name.endswith('.pdf'):
        target_text = extract_text_from_pdf(target_file_path)
    else:
        return []
    print(target_text)
    data.append(target_text)
    file_names.append(file_name)

    processed_data = [preprocess_text(text) for text in data]
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(processed_data)
    kmeans = KMeans(n_clusters=2, init='random', max_iter=400, n_init=10)
    kmeans.fit(X)
    labels = kmeans.labels_
    print(labels)
    cluster_labels = labels[file_names.index(file_name)]
    result = dict(zip(file_names, labels))
    cluster_files = [file_names[i] for i in range(len(file_names)) if labels[i] == cluster_labels]
    return cluster_files