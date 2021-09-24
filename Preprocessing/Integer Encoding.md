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
[[1, 5], [1, 5], [1, 3, 5], [2], [2, 4, 3, 2], [3, 2], [1, 4], [1, 4], [1, 4, 2], [3, 2, 1], [1, 3]]```
padding을 위해 단어 집합의 크기를 +1

- 단어 집합에 없는 단어(OOV)는 인코딩 과정에서 제거
- oov_token의 OOV 인덱스 : 1 
