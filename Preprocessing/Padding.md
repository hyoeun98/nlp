# Padding
- 여러 문장의 길이를 동일하게 통일하는 작업

### numpy padding
```
max_len = max(len(item) for item in encoded) #가장 긴 문장의 길이
for item in encoded: # 각 문장에 대해서
    while len(item) < max_len:   # max_len보다 작으면
        item.append(0)

padded_np = np.array(encoded)
padded_np
```
```
array([[ 1,  5,  0,  0,  0,  0,  0],
       [ 1,  8,  5,  0,  0,  0,  0],
       [ 1,  3,  5,  0,  0,  0,  0],
       [ 9,  2,  0,  0,  0,  0,  0],
       [ 2,  4,  3,  2,  0,  0,  0],
       [ 3,  2,  0,  0,  0,  0,  0],
       [ 1,  4,  6,  0,  0,  0,  0],
       [ 1,  4,  6,  0,  0,  0,  0],
       [ 1,  4,  2,  0,  0,  0,  0],
       [ 7,  7,  3,  2, 10,  1, 11],
       [ 1, 12,  3, 13,  0,  0,  0]])
```
- 숫자 0을 사용한 zero padding

### keras padding
```
from tensorflow.keras.preprocessing.sequence import pad_sequences
padded = pad_sequences(encoded)
padded
```
- numpy는 문서의 뒤에 0을 채우고
- keras는 문서의 앞에 0을 채움

