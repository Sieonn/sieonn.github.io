---
title: "AWS Step Functions"
toc: true
toc_sticky: true
toc: "AWS Step Functions"
---

## AWS Step Funtions

### AWS Step Functions

AWS Lambda 기능 및 AWS 서비스 기타와 통합하여 비즈니스에 중요한 애플리케이션을 구축할 수 있는 서버리스 오케스트레이션 서비스입니다.

한 스테이크의 작업을 태스크라고 합니다.

step funcions: 워크플로우를 하기 위한 툴을 말합니다.

AWS Step Functions를 사용하면 AWS 서비스를 서버리스 워크플로로 조정할 수 있습니다. 

- • 워크플로는 일련의 단계로 구성됩니다. • 
- 한 단계의 출력은 다음 단계에 대한 입력으로 작용합니다. 

주요 이점: 

- 분산 애플리케이션을 빌드하고 업데이트합니다.
- 코드 작성을 최소화합니다.

{: .notice}

Ex) AWS Step Functions를 사용하면 AWS Lambda와 Amazon Elastic Container Service(Amazon ECS)를 연동할 수 있습니다.

### AWS Step Functions 이점

- 생산성

  분산 구성 요소와 마이크로서비스를 쉽게 연결하고 조정하여 애플리케이션을 빠르게 생성

- 민첩성

  문제 진단 및 디버그 시간 단축

- 복원력

  서비스 조정의 운영 및 인프라를 관리하여 규모에 상관없이 장애 발생 시 가용성 보장

### AWS Step Functions 작동 방식

### Step Functions 애플리케이션 수명 주기

ARN: AWS resource name

### 콘솔의 JSON 예제 및 시각화



### 콘솔에서 런타임 모니터링

## 용례

### 일부 AWS Step Functions 용례 예제

고인들에게 많이 사용합니다.

- <span class="hlm">**데이터 처리**</span>: 여러 데이터베이스의 데이터를 통일된 보고서로 통합합니다.  `제일 많이 사용합니다.> 수집 전처리 시각화 에널리틱 `
- DevOps 및 IT 자동화: 지속적 통합 및 지속적 배포를 위한 도구를 구축합니다. 
- 전자 상거래: 주문 이행 및 재고 추적 자동화 
- 웹 애플리케이션: 강력한 사용자 등록 프로세스와 로그인 인증 구현



1. True 또는 False: 고객은 워크플로를 일련의 단계로 정의하고 각 단계 간의 전환을 상태 시스템이라고도 합니다. 

   False 상태 머신이라고 합니다.

2. True 또는 False: AWS Step Functions는 많은 비즈니스 프로세스에 사용할 수 있습니다. 비즈니스 프로세스를 일련의 단계로 세분할 수 있는 경우 유용합니다. 

   True: 단계별로 분할 할 수 있습니다.

   좋은점은 레고처럼 끼우고 뺄 수 있습니다. = 수정에 용이합니다.  