import xlsxwriter
import xlrd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from gensim import corpora, models, similarities
import logging

from xlsxwriter.exceptions import FileCreateError


def show_course_info(course: list):
    assert len(course) == 3
    print("course name:           " + course[0])
    print("course intorduction:   " + course[1])
    print("course detail:         " + course[2])


def save(course_list:list):
    try:
        workbook = xlsxwriter.Workbook("coursera_corpus.xlsx")
        sheet1 = workbook.add_worksheet()
        if len(course_list[0]) == 0:
            workbook.close()
            return
        index = 1
        for i in course_list[0]:
            sheet1.write_row("A" + str(index), i)
            index += 1
        workbook.close()
    except FileCreateError as fe:
        print(fe)
    except PermissionError as pe:
        print(pe)





def read_file() -> list:
    workbook = xlrd.open_workbook("coursera_corpus.xlsx")
    sheet1 = workbook.sheet_by_index(0)
    total_rows = sheet1.nrows
    course_list = [[], []]

    for i in range(total_rows):
        temp = sheet1.row_values(rowx=i,start_colx=0,end_colx=3)
        course_list[0].append(temp)
        course_list[1].append(temp[0])

    return course_list



def upload_txt_data():
    with open("coursera_corpus.txt",encoding="utf-8") as f:
        lines = f.readlines()
    data = [[], []]
    for i in lines:
        temp = i.split("	")
        for i in range(len(temp)):
            temp[i] = temp[i].strip()
        assert len(temp) == 3
        data[0].append(temp)
        data[1].append(temp[0])
    f.close()
    save(data)


def similarity(course_list:list, courseindex:int) ->list:
    courses = [i[0] + " " + i[1] + " " + i[2] for i in course_list[0]]
    courses = [ i.encode("utf-8") for i in courses]
    courses_name = course_list[1]
    texts_tokenized = [[word.lower() for word in word_tokenize(document.decode('utf-8'))] for document in courses]
    english_stopwords = stopwords.words('english')
    texts_filtered_stopwords = [[word for word in document if not word in english_stopwords]
                                for document in texts_tokenized]
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    texts_filtered = [[word for word in document if not word in english_punctuations] for document in
                      texts_filtered_stopwords]
    st = LancasterStemmer()
    texts_stemmed = [[st.stem(word) for word in docment] for docment in texts_filtered]
    all_stems = sum(texts_stemmed, [])
    stems_once = set(stem for stem in set(all_stems) if all_stems.count(stem) == 1)
    texts = [[stem for stem in text if stem not in stems_once] for text in texts_stemmed]
    #logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10)
    index = similarities.MatrixSimilarity(lsi[corpus])
    ml_course = texts[courseindex]
    ml_bow = dictionary.doc2bow(ml_course)
    ml_lsi = lsi[ml_bow]
    sims = index[ml_lsi]
    sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
    return [courses_name[courseindex], sort_sims]



if __name__ == "__main__":
    upload_txt_data()