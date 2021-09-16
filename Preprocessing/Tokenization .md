# Tokenization
- corpus를 token으로 분리하는 작업
## Word Tokenization
- 토큰의 기준을 word로 설정 (단어, 구, 문자열 등)
- NLTK의 word_tokenize(보편적), WordPunctTokenizer(구두점을 별도로 분류)
- Keras의 text_to_word_sequence(모든 알파벳을 소문자로, 구두점 제거, '는 보존)
- Tokenization 시 고려사항
    - 구두점, 특수문자를 고려할 것
    - 줄임말, 단어 내의 띄어쓰기를 고려할 것
- Penn Treebank Tokenization (업계 표준)
    - 하이푼으로 구성된 단어는 하나로 유지한다
    - don't와 같이 '로 접어가 함께하는 단어는 분리한다. 
## Sentence Tokenization
- 토큰의 기준을 sentence로 설정
- NLTK의 sent_tokenize
- KSS(한국어 문장 토큰화)
### Binary Classfier
- 두 클래스로 구분
1. 마침표(.)가 약어로 쓰일 경우
2. 마침표(.)가 문장의 구분자(boundary)일 경우
- 임의로 정한 규칙, 머신러닝을 통한 학습 사용
- NLTK, OpenNLP, CoreNLP, LingPipe 등
## Korean Tokenization
- 한국어는 교착어이다
- 띄어쓰기가 잘 지켜지지 않는다
- 토큰화 어려움
## Part Of Speech tagging
- 품사에 따라 단어의 뜻이 바뀌는 경우
- 각 단어가 어떤 품사로 쓰이는지 구분
- NLTK의 Penn Treebank POS Tags
```
from nltk.tokenize import word_tokenize
text="I am actively looking for Ph.D. students. and you are a Ph.D. student."
from nltk.tag import pos_tag
x=word_tokenize(text)
pos_tag(x)
```
```
[('I', 'PRP'), ('am', 'VBP'), ('actively', 'RB'), ('looking', 'VBG'), ('for', 'IN'), ('Ph.D.', 'NNP'), ('students', 'NNS'), ('.', '.'), ('and', 'CC'), ('you', 'PRP'), ('are', 'VBP'), ('a', 'DT'), ('Ph.D.', 'NNP'), ('student', 'NN'), ('.', '.')]
```
word tokenization 후 pos tagging

- KoNLPy의 Okt
```
from konlpy.tag import Okt  
okt=Okt()  
print(okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
print(okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
print(okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
```
```
['열심히', '코딩', '한', '당신', ',', '연휴', '에는', '여행', '을', '가봐요']  
[('열심히','Adverb'), ('코딩', 'Noun'), ('한', 'Josa'), ('당신', 'Noun'), (',', 'Punctuation'), ('연휴', 'Noun'), ('에는', 'Josa'), ('여행', 'Noun'), ('을', 'Josa'), ('가봐요', 'Verb')]  
['코딩', '당신', '연휴', '여행']  
```
morphs 형태소 추출, pos 품사 태깅, nouns 명사 추출

- 한국어 형태소 분석기 비교 https://velog.io/@metterian/%ED%95%9C%EA%B5%AD%EC%96%B4-%ED%98%95%ED%83%9C%EC%86%8C-%EB%B6%84%EC%84%9D%EA%B8%B0POS-%EB%B6%84%EC%84%9D-3%ED%8E%B8.-%ED%98%95%ED%83%9C%EC%86%8C-%EB%B6%84%EC%84%9D%EA%B8%B0-%EB%B9%84%EA%B5%90
## SubwordTokenization
### BPE(Byte Pair Encoding)
- 기계가 모르는 단어 Out-Of-Vocabulary or Unknown Token -> OOV 문제
- Subword segmentation
- 희귀 단어, 신조어 파악 가능
- 연속적으로 가장 많이 등장한 글자의 쌍을 찾아서 하나의 글자로 병합
- 
```
aaabdaaabac

Z=aa
ZabdZabac

Y=ab
Z=aa
ZYdZYac

X=ZY
Y=ab
Z=aa
XdXac
```

1. 단어를 글자 단위로 분리하여 vocabulary 생성
2. 가장 많이 등장하는 unigram pair를 병합하여 vocabulary에 추가 (n번 반복)
3. 새로운 단어 등장 시 글자 단위로 분리하여 vocabulary에서 탐색

- WPM (WordPiece Model)
    - BPE는 빈도 수에 기반하여 병합하지만, WPM는 병합되었을 때 corpus의 likelihood가 가장 높은 pair 병합
    - 모든 단어의 앞에 _를 붙이고, 통계에 기반하여 subword 분리 
    - underscore _는 subword의 분리와 기존의 띄어쓰기를 구분하기 위함

```
WPM을 수행하기 이전의 문장: Jet makers feud over seat width with big orders at stake
WPM을 수행한 결과(wordpieces): _J et _makers _fe ud _over _seat _width _with _big _orders _at _stake
```

- Unigram Language Model Tokenizer
    - 각각의 subword들에 대한 loss 계산 (subword가 vocabulary에서 제거되었을 때 감소하는 likelihood)
    - 손실이 가장 큰 토큰부터 제거
    
### Sentencepiece
    - pretokenization 없이 토큰화 가능 -> 어떤 언어에도 적용 가능

```
import sentencepiece as spm
import pandas as pd
import urllib.request
import csv
```
importing
```
urllib.request.urlretrieve("https://raw.githubusercontent.com/LawrenceDuan/IMDb-Review-Analysis/master/IMDb_Reviews.csv", filename="IMDb_Reviews.csv")
train_df = pd.read_csv('IMDb_Reviews.csv')
```
train data
```
with open('imdb_review.txt', 'w', encoding = 'utf-8') as f:
    f.write('\n'.join(train_df['review']))
```
txt 파일로 저장    
```
spm.SentencePieceTrainer.Train('--input=imdb_review.txt --model_prefix=imdb --vocab_size=5000 --model_type=bpe --max_sentence_length=9999')
```
학습, model 파일 & vocab 파일 생성
```
sp = spm.SentencePieceProcessor()
vocab_file = "imdb.model"
sp.load(vocab_file)
```

Encoding = 문장을 subword, subword index로 변환 (encode_as_pieces(), encode_as_ids())\
Decoding = subword, subword index를 문장으로 변환 (DecodeIds(), DecodePieces())

### SubwordTextEncoder
    - tensorflow를 통해 사용가능
    - bpe와 유사한 Wordpiece Model
    - tf2.3- -> tfds.features.text
    - tf2.3+ -> tfds.deprecated.text
```
import tensorflow_datasets as tfds
import urllib.request
import pandas as pd
```
importing
```
urllib.request.urlretrieve("https://raw.githubusercontent.com/LawrenceDuan/IMDb-Review-Analysis/master/IMDb_Reviews.csv", filename="IMDb_Reviews.csv")
train_df = pd.read_csv('IMDb_Reviews.csv')
```
train data
```
tokenizer = tfds.features.text.SubwordTextEncoder.build_from_corpus(train_df['review'], target_vocab_size=2**13)
```
tokenization
```
encoded = tokenizer.encode(train_df['review'][20])
decoded = tokenizer.decode(encoded)
print(decoded)
```
21번째 문장을 정수 encoding 후 다시 decoding
```
for ts in encoded:
    print('{} ----> {}'.format(ts,tokenizer.decode([ts])))
```
subword index - subword 간 맵핑 확인
