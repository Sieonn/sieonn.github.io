---
title: "AWS Database Migration Service(AWS DMS)"
---

## AWS Database Migration Service(AWS DMS)

**AWS Database Migration Service**는 데이터베이스를 Amazon Web Services(AWS)로 빠르고 안전하게 마이그레이 션할 수 있도록 지원합니다

### AWS Database Migration Service

주요 기능 및 지원되는 데이터베이스 유형 • 

- AWS Database Migration Service의 경우, 마이그 레이션하는 동안 원본 데이터베이스가 변함없이 운 영되어 데이터베이스를 사용하는 애플리케이션의 가동 중지 시간을 최소화할 수 있습니다. • 
- AWS DMS를 사용하면 가장 널리 사용되는 상용 및 오픈 소스 데이터베이스를 소스나 대상으로 데이터 를 마이그레이션할 수 있습니다. 이 서비스를 사용 하여 데이터베이스 관리 시스템(DBMS) 서비스에서 다른 DBMS 서비스로 마이그레이션할 수 있습니다. 예를 들어 다음에서 이동할 수 있습니다. 
  - Oracle에서 Oracle로 
  - Microsoft SQL Server에서 Amazon Aurora로 • 
- 애플리케이션은 마이그레이션 중에 활성 상태를 유 지하거나 실행할 수 있습니다

### AWS DMS의 고가용성

기타 주요 기능 • 

- AWS DMS는 거의 지속적으로 데이터를 복제할 수 있 으며 고가용성을 제공합니다. 

AWS DMS가 제공하는 추가 기능 • 

- 필요한 경우 AWS DMS를 통해 페타바이트 규모의 데이 터 웨어하우스에 있는 데이터베이스를 다른 Amazon 서 비스로 통합할 수 있습니다. 이러한 서비스의 예로는 Amazon Redshift 및 Amazon S3가 있습니다.

### 구문 마이그레이션 전환

AWS DMS는 정형 쿼리 언어(SQL)와 NoSQL 데이터베이 스 간에 마이그레이션할 수 있습니다. 예를 들어 다음에 서 마이그레이션할 수 있습니다. • SQL에서 SQL로 • NoSQL에서 SQL로 • SQL에서 NoSQL로 • NoSQL에서 NoSQL로 예를 들어 NoSQL 소스인 Amazon S3에서 SQL 대상인 Amazon Relational Database Service(Amazon RDS)로 마 이그레이션할 수 있습니다

## 데이터베이스 마이그레이션 유형

### 동종 데이터베이스 마이그레이션

동종 데이터베이스 마이그레이션 이해

![image-20231027151533514](/../images/2023-10-27-AWS Datebase Migration Service(AWS)/image-20231027151533514.png)

동종 데이터베이스 마이그레이션에서는 소스 및 대상 데이터베이스 엔진이 동일하거나 호환됩니다.



### 이기종 데이터베이스 마이그레이션 

이기종 데이터베이스 마이그레이션 

![image-20231027151553553](/../images/2023-10-27-AWS Datebase Migration Service(AWS)/image-20231027151553553.png)

이기종 마이그레이션은 2단계 프로세스입니다. 

## AWS Schema Conversion Tool

대부분의 데이터베이스 마이그레이션에는 AWS SCT를 사용 하여 스키마를 변환하고 AWS DMS를 사용하여 데이터를 마 이그레이션하는 2단계가 포함됩니다.

AWS DMS를 AWS SCT와 함께 사용하면 가동 중지 시간을 줄 이면서 데이터베이스를 AWS로 마이그레이션할 수 있습니다.

### AWS SCT가 지원하는 변환

AWS SCT 변환: • 소스 데이터베이스 스키마 • 보기 • 축적 절차(stored procedure) • 함수

|      |      |
| ---- | ---- |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |

## 거의 연속적인 데이터베이스 복제

### 거의 연속적인 데이터베이스 복제

거의 연속적인 데이터베이스 복제를 사용하면 야간 작업과 같은 일정에 따라 데이터를 복제하거나 거의 실시간으로 복제할 수 있습니다. 

데이터 센터에서 AWS의 데이터베이스로 거의 연속적인 복제를 수행할 수 있습니다. 또는 AWS의 데이터베이스에서 데이터 센터의 데이터베이스로 복제하여 반대 방향으로 수행할 수 있습니다

### 거의 연속적인 데이터 복제

소스 데이터베이스의 데이터는 대상 데이 터베이스에 지속적으 로 복제됩니다. 연속적인 데이터 복 제는 재해 복구, 지리 적 데이터베이스 배 포에 유용할 수 있습 니다.

![image-20231027151749984](/../images/2023-10-27-AWS Datebase Migration Service(AWS)/image-20231027151749984.png)

## AWS DMS 통합

### 데이터베이스 통합

데이터베이스 통합 이해

데이터베이스 통합에 서 여러 소스가 하나 의 데이터베이스로 결합됩니다.

![image-20231027151831499](/../images/2023-10-27-AWS Datebase Migration Service(AWS)/image-20231027151831499.png)

## AWS DMS 프로세스 아키텍처

### AWS DMS의 4가지 구성 요소

![image-20231027151857576](/../images/2023-10-27-AWS Datebase Migration Service(AWS)/image-20231027151857576.png)

### 설명: AWS DMS 아키텍처

![image-20231027151924015](/../images/2023-10-27-AWS Datebase Migration Service(AWS)/image-20231027151924015.png)

### AWS DMS 엔드포인트

DMS 소스 및 대상 조합

| 소스 또는 대상          | 온프레미스 | Amazon RDS, Amazon Redshift, Amazon S3 및 Amazon DynamoDB | Amazon EC2 |
| ----------------------- | ---------- | --------------------------------------------------------- | ---------- |
| 온프레미스              | 미지원     | 지원                                                      | 지원       |
| Amazon RDS 및 Amazon S3 | 지원       | 지원                                                      | 지원       |
| Amazon EC2              | 지원       | 지원                                                      | 지원       |
| Azure SQL               | 미지원     | 지원                                                      | 지원       |

## AWS DMS 복제 인스턴스

AWS DMS 복제 인스턴스는 다중 AZ 배포를 사용한 고가용성 및 장애 조치 지원을 제공합니다.

### 다중

 AZ 배포 다중 AZ 배포에서 AWS DMS는 다른 가용 영역에 복제 인스턴스의 동기 대기 복제본을 자동으로 프로비저닝하고 유지 관리합니다. 

![image-20231027152132570](/../images/2023-10-27-AWS Datebase Migration Service(AWS)/image-20231027152132570.png)

프라이머리 복제 인스턴스는 가용 영역에서 대기 복제본으로 동기식으로 복제됩니다. 이 접근 방식은 데이터 중복성을 제공하고 I/O 정지를 줄이며 최고 대기 시간을 최소화합니다.

## 학습 내용 확인

1. 이기종 데이터베이스 마이그레이션 프로세스에는 몇 단계가 있으며 단계는 무엇입니까?

   2단계가 있습니다. 원본데이터베이터를 SCT로 변환하고 타겟 데이터베이스로 변환합니다.

2. 소스 데이터베이스와 대상 데이터베이스의 차이점은 무엇입니까?

   동종이 있고 이종이 있습니다.

3. AWS Schema Conversion Tool로 무엇을 할 수 있습니까?

   바로 마이그레이션이 안되기 때문에 스키마를 컨버전하는 것입니다.

## 핵심 사항

- AWS DMS 및 AWS SCT는 온프레미스 데이터 센터 및 클라우드 인스턴스에서 AWS로 동종 및 이기종 데이터베이스를 마이그레이션하는 데 도움이 됩니다. • 
- 대부분의 데이터베이스 마이그레이션에는 AWS SCT를 사용하여 스키마를 변환하고 AWS DMS를 사용하여 데이터를 마이그레이션하는 2단계가 포함됩니다.

## Knowledge Check

#### 다음 중 MySQL 및 PostgreSQL과 호환되는 완전관리형 Amazon Web Services(AWS) 관계형 데이터베이스는 무엇입니까?

- [x] Amazon Aurora
- [ ] Amazon DynamoDB
- [ ] Amazon Neptune
- [ ] Amazon Redshift

#### 고객이 데이터 센터에서 실행되는 MySQL 데이터베이스를 Amazon Aurora로 마이그레이션하기로 했습니다. 데이터베이스는 마이그레이션이 진행되는 동안에도 완벽하게 작동해야 합니다. 또한 데이터가 AWS로 마이그레이션되었을 때 자동으로 데이터를 변환하고 싶어 합니다. 다음 중 이 고객이 사용해야 할 AWS 서비스 기능은 무엇입니까?

- [ ] AWS DataSync
- [x] AWS Database Migration Service(AWS DMS)
- [ ] Amazon Aurora 스토리지 엔진
- [ ] 통합 모니터링

#### 다음 Amazon Web Services(AWS) 서비스 중 복잡한 분석 쿼리를 실행하는 데 사용할 수 있는 완전관리형 데이터 웨어하우스는 무엇입니까?

- [ ] Amazon DynamoDB
- [ ] Amazon Relational Database Service(Amazon RDS)
- [ ] Amazon Neptune
- [x] Amazon Redshift

#### 다음 중 Amazon Aurora 데이터베이스 클러스터가 가질 수 있는 읽기 전용 복제본의 최대 수는 무엇입니까?

- [ ] 5
- [ ] 10
- [x] 15
- [ ] 20

#### 다음 중 NoSQL 데이터베이스 옵션은 무엇입니까?

- [ ] Amazon Aurora
- [x] Amazon DynamoDB
- [ ] PostgreSQL
- [ ] MariaDB