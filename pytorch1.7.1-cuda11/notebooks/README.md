
# kid news Summarization


## KorBertSum 문서 추출요약 

### 1. Preparing Datasets

#### (1) Pre-trained BERT 
- ModelBERT fine-tuning을 위해서는 먼저 사전학습된 BERT 모델이 필요
- [ETRI 홈페이지](https://aiopen.etri.re.kr/service_dataset.php)에서 모델 사용신청을 하여 BERT Model을 다운로드

```
├─ 001_bert_morp_pytorch
│   ├── KorBERT_FAQ_20190619.pdf
│   ├── bert_config.json
│   ├── pytorch_model.bin
│   ├── readme.txt
│   ├── src_examples
│   ├── src_tokenizer
│   └── vocab.korean_morp.list
```

#### (2) Train Dataset
- [Dacon 문서 추출요약 AI 경진대회](https://dacon.io/competitions/official/235671/data) 의 데이터 셋 활용
- [AI Hub](https://aihub.or.kr/aidata/8054)의 데이터 셋 활용

#### (3) Test Dataset
- [어린이 조선일보](http://kid.chosun.com) 

---

### 2. Preprocess

- newsdata to json use [Mecab](https://konlpy.org/ko/latest/api/konlpy.tag/#mecab-class)
- json to Bert pytorch file

#### (1) project 구조

```
├── KorBertSum
│   ├── bert_config_uncased_base.json
│   ├── bert_data
│   │   ├── korean.test.0.bert.pt
│   │   ├── korean.train.0.bert.pt
│   │   └── korean.valid.0.bert.pt
│   ├── json_data
│   │   ├── korean.test.0.json
│   │   ├── korean.train.0.json
│   │   └── korean.valid.0.json
│   ├── logs
│   ├── models
│   │   └── bert_classifier
│   ├── results
│   │   ├── korean_step10000.candidate
│   │   └── korean_step10000.gold
│   └── src
│       ├── distributed.py
│       ├── models
│       ├── others
│       ├── prepro
│       ├── preprocess.py
│       └── train.py
├── korBertTest.ipynb
├── model
└── test_result.csv
```
#### (2) 세부 파일 설명

1. test_result.csv :

| media  |    id    | article_original |   article_morp    | abstractive | extractive |
|:----:|:------:|:--------------:|:---------------:|:---------:|:--------:|
| 신문사 | 기사번호 |     기사원문     | 형태소분석된 기사 |  생성요약   |  추출요약  |

2. bert_data : json_data to pt
   - `korean.test.0.bert.pt`, `korean.train.0.bert.pt`, `korean.valid.0.bert.pt`
3. json_data :  `test_result.csv` file to json
   - `korean.test.0.json`, `korean.train.0.json`, `korean.valid.0.json`
4. models : train result
   - `model_step_10000.pt` 
5. results : test result
   - `korean_step10000.candidate` : label data
   - `korean_step10000.gold` : test data
6. model : Pre-trained BERT model

---

### 3. Train
- train with encoder-classifier

<img width="888" alt="image" src="https://user-images.githubusercontent.com/44595181/163676742-e8f58c31-5b43-42ae-9162-70e4006e5608.png">


### 4. Test

- kid news article
```
전 세계가 우크라이나를 침공한 러시아에 각종 제재를 가하고 있다.
이에 러시아 고양이도 국제 대회에 출전하지 못한다는 소식이 전해졌다.
지난 3일 영국 일간 데일리메일에 따르면 70여 년 역를 가 국제고양이연맹이 최근 성명을 통해 월드 캣 쇼에 러시아 소속 고양이 참가를 금지하겠다고 밝혔다.
고양이연맹은 예쁜 고양이 대회를 비롯해 매년 700여 개의 고양이 관련 대회를 주최해왔다.
연맹 측은 오는 5월 말까지 러시아산 고양이의 수입을 금지하고 러시아에서 태어난 고양이의 혈통서 등록도 허용하지 않겠다며 우크라이나를 향한 러시아의 잔혹한 행위에 대해 더 이상 침묵할 수 없었다고 밝혔다.
이어 우크라이나 난민과 피란 중인 반려동물을 위한 기금도 마련할 것이라고 덧붙였다.
러시아 고양이의 국제 대회 출전 금지령에 대해 어떻게 생각하나요.
```

- summarization result
```
['전 세계가 우크라이나를 침공한 러시아에 각종 제재를 가하고 있다.',
 '연맹 측은 오는 5월 말까지 러시아산 고양이의 수입을 금지하고 러시아에서 태어난 고양이의 혈통서 등록도 허용하지 않겠다며 우크라이나를 향한 러시아의 잔혹한 행위에 대해 더 이상 침묵할 수 없었다고 밝혔다.',
 '고양이연맹은 예쁜 고양이 대회를 비롯해 매년 700여 개의 고양이 관련 대회를 주최해왔다.']
```

---

## Reference
1. Fine-tune BERT for Extractive Summarization [BertSum](https://github.com/nlpyang/BertSum)
2. 추출 요약 관련 아래 깃허브 소스를 참고했습니다.
	- https://github.com/HaloKim/KorBertSum
	- https://github.com/raqoon886/KorBertSum