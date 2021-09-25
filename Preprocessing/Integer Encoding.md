# Integer Encoding(정수 인코딩)
- 단어에 고유한 정수를 mapping
- Encoding 전에 최대한 전처리를 끝내 놓아야 함

### Counter
- 단어들을 하나의 list에 저장 후
```from collection import Counter
vocab = Counter(words)
print(vocab)
```
```
Counter({'barber': 8, 'secret': 6, 'huge': 5, 'kept': 4, 'person': 3, 'word': 2, 'keeping': 2, 'good': 1, 'knew': 1, 'driving': 1, 'crazy': 1, 'went': 1, 'mountain': 1})
```

### NLTK의 FreqDist
```
from nltk import FreqDist
import numpy as np
vocab = FreqDist(np.hstack(sentences)) #np.hstack() -> list를 이어 붙이는 함수
vocab
```
```
Counter({'barber': 8, 'secret': 6, 'huge': 5, 'kept': 4, 'person': 3, 'word': 2, 'keeping': 2, 'good': 1, 'knew': 1, 'driving': 1, 'crazy': 1, 'went': 1, 'mountain': 1})
```

### enumerate
```
test=['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(test): # 입력의 순서대로 0부터 인덱스를 부여함.
  print("value : {}, index: {}".format(value, index))
```
```
value : a, index: 0
value : b, index: 1
value : c, index: 2
value : d, index: 3
value : e, index: 4
```

### keras Tokenizer
```
from tensorflow.keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
print(tokenizer.word_index)
```
```
{'barber': 1, 'secret': 2, 'huge': 3, 'kept': 4, 'person': 5, 'word': 6, 'keeping': 7, 'good': 8, 'knew': 9, 'driving': 10, 'crazy': 11, 'went': 12, 'mountain': 13}
```
- 빈도수가 높은 순으로 정수 인코딩
```
vocab_size = 5
tokenizer = Tokenizer(num_words = vocab_size + 1) # 상위 5개 단어만 사용
tokenizer.fit_on_texts(sentences)
print(tokenizer.texts_to_sequences(sentences))
```
```
[[1, 5], [1, 5], [1, 3, 5], [2], [2, 4, 3, 2], [3, 2], [1, 4], [1, 4], [1, 4, 2], [3, 2, 1], [1, 3]]
```
padding을 위해 단어 집합의 크기를 +1

- 단어 집합에 없는 단어(OOV)는 인코딩 과정에서 제거
- oov_token의 OOV 인덱스 : 1 

### One-Hot Encoding
- vocabulary : 서로 다른 단어들의 집합
- book, books도 다른 단어로 간주
- 단어 집합의 크기 = 벡터의 차원
1. 각 단어에 고유한 인덱스 부여
2. 표현하고 싶은 단어의 인덱스에 1, 나머지에 0

- Keras의 One-Hot Encoding
```
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

text="나랑 점심 먹으러 갈래 점심 메뉴는 햄버거 갈래 갈래 햄버거 최고야"

t = Tokenizer()
t.fit_on_texts([text])
print(t.word_index) # 각 단어에 대한 인코딩 결과 출력.
```
```
{'갈래': 1, '점심': 2, '햄버거': 3, '나랑': 4, '먹으러': 5, '메뉴는': 6, '최고야': 7}
```
```
encoded=t.texts_to_sequences([text])[0]
print(encoded) # text를 인코딩된 정수 시퀀스로 변환
```
```
[4, 2, 5, 1, 2, 6, 3, 1, 1, 3, 7]
```
```
one_hot = to_categorical(encoded)
print(one_hot) # 원-핫 인코딩 
```
```
[[0. 0. 0. 0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 1. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1.]]
```

- Cons 
  - 비효율적인 저장 공간
  - 단어의 유사도 표현 불가
- 대안
  - 카운트 기반 LSA, HAL
  - 예측 기반 NNLM, RNNLM, Word2Vec, FastText
  - 모두 사용하는 GloVe
