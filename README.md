# 데이터 사이언스개론 텀프로젝트

### [nbviewer에서 코드 보기](https://nbviewer.jupyter.org/github/pgy11/HUFS-AI-Internship/tree/main/)

## 0. 주제

- 데이터 전처리를 다르게하여 3개의 데이터셋을 만들고, 결정트리를 이용하여 각 성능을 측정
  - 전처리된 데이터를 토대로 사람의 자세를 예측 할 때, 어떤 데이터 셋에서 예측이 잘 됐는지 확인하는 프로젝트 

<br/>

## 1. 데이터 셋

- MHEALTH 데이터 셋 사용(참고: https://archive.ics.uci.edu/ml/datasets/MHEALTH+Dataset)

- 3축 가속도 센서, 3축 자이로 센서, 3축 지자기 센서를 사람의 신체에 착용하고, 사람의 자세에 따른 각각의 값을 1분간 기록(점프, 무릎 굽히기, 손목 앞으로 구부리기, 팔 앞으로 올리기는 횟수로 진행)

- 데이터는 50HZ 샘플링 거쳐서 저장된다.

<details>
    <summary>Label 종류</summary>
    L1: Standing still (1 min)
    <br/>
	L2: Sitting and relaxing (1 min)
	<br/>
    L3: Lying down (1 min)
	<br/>
    L4: Walking (1 min)
	<br/>
    L5: Climbing stairs (1 min)<br/>
	L6: Waist bends forward (20x)<br/>
	L7: Frontal elevation of arms (20x)<br/>
	L8: Knees bending (crouching) (20x)<br/>
	L9: Cycling (1 min)<br/>
	L10: Jogging (1 min)<br/>
	L11: Running (1 min)<br/>
	L12: Jump front & back (20x)<br/>
</details>

<details>
    <summary>데이터 속성</summary>
    Column 1: acceleration from the chest sensor (X axis)<br/>
Column 2: acceleration from the chest sensor (Y axis)<br/>
Column 3: acceleration from the chest sensor (Z axis)<br/>
Column 4: electrocardiogram signal (lead 1)<br/>
Column 5: electrocardiogram signal (lead 2)<br/>
Column 6: acceleration from the left-ankle sensor (X axis)<br/>
Column 7: acceleration from the left-ankle sensor (Y axis)<br/>
Column 8: acceleration from the left-ankle sensor (Z axis)<br/>
Column 9: gyro from the left-ankle sensor (X axis)<br/>
Column 10: gyro from the left-ankle sensor (Y axis)<br/>
Column 11: gyro from the left-ankle sensor (Z axis)<br/>
Column 13: magnetometer from the left-ankle sensor (X axis)<br/>
Column 13: magnetometer from the left-ankle sensor (Y axis)<br/>
Column 14: magnetometer from the left-ankle sensor (Z axis)<br/>
Column 15: acceleration from the right-lower-arm sensor (X axis)<br/>
Column 16: acceleration from the right-lower-arm sensor (Y axis)<br/>
Column 17: acceleration from the right-lower-arm sensor (Z axis)<br/>
Column 18: gyro from the right-lower-arm sensor (X axis)<br/>
Column 19: gyro from the right-lower-arm sensor (Y axis)<br/>
Column 20: gyro from the right-lower-arm sensor (Z axis)<br/>
Column 21: magnetometer from the right-lower-arm sensor (X axis)<br/>
Column 22: magnetometer from the right-lower-arm sensor (Y axis)<br/>
Column 23: magnetometer from the right-lower-arm sensor (Z axis)<br/>
Column 24: Label (0 for the null class)<br/>
<br/>
*Units: Acceleration (m/s^2), gyroscope (deg/s), magnetic field (local), ecg (mV)
</details>

- 10명의 실험자가 참여해서 10개의 로그파일이 존재한다.(i.e 10개의 로그파일이 데이터 셋)

<br/>

## 2. 데이터 전처리

- 10개의 로그파일에 기록된 값을 모두 가져오고 지원자를 구분하기 위한 속성을 새로 추가한다.

- 1번째 전처리된 데이터 셋: sliding window at 10hz and stride=1
- 2번째 전처리된 데이터 셋: sliding window at 10hz and stride=5
- 3번째 전처리된 데이터 셋: sliding window at 10hz and stride=10

<br/>

## 3. EDA

- 3개의 전처리된 데이터 셋은 간단하게 EDA

<details>
    <summary>내용</summary>
1. Size of dataset, Number of label, t-test<br/>
2. Distribution of data where x axis = Mean of acceleration measured by a sensor in chest.<br/>
3. Boxplot where x axis is same with above.<br/>
4. Distribution of data using 2 features, Mean and std of acceleration measured by a sensor in chest.<br/>
5. Distribution of data where x axis = Mean of magnetometer measured by a sensor in left ankle.<br/>
6. Boxplot where x axis is same with above.<br/>
7. Distribution of data using 2 features, Mean of acceleration measured by a sensor in chest and of magnetometer measured by a sensor in left ankle.<br/>
</details>

- 결론
  - If an activity is moving and requires related muscle which has a sensor, range of value by the sensor is wide.
  - Range of value for unrelated muscle is high, if the unrelated muscle is affected by external forces 

<br/>

## 4. 분류

- 3개의 데이터 셋을 이용하여 실험을 진행(노트북 성능 문제로 다양한 ML 모델을 활용하지 못했음)
- 결정 트리 사용
  - 1번째 데이터셋의 경우, 트리의 깊이가 15일 때 정확도가 약 0.67로 가장 좋았다.
  - 2번째 데이터셋의 경우, 트리의 깊이가 12일 때 정확도가 약 0.66으로 가장 좋았다.
  - 3번째 데이터셋의 경우, 트리의 깊이가 12일 때 정확도가 약 0.66으로 가장 좋았다.

