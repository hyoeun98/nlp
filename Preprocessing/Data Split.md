# Data Split
- 지도 학습을 위한 데이터 분리
1. 데이터와 레이블 분리
```
import pandas as pd

values = [['당신에게 드리는 마지막 혜택!', 1],
['내일 뵐 수 있을지 확인 부탁드...', 0],
['도연씨. 잘 지내시죠? 오랜만입...', 0],
['(광고) AI로 주가를 예측할 수 있다!', 1]]
columns = ['메일 본문', '스팸 메일 유무']

df = pd.DataFrame(values, columns=columns)
df
```
![image](https://user-images.githubusercontent.com/62679143/134761895-8af9e9c4-1757-474a-8a12-0249dbde5a4b.png)

2. train data와 test data 분리
- scikit-learn
```
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=1234)
```
