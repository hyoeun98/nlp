# Topic Modeling
- 문서의 주제(topic)을 발견하기 위한 통계적 모델
- 검색 엔진, 민원 시스템 등 주제를 알아내는 일이 중요한 곳
### 잠재 의미 분석(Latent Semantic Analysis)
- BoW(Bag of Word에 기반한 DTM이나 TF-IDF는 단어의 frequency를 기반으로 하기 때문에 의미(토픽)를 고려하지 않음
- 쉽고 빠르게 구현 가능
- 새로운 정보에 대한 업데이트가 어려움
##### 특이값 분해(Singular Value Decomposition) # 링크

### 잠재 디리클레 할당(Latent Dirichlet Allocation)
- Assume : 문서들은 토픽들의 혼합, 토픽들은 확률 분포에 의해 단어들을 생성
- 문서의 생성 과정
  1. 문서에 사용할 단어의 개수를 정함
  2. 문서에 사용할 토픽의 혼합을 확률 분포에 의해 정함
  3. 문서에 사용할 토픽을 확률 분포에 의해 정함
  4. 문서에 사용할 단어를 토픽 내의 확률 분포에 의해 정함


- 사용자가 토픽을 개수를 정해야 함
  - 모델의 성능에 영향을 주는hyper parameter
- DTM, TF-IDF기반 -> 단어의 순서는 관련 없음
- 문서 내의 단어들 중 각 토픽에 해당하는 단어들의 비율
- 각 토픽 내에서 단어의 분포
- LSA : DTM을 Dimension Reduction하여 근접 단어들을 토픽으로 묶는다
- LDA : 단어가 특정 토픽에 존재할 확률과 문서에 특정 토픽이 존재할 확률을 결합하여 추정하여 토픽 추출
```
import pandas as pd
import urllib.request
urllib.request.urlretrieve("https://raw.githubusercontent.com/franciscadias/data/master/abcnews-date-text.csv", filename="abcnews-date-text.csv")
data = pd.read_csv('abcnews-date-text.csv', error_bad_lines=False)
text = data[['headline_text']]
```
data load

```
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
text['headline_text'] = text.apply(lambda row: nltk.word_tokenize(row['headline_text']), axis=1) # 토큰화
stop = stopwords.words('english')
text['headline_text'] = text['headline_text'].apply(lambda x: [word for word in x if word not in (stop)]) # 불용어 제거
text['headline_text'] = text['headline_text'].apply(lambda x: [WordNetLemmatizer().lemmatize(word, pos='v') for word in x]) # 표제어 추출
tokenized_doc = text['headline_text'].apply(lambda x: [word for word in x if len(word) > 3]) # 길이가 3 이하인 단어 제거
```
preprocessing

```
# 역토큰화 (토큰화 작업을 되돌림)
detokenized_doc = []
for i in range(len(text)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)

text['headline_text'] = detokenized_doc # 다시 text['headline_text']에 재저장
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english', 
max_features= 1000) # 상위 1,000개의 단어를 보존 
X = vectorizer.fit_transform(text['headline_text'])
```
TF-IDF Matrix 생성

```
from sklearn.decomposition import LatentDirichletAllocation
lda_model=LatentDirichletAllocation(n_components=10,learning_method='online',random_state=777,max_iter=1)
lda_top=lda_model.fit_transform(X)
terms = vectorizer.get_feature_names() # 단어 집합. 1,000개의 단어가 저장됨.

def get_topics(components, feature_names, n=5):
    for idx, topic in enumerate(components):
        print("Topic %d:" % (idx+1), [(feature_names[i], topic[i].round(2)) for i in topic.argsort()[:-n - 1:-1]])
get_topics(lda_model.components_,terms)
```
```
Topic 1: [('people', 131.94), ('think', 123.56), ('like', 111.1), ('know', 105.72), ('time', 94.95)]
Topic 2: [('space', 52.18), ('nasa', 30.72), ('satellite', 20.94), ('orbit', 20.39), ('station', 20.0)]
Topic 3: [('thanks', 171.58), ('windows', 136.93), ('know', 125.39), ('like', 110.79), ('mail', 109.0)]
Topic 4: [('bike', 68.49), ('chip', 39.47), ('like', 31.29), ('miles', 30.56), ('cars', 29.52)]
Topic 5: [('soon', 31.12), ('wanted', 13.22), ('produce', 9.45), ('engine', 8.72), ('problems', 8.08)]
Topic 6: [('game', 98.42), ('games', 81.98), ('team', 79.7), ('year', 69.51), ('season', 55.49)]
Topic 7: [('drive', 75.24), ('drives', 32.29), ('disk', 25.74), ('hard', 22.01), ('floppy', 19.64)]
Topic 8: [('armenians', 31.55), ('armenian', 30.42), ('turkish', 28.27), ('turkey', 25.54), ('condition', 25.37)]
Topic 9: [('picture', 18.53), ('xterm', 14.78), ('western', 12.42), ('tape', 10.65), ('conference', 8.27)]
Topic 10: [('people', 98.95), ('government', 78.78), ('think', 51.35), ('state', 47.48), ('like', 46.49)]
```
topic modeling
