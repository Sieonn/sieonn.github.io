---
title: "Amazon CloudWatch"
toc: true
toc_label: "Amazon CloudWatch"
toc_sticky: true
---

## Amazon CloudWatch

### AWS를 효율적으로 사용하고 인사이트 얻기

**AWS 사용하기** 

- AWS를 효율적으로 사용하려면 AWS 리소스에 대한 인사이트가 필요합니다. 
  - 더 많은 Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스를 언제 시작해야 하는지 어떻게 알 수 있습니까? 
  - 용량 부족으로 인해 애플리케이션의 성능이나 가용성이 영향을 받고 있습니까? 
  - 인프라에서 실제로 사용되고 있는 부분은 얼마나 됩니까?

### 리소스 성능 모니터링

Amazon CloudWatch 워크로드 성능을 모니터링할 때 두 가지 중요한 질문을 스스로에게 던져야 합니다. 

1) 변화하는 성능 요구 사항을 충족시키기 위해 내 워크로드에 충분한 리소스가 있는지 어떻게 확인할 수 있습니까? 

2) 온디맨드로 리소스 프로비저닝을 자동화하려면 어떻게 해야 합니까?

### Amazon CloudWatch란 무엇입니까?

- Amazon CloudWatch AWS에서 관리할 수 있는 대부분의 리소스 상태 및 사용률 모니터링
- 주요 개념: – 
  - 표준 지표 – 
  - 사용자 지정 지표 – 
  - 경보 – 
  - 알림 
- CloudWatch 에이전트는 다음과 같은 시스템 수준 지표를 수집합니다. – 
  - EC2 인스턴스 –
  -  온프레미스 서버

![image-20231030162851093](/../images/Untitled/image-20231030162851093.png)

### Amazon CloudWatch

![image-20231030162903007](/../images/Untitled/image-20231030162903007.png)

### Amazon CloudWatch 액션

![image-20231030162915930](/../images/Untitled/image-20231030162915930.png)

### Amazon CloudWatch 경보

- 특정 임계값에 대해 선택한 지표 테스트(크거나 같음, 작거나 같음)  
- ALARM 상태가 반드시 위급한 상태를 의미하는 것은 아닙니다.

**세 가지 가능한 경보 상태:**

**OK** - 임계값을 초과하지 않음

**ALARM** - 임계값을 초과함

**INSUFFICIENT DATA** - 경보가 방금 시작되었으며, 지표를 사용할 수 없거나 데이터가 부족함.

## Amazon CloudWatch 모니터링 예제

![image-20231030163052127](/../images/Untitled/image-20231030163052127.png)

### CloudWatch 경보 예제

![image-20231030163108670](/../images/Untitled/image-20231030163108670.png)

`1개 기간만 임계값을 초과하면 작업이 호출 안 됨`

### 지표 구성 요소

| 지표         | 이름 및 값                                                   |
| ------------ | ------------------------------------------------------------ |
| 네임스페이스 | 관련 지표를 하나로 그룹화                                    |
| 배열         | 지표를 추가로 분류하는 이름-값 페어<br />Ex) instanceld는 CPU 사용률의 배열<br />지표 이름 + 배열 = 고유한 새 지표 |
| 기간         | 지표가 수집되는 지정된 시간(초 단위)                         |

### 지표 구성 요소

![d](/../images/Untitled/d.png)

### 표준 지표 및 사용자 지정 지표

**표준 지표:**  

- 서비스 이름별로 그룹화  
- 선택한 지표를 비교할 수 있도록 그래픽 방식으로 표시  
- 직전 15개월 이내에 서비스를 사용한 경우에만 제공  
- AWS Command Line Interface(AWS CLI) 또는 애플리케이션 프로그래밍 인터페이스(API)를 통해 프로그래밍 방식으로 연결 가능

**사용자 지정 지표:**  

- 사용자 정의 네임스페이스를 기준으로 그룹화  
- AWS CLI, API 또는 CloudWatch 에이전트를 사용하여 CloudWatch에 게시

### 모니터링 및 보안

**CloudWatch**를 사용하여 다음과 같은 의심스러운 활동을 모니터링합니다

- CPU, 디스크 활동 또는 Amazon Relational Database(Amazon RDS) 사용량과 같은 서비스 사용량의 비정상적이고 장기간 급등 – 
- 과금 지표에 대해 알림 설정(계정 설정에서 활성화해야 함)

### CloudWatch Automatic Dashboards

**Amazon CloudWatch 대시보드:**  

- 실행 중인 AWS 서비스에 대한 데이터 표시  
- 기존 모니터링 도구를 통해 사용 가능

### 세부 인스턴스 모니터링 활성화

- 기본적으로 EC2 인스턴스는 5분 단위로 데이터를 보고(AWS 무료 등급) – AWS 무료 등급에 대한 자세한 내용은 AWS 무료 등급 웹 페이지를 참조하십시오.  
- 보고 빈도를 1분 단위로 늘리려면 인스턴스에 대한 세부 모니터링을 활성화합니다. – 추가 요금이 적용됩니다.

## 핵심 사항

- Amazon CloudWatch는 성능, 리소스 및 애플리케이션 상태를 모니터링합니다.  
- 다음을 수행할 수 있습니다. » 리소스 및 애플리케이션 성능 추적 » 로그 파일 수집 및 모니터링 » 경보가 울릴 때 알림 수신  
- CloudWatch는 3가지 기본 요소로 구성됩니다. 
  - 지표
  - 경보
  - 이벤트