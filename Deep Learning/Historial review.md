# Deep learning

### Key components
- The data that the model can learn from
- The model how to transform the data
- The loss function that qeuantifies badness of the model
- The algorithm to adjust the parameters to minimize the loss

### History
- 2012 - AlexNet
  -  CNN, 224x224 image classification
  -  deep learning을 활용한 첫 imagenet 우승
- 2013 - DQN
  - Deep Q-Network
  - deepmind, alphago
  - deep learning + reinforcement learning
- 2014 - Encoder/Decoder
  - NMT(Neural Machine Translation)
  - sequence to sequence model
- 2014 - Adam Optimizer
  - Adaptive momentum optimizer
  - reasonable hyperparameter를 찾는 방법
- 2015 - GAN
  - Generative Adversarial Network
  - image,text generation를 위함
  - discriminator(경찰)이 위조지폐를 찾으면 generator(위조지폐범)이 더욱 정교한 위조지폐를 만든다
- 2015 - ResNet
  - Residual Networks
  - 기존에는 network가 너무 deep하면 성능이 안좋아짐 -> 완화
- 2017 - Transformer 
  - Attention
  - RNN을 대체 가능
- 2018 - BERT
  - Bidirectional Encoding Representation from Transformers
  - fine-tuned NLP models
- 2019 - Big Language Models(GPT-X)
  - BERT의 진화형
  - many many parameter
- 2020 - Self Supervised Learning
  - simCLR -a simple framework for Contrastive Learning of visual Representations
  - 주어진 train data외에 label이 없는 unsupervised data 활용
