# Machine Learning

- Training data, Validation data, Testing data
- Hyperparameter, parameter(가중치, 편향)

### Classification
- Binary Classification : 주어진 Input에 따라 둘 중 하나의 Output을 도출
- Multi-class Classification : 주어진 Input에 따라 둘 이상의 선택지 중 Output을 도출

### Regression
- 분류처럼 Output이 이산적이 아닌 연속된 값

### Supervised Learning
- 학습의 정답(label)이 존재

### Unsupervised Learning
- Label이 존재하지 않음
- LDA, Word2Vec 등

- Classification & Regression : Output의 이산적, 연속적 여부
- Supervised & Unsupervised : Label의 존재 여부

![image](https://user-images.githubusercontent.com/62679143/135707265-ca835bee-9730-4054-9ace-ec0510d1986d.png)

- Sample : data
- Feature : 학습의 기준

### Confusion Matrix
- Accuracy : 맞힌 문제 / 전체 문제

![image](https://user-images.githubusercontent.com/62679143/135707423-18a717c9-20d7-4f51-856c-9170fd37f034.png)
- row : 실제 값
- col : 예측 값

- Precision : TP / (TP + FP)
- Recall : TP / (TP + FN) 
- Overfitting : 과하게 학습하여 training data에 대한 정확도는 높으나, 실제 data에 대해 정확도가 떨어지는 현상
  - Drop out, Early Stopping 등을 이용하여 Overfitting 방지
- Underfitting : 학습이 부족하여 training data에 대한 정확도가 떨어짐
