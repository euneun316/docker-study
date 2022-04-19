# Docker 환경 구성

AI model 학습 및 배포를 위한 docker 환경 구성

## 구조

```
─── pytorch1.7.1-cuda11
    ├── jupyter_notebook_config.py
    ├── notebooks/
    ├── pytorch.DockerFile
    ├── requirements.txt
    └── run_jupyter.sh
```
## Version

```
ubuntu: 18.04
cuda: 11.3.1
torch: 1.7.1
```

## 실행
- image build
```
docker build -t cuda11.3:pytorch1.7.1 -f pytorch.DockerFile .
```
- docker run : gpu 사용
```
docker run -it --name pytorch --gpus '"device=0"' -v $PWD/notebooks:/notebooks -p 8888:8888 -p 6006:6006 cuda11.3:pytorch1.7.1
```
- docker start
```
docker start pytorch -i
```
