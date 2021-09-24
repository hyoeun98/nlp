# Cleaning and Normalization
- Cleaning : corpus의 noise data 제거
  - 불용어 제거
  - 빈도가 적은 단어 제거
  - 길이가 짧은 단어 제거
```
import re
text = "I was wondering if anyone out there could enlighten me on this car."
shortword = re.compile(r'\W*\b\w{1,2}\b')
print(shortword.sub('', text))
```
```
was wondering anyone out there could enlighten this car.
```
길이가 2이하인 단어를 정규 표현식을 이용하여 삭제

- Normalization : 표현 방법이 다른 단어를 하나의 단어로 정규화
  - 이음동의어를 하나의 단어로 (ex. USA = US)
  - stemming, lemmatization 사용
  - 대, 소문자 통합

## Lemmatization(표제어 추출)
- 표제어 : 기본 사전형 단어
- 문맥을 고려하며, 해당 단어의 품사 정보(POS tag)를 보존

```
from nltk.stem import WordNetLemmatizer
n=WordNetLemmatizer()
words=['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
print([n.lemmatize(w) for w in words])
```

## Stemming(어간 추출)
- 표제어 추출에 비해 섬세하지 않음
- 단순한 규칙에 의하여 이루어짐

```
from nltk.stem import PorterStemmer 
s=PorterStemmer()
words=['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
print([s.stem(w) for w in words])
```

```
from nltk.stem import LancasterStemmer
l=LancasterStemmer()
words=['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
print([l.stem(w) for w in words])
```
### Korean stemming
- Conjugation(활용) : 용언의 어간이 어미를 가지는 일
- 규칙 활용 / 불규칙 활용

## Stopword
- 자주 등장하지만 분석을 함에 있어서 큰 도움이 되지 않는 단어

```
from nltk.corpus import stopwords  
stopwords.words('english')
```
179개의 stopword가 등록

```
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

example = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words('english')) 

word_tokens = word_tokenize(example)

result = []
for w in word_tokens: 
    if w not in stop_words: 
        result.append(w) 

print(word_tokens) 
print(result) 
```
- 참고할 만한 한국어 불용어
  - https://www.ranks.nl/stopwords/korean
  - https://bab2min.tistory.com/544

