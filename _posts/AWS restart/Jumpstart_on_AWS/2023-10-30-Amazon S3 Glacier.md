---
title: "Amazon Simple Storage Service Glacier"
toc_label: "Amazon Simple Storage Service Glacier"
toc: true
toc_sticky: true
---

## Amazon S3 Glacier

**Amazon S3 Glacier**는 데이터 아카이브 및 장기 백업을 위한, 안전하고 안정적이며 비용이 매우 저렴한 Amazon S3 스토리지 클래스입니다.

## Amazon S3 Glacier 개념

### Amazon S3 Glacier 핵심 개념: 아카이브

데이터 모델 개념 

아카이브: Amazon S3 Glacier에 저장하는 사진, 동영상, 파일 또는 문서와 같은 객체입니다. 

- 각 아카이브에는 고유한 주소가 있습니다. 아카이브 주소의 일반적인 형식은 다음과 같습니다. 

  **https://<리전에 고유한 엔드포인트>/<계정 ID>/vaults/<저장소 이름>/archives/<아카이브 ID>**

### Amazon S3 Glacier 핵심 개념: 저장소

데이터 모델 개념

**저장소** : 아카이브를 저장하기 위한 컨테이너입니다. 저장소를 생성할 때는 저장소 이름과 저장소가 위치할 리전을 지정합니다

![image-20231030123922547](/../../images/2023-10-31-Amazon S3 Glacier/image-20231030123922547.png)

### Amazon S3 Glacier 핵심 개념: 저장소 액세스 정책

- 저장소 액세스 정책: 저장소에 저장된 데이터에 액세스할 수 있는 사람과 액세스할 수 없는 사람을 결정합니다. 사용자가 수행할 수 있는 작업과 수행할 수 없는 작업 또한 결정합니다. 각 저장소에 대해 하나의 저장소 액세스 권한 정책을 생성하여 해당 저장소에 대한 액세스 권한을 관리할 수 있습니다.  
- 저장소 잠금 정책을 사용하여 저장소를 변경하지 못하도록 할 수 있습니다. 각 저장소에는 하나의 저장소 액세스 정책과 하나의 저장소 잠금 정책이 연결될 수 있습니다.

### Amazon S3 Glacier 핵심 개념: 작업

**작업**: Amazon S3 Glacier 작업은 아카이브에서 몇 가지 쿼리를 수행하거나, 아카이브를 검색하거나, 저장소의 인벤토리를 가져올 수 있습니다. 아카이브에서 쿼리를 수행할 때 정형 쿼리 언어(SQL) 쿼리와 Amazon S3 Glacier 아카이브 객체의 리스트를 제공하는 작업을 시작합니다.

### Amazon S3 Glacier

**보안, 내구성, 저렴한 비용을 위한 설계**

- 99.999999999%의 내구성을 보장하도록 설계되었습니다.  
- 보안 소켓 계층(SSL)/전송 계층 보안(TLS)의 전송 중인 데이터와 저장된 데이터의 암호화를 지원합니다.  
- 저장소 잠금 기능은 잠금 가능한 정책을 통해 규정 준수를 강화합니다.

## Amazon S3 Glacier 액세스

### Amazon S3 Glacier 액세스

- REST 웹 서비스  
- Java 또는 .NET 소프트웨어 개발 키트(SDK)  
- 수명 주기 정책을 사용하는 Amazon S3

### Amazon S3 Glacier 액세스 및 아카이브 검색

![image-20231030124039458](/../../images/2023-10-31-Amazon S3 Glacier/image-20231030124039458.png)

## Amazon S3 Glacier에서 데이터 저장 및 데이터와 상호 작용

### Amazon S3 Glacier가 데이터를 저장하는 방법

- Amazon S3 Glacier는 아카이브에 데이터를 저장합니다. – Amazon Glacier의 기본 데이터 단위(문서, 비디오, 이미지 등)  
- 저장소는 아카이브의 컬렉션입니다.

### Amazon S3 Glacier와 상호 작용하는 방법

**다음을 사용하여 Amazon S3 Glacier와 상호 작용**

Amazon S3 수명 주기 정책  

- 아카이브된 파일은 Amazon S3 또는 Amazon S3 API를 통해 액세스할 수 있습니다.

Amazon S3 Glacier API  

- 직접 파일 추가  
- 파일 검색 방법: 
  - job 요청을 시작합니다.  
  - 아카이브 검색 작업을 선택합니다.  
  - 원하는 경우 날짜 범위 또는 바이트 범위 필터를 지정합니다.  
  - 작업 완료에 대해 폴링하거나 Amazon Simple Notification(Amazon SNS) 알림을 수신합니다.

## 정책, 암호화, Amazon S3 Glacier를 사용한 보안

### Amazon S3 수명 주기 정책

정책을 사용하면 생성 후 기간을 기준으로 객체를 삭제 또는 이동할 수 있습니다.

![image-20231030124219964](/../../images/2023-10-31-Amazon S3 Glacier/image-20231030124219964.png)

### 서버 측 암호화

![image-20231030124238420](/../../images/2023-10-31-Amazon S3 Glacier/image-20231030124238420.png)

### Amazon S3 Glacier를 사용한 보안

- AWS Identity 및 Access Management(IAM)를 사용하여 액세스 제어
- Amazon S3 Glacier는 AES-256을 사용하여 데이터 암호화
- Amazon S3 Glacier가 자동으로 키 관리

## Amazon S3와 Amazon S3 Glacier 비교

### 스토리지 비교

|                | Amazon S3                  | Amazon S3 Glacier  |
| -------------- | -------------------------- | ------------------ |
| 데이터 볼륨    | 무제한                     | 무제한             |
| 평균 대기 시간 | 밀리초                     | 몇 분 또는 몇 시간 |
| 항목 크기      | 최대 5TB                   | 최대 40TB          |
| 월 GB당 요금   | ¢¢                         | ¢                  |
| 청구되는 요청  | PUT, COPY, POST, LIST, GET | UPLOAD, 검색       |
| 검색 요금      | ¢ 요청당                   | ¢¢ 요청당 및 GB당  |

## 핵심 사항

- Amazon S3 Glacier는 보안, 내구성 및 매우 저렴한 비용을 제공하도록 설계된 데이터 아카이브 서비스입니다.  
- Amazon S3 Glacier 요금은 리전 기반입니다.  
- 매우 저렴한 비용의 설계로 장기 아카이브에 적합합니다.  
- 이 서비스는 객체에 대해 11 9s 의 내구성을 보장하도록 설계되었습니다.