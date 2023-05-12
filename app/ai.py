import os
import codecs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import docx
import textract
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import AgglomerativeClustering
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
        print(f"K = {k}, Silhouette Average: {silhouette_avg}")

        if silhouette_avg > best_score:
            best_score = silhouette_avg
            best_k = k

    print(f"Best K: {best_k}, Best Silhouette Average: {best_score}")

    labels = KMeans(n_clusters=best_k, init='random', max_iter=400, n_init=10).fit_predict(X)
    cluster_labels = labels[file_names.index(file_name)]
    result = dict(zip(file_names, labels))
    cluster_files = [file_names[i] for i in range(len(file_names)) if labels[i] == cluster_labels]
    # for k in range(best_k):
    #     cluster_text = ' '.join([processed_data[i] for i, label in enumerate(labels) if label == k])
    #     wordcloud = WordCloud(max_font_size=50, max_words=100, background_color='white').generate(cluster_text)

    #     print(f'Cluster {k} Word Cloud:')
    #     plt.figure()
    #     plt.imshow(wordcloud, interpolation='bilinear')
    #     plt.axis('off')
    #     plt.savefig(f'wordcloud_cluster_{k}.png')
    #     plt.close()

    return cluster_files
# def cluster_files(folder_path, resume_folder, file_name):
#     data = []
#     file_names = []

#     for filename in os.listdir(folder_path):
#         with codecs.open(os.path.join(folder_path, filename), 'r', encoding='utf-8', errors='ignore') as file:
#             text = file.read()
#             data.append(text)
#             file_names.append(filename)
  
#     target_file_path = os.path.join(resume_folder, file_name)
#     if file_name.endswith('.docx'):
#         target_text = extract_text_from_docx(target_file_path)
#     elif file_name.endswith('.pdf'):
#         target_text = extract_text_from_pdf(target_file_path)
#     else:
#         return []

#     data.append(target_text)
#     file_names.append(file_name)

#     processed_data = [preprocess_text(text) for text in data]
#     vectorizer = TfidfVectorizer(stop_words='english')
#     X = vectorizer.fit_transform(processed_data)
#     best_silhouette_avg = -1
#     best_n_clusters = -1

#     for n_clusters in range(2, 10):
#         clustering = AgglomerativeClustering(n_clusters=n_clusters, affinity='cosine', linkage='complete')
#         labels = clustering.fit_predict(X.toarray())
#         silhouette_avg = silhouette_score(X, labels)

#         if silhouette_avg > best_silhouette_avg:
#             best_silhouette_avg = silhouette_avg
#             best_n_clusters = n_clusters

#     print("Optimal number of clusters:", best_n_clusters)

#     # Perform clustering with the optimal number of clusters
#     clustering = AgglomerativeClustering(n_clusters=best_n_clusters, affinity='cosine', linkage='complete')
#     labels = clustering.fit_predict(X.toarray())
#     try:
#         silhouette_avg = silhouette_score(X, labels)
#         print("Silhouette Average:", silhouette_avg)
#     except Exception as e:
#         print("Error calculating silhouette score:", e)

#     # Retrieve cluster labels and files in the same cluster as the target file
#     cluster_labels = labels[file_names.index(file_name)]
#     cluster_files = [file_names[i] for i in range(len(file_names)) if labels[i] == cluster_labels]

#     return cluster_files

    # Calculate Silhouette score
    
    # Print cluster labels
    # print("Cluster Labels:", labels)

    # # Retrieve files in the same cluster as the target file
    # cluster_files = [file_names[i] for i in range(len(file_names)) if labels[i] == cluster_labels]

    # return cluster_files
    # lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    # lda.fit(X)

    # labels = lda.transform(X).argmax(axis=1)
    # try:
    #     silhouette_avg = silhouette_score(X, labels)
    #     print("Silhouette Average:", silhouette_avg)
    # except Exception as e:
    #     print("Error calculating silhouette score:", e)

    # cluster_label = labels[file_names.index(file_name)]

    # clustered_files = [file_names[i] for i in range(len(file_names)) if labels[i] == cluster_label]

    # return clustered_files
    # best_score = -1
    # best_k = 2

    # for k in range(2, 10):
    #     kmeans = KMeans(n_clusters=k, init='random', max_iter=400, n_init=10)
    #     kmeans.fit(X)
    #     labels = kmeans.labels_
    #     # Calculate pairwise cosine similarity
    #     similarity_matrix = cosine_similarity(X)
    #     average_similarity = similarity_matrix.mean()
    #     print(f"K = {k}, Average Cosine Similarity: {average_similarity}")

    #     if average_similarity > best_score:
    #         best_score = average_similarity
    #         best_k = k

    # print(f"Best K: {best_k}, Best Average Cosine Similarity: {best_score}")
    #     silhouette_avg = silhouette_score(X, labels)
    #     print(f"K = {k}, Silhouette Average: {silhouette_avg}")

    #     if silhouette_avg > best_score:
    #         best_score = silhouette_avg
    #         best_k = k

    # print(f"Best K: {best_k}, Best Silhouette Average: {best_score}")

    # labels = KMeans(n_clusters=best_k, init='random', max_iter=400, n_init=10).fit_predict(X)
    # cluster_labels = labels[file_names.index(file_name)]
    # result = dict(zip(file_names, labels))
    # cluster_files = [file_names[i] for i in range(len(file_names)) if labels[i] == cluster_labels]
    # return cluster_files