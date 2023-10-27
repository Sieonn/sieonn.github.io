---
title: "Amazon Aurora"
toc: true
toc_sticky: true
toc_label: "Amazon Aurora"
---

Amazon Aurora는 MySQL 및 PostgreSQL과 호환되는 완전관리형 관계형 데이터베이스 엔진입니다.

## Amazon Aurora

### Amazon Aurora 란 무엇입니까?

Amazon Aurora

- • Aurora는 Amazon Relational Database Service(Amazon RDS) 관리형 데이터베이스 서비스에 속합니다. • Aurora는 속도가 표준 MySQL 데이터베이스보다 최대 5배 빠릅니다. • Aurora는 클러스터로 구성됩니다. • 또한 Aurora는 일반적으로 데이터베이스 구성 및 관리의 가장 어려운 측면 중 하나인 데이터베이스 클러스터링 및 복제를 자동화하고 표준화합니다.

### Amazon Aurora 주요 기능

![image-20231027144618597](/../images/2023-10-27-Amazon Aurora/image-20231027144618597.png)

### Aurora를 통한 고가용성의 예

![image-20231027144638860](/../images/2023-10-27-Amazon Aurora/image-20231027144638860.png)

## Amazon Aurora 인스턴스 및 DB 클러스터

### Amazon Aurora 인스턴스 및 DB 클러스터

Amazon Aurora 인스턴스 및 DB 클러스터

• Amazon Aurora 인스턴스를 생성하면 데이터베이스(DB) 클러스터가 만들어집니다. • Aurora DB 클러스터는 하나 이상의 DB 인스턴스와 해당 DB 인스턴스에 대한 데이터를 관리하는 클러스터 볼륨으로 구성됩니다. 

### Aurora 클러스터 볼륨

클러스터 볼륨

안정성, 고가용성, 속도

Aurora 클러스터 볼륨은 여러 가용 영역에 걸쳐 있는 가상 데이터베이스 스토리지 볼륨입니다. 각 가용 영역에는 DB 클러스터 데이터의 복사본이 있습니다. Aurora DB 클러스터는 2가지 유형의 DB 인스턴스로 구성됩니다. 

- 프라이머리 인스턴스
- 오로라 인스턴스

###  Amazon Aurora DB 클러스터란 무엇입니까?



2가지 유형의 Amazon Aurora DB 클러스터 

• 프라이머리 인스턴스는 읽기 및 쓰기 작업을 지원하고, 클러스터 볼륨의 모든 데이터 변경을 실행합니다. 각 Aurora DB 클러스터에는 프라이머리 인스턴스가 하나씩 있습니다. 

• Aurora 복제본은 읽기 작업만 지원합니다. 각 Aurora DB 클러스터는 프라이머리 인스턴스 이외에 최대 15개의 Aurora 복제본을 가질 수 있습니다. 여러 복제본이 읽기 워크로드를 분산하고 별도의 가용 영역에 있는 경우 데이터베이스의 가용성을 높일 수 있습니다.





### Amazon Aurora DB 클러스터 아키텍처

![image-20231027144919199](/../images/2023-10-27-Amazon Aurora/image-20231027144919199.png)



## 용례

### 엔터프라이즈 애플리케이션 용례



Aurora 는 상용 데이터베이스와 비교하여 데이터베이스 비용을 90% 이상 낮추면서도 데이터베이스의 안정성과 가용성은 높일 수 있습니다.

### Software as a Service(SaaS)애플리케이션 용례

이 경우 Aurora는 관리형 데이터베이스 제품의 기능을 제공합니다. 따라서 SaaS 회사는 애플리케이션을 구동하는 기본 데이터베이스에 대해 걱정하지 않고 고품질 애플리케이션을 구축하는 데 집중할 수 있습니다.

### 웹 및 모바일 게임 용례

웹 및 모바일 게임은 대규모로 운영되도록 구축되었기 때문에 높은 처리량과 방대한 스토리지 확장성을 갖춘 데이터베이스가 필요합니다. Aurora는 미래 성장을 위한 충분한 여지를 제공합니다.

### 데이터베이스 오류 후 Aurora

Aurora • 마지막 데이터베이스 체크포인트에서 다시 실행 로그를 재생할 필요가 없습니다. • 대부분의 경우 데이터베이스 오류가 발생한 후 재시작 시간이 60초 미만으로 줄어듭니다.

## 학습 내용 확인

1. Aurora란 무엇입니까?

2. Amazon RDS에서 SQL 대신 Aurora를 사용해야 하는 이유는 무엇입니까?

   빠른 속도, 고성능 및 확장성 • 고가용성 및 내구성

3. Amazon Aurora DB 클러스터의 2가지 유형의 인스턴스란 무엇입니까?

   프라이머리 인스턴스 오로라인스턴스

##  핵심 사항

고성능 및 확장성 • 고가용성 및 내구성 • 여러 수준의 보안 • MySQL 및 PostgreSQL과 호환 가능 • 완전관리형