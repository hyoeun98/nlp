# Word Representation
- Local Representation
  - 해당 단어만 보고 특정값 맵핑
  - One-hot vector, N-gram, Bag of Words 등
- Distributed Representation
  - 해당 단어의 주변을 참고
  - 단어의 뉘앙스 표현 가능
  - Word2Vec, LSA, Glove 등

### Bag of Words(BoW)
- 단어의 순서가 아닌 빈도만 고려
1. 각 단어에 고유한 정수 인덱스 부여
2. 각 인덱스에 단어의 등장 횟수를 기록한 벡터 생성

```
from sklearn.feature_extraction.text import CountVectorizer
corpus = ['you know I want your love. because I love you.']
vector = CountVectorizer()
print(vector.fit_transform(corpus).toarray()) # 코퍼스로부터 각 단어의 빈도 수를 기록한다.
print(vector.vocabulary_) # 각 단어의 인덱스가 어떻게 부여되었는지를 보여준다.
```
```
[[1 1 2 1 2 1]]
{'you': 4, 'know': 1, 'want': 3, 'your': 5, 'love': 2, 'because': 0}
```
띄어쓰기를 기준으로 토큰화를 진행하고 BoW 생성

```
from sklearn.feature_extraction.text import CountVectorizer

text=["Family is not an important thing. It's everything."]
vect = CountVectorizer(stop_words="english")
print(vect.fit_transform(text).toarray())
print(vect.vocabulary_)
```
```
[[1 1 1]]
{'family': 0, 'important': 1, 'thing': 2}
```
CountVectorizer에서 제공하는 불용어 사용

### 문서 단어 행렬(Document-Term Matrix)
- 다수의 문서에 등장하는 단어의 빈도를 행렬로 표현
- 여러 개의 BoW를 하나의 행렬로 표현
- Cons
  - 원-핫 벡터와 마찬가지로 희소 문제(sparse) 발생
  - 단순 빈도 수 접근 방식의 한계

### TF-IDF(Term Frequency-Inverse Document Frequency)
- 문서의 유사도, 단어의 중요도를 측정
- TF(d, t) : 문서 d에서 단어 t가 등장한 횟수
- DF(t) : 단어 t가 등장한 문서의 개수
- IDF(d, t) :  log(n/1+DF(t)) 
  - IDF값이 기하급수적으로 커지는 것&분모가 0이 되는 것을 방지   

- scikit-learn으로 DTM 생성
```
from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    'you know I want your love',
    'I like you',
    'what should I do ',    
]
vector = CountVectorizer()
print(vector.fit_transform(corpus).toarray()) # 코퍼스로부터 각 단어의 빈도 수를 기록한다.
print(vector.vocabulary_) # 각 단어의 인덱스가 어떻게 부여되었는지를 보여준다.
```
```
[[0 1 0 1 0 1 0 1 1]
 [0 0 1 0 0 0 0 1 0]
 [1 0 0 0 1 0 1 0 0]]
{'you': 7, 'know': 1, 'want': 5, 'your': 8, 'love': 3, 'like': 2, 'what': 6, 'should': 4, 'do': 0}
```

- scikit-learn으로 tf-idf 계산
```
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
    'you know I want your love',
    'I like you',
    'what should I do ',    
]
tfidfv = TfidfVectorizer().fit(corpus)
print(tfidfv.transform(corpus).toarray())
print(tfidfv.vocabulary_)
```
```
[[0.         0.46735098 0.         0.46735098 0.         0.46735098
  0.         0.35543247 0.46735098]
 [0.         0.         0.79596054 0.         0.         0.
  0.         0.60534851 0.        ]
 [0.57735027 0.         0.         0.         0.57735027 0.
  0.57735027 0.         0.        ]]
{'you': 7, 'know': 1, 'want': 5, 'your': 8, 'love': 3, 'like': 2, 'what': 6, 'should': 4, 'do': 0}
```
