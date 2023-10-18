---
title: "Amazon S3"
toc: true
toc_label: "Amazon S3"
toc_sticky: true
---

## Amazon S3

### Amazon S3

관리형 클라우드 스토리지 솔루션

- 데이터는 버킷 내에 객체로 저장됨
- 사실상 무제한의 스토리지
  - 객체 크기는  최대 5TB
- 99.999999999%의 내구성을 보장하도록 설계  
- 버킷 및 객체에 대한 세분화된 액세스

### Amazon S3 기능

- 사실상 원하는 만큼 많은 수의 객체를 저장 가능  
- 기본값으로 모든 데이터는 프라이빗 유형이며 선택적으로 암호화할 수 있음  
- 데이터는 중복으로 저장됨  
- 언제, 어디서나 인터넷을 통해 데이터 검색 가능  
- 버킷 이름은 Amazon S3에 있는 어떤 기존 버킷 이름과도 중복되지 않아야 함

### Amazon S3 스토리지 클래스

Amazon S3는 다양한 용례에 맞게 설계된 다양한 객체 수준 스토리지 클래스를 제공합니다. 

- AWS Cloud Amazon S3 
-  Amazon S3 Standard  
- Amazon S3 Intelligent-Tiering  
- Amazon S3 스탠더드-저빈도 액세스(Amazon S3 스탠더드-IA)  
- Amazon S3 단일 영역 - 저빈도 액세스(Amazon S3 단일 영역 - IA)  
- Amazon Simple Storage Service Glacier  
- Amazon S3 Glacier Deep Archive

### 어디서나 데이터에 액세스

![image-20231018202724243](/../images/2023-08-25-Amazon Simple Storage Service/image-20231018202724243.png)

### Amazon S3 버킷 및 객체 URL 구조

![image-20231018202758197](/../images/2023-08-25-Amazon Simple Storage Service/image-20231018202758197.png)

### Amazon S3에서의 중복

**데이터가 리전에 중복으로 저장되는 방식**

![image-20231018202831792](/../images/2023-08-25-Amazon Simple Storage Service/image-20231018202831792.png)

### 원활한 크기 조정

**원활한 크기 조정을 고려하여 설계된 Amazon S3** 

![image-20231018202917531](/../images/2023-08-25-Amazon Simple Storage Service/image-20231018202917531.png)

### Amazon S3의 일반 용례

- 애플리케이션 자산 저장
- 정적 웹 호스팅
- 백업 및 재해 복구(DR)
- 빅 데이터를 위한 스테이징 영역
- 그 외 다수의 사례가 있습니다.

### Amazon S3  요금제

**사용량에 대해서만 요금 지불**: 

- 월별 GB  
- 다른 리전으로 송신  
- PUT, COPY, POST, LIST 및 GET 요청 

**다음에 대해서는 비용을 지불할 필요가 없음**  

Amazon S3에서 수신  

Amazon S3에서 같은 리전의 Amazon CloudFront 또는 Amazon EC2로 송신

### Amazon S3 비용 추정

**Amazon S3 비용을 추정하려면 다음 사항을 고려합니다**.

1. 스토리지 클래스 유형 

   – 스탠더드 스토리지는 다음을 보장하도록 설계됨 

   ​		» 99.999999999%의 내구성 

   ​		» 99.99%의 가용성 

   – Standard-Infrequent Access(S-IA)는 다음을 보장하도록 설계됨 

   ​		» 99.999999999%의 내구성 

   ​		» 99.9%의 가용성 

   `스토리지 클래스를 뭘 사용하느냐에 따라서 달라질 수 있습니다.`

2. 스토리지 용량 

   – 객체 수와 크기 Amazon S3 비용 추정

3. 요청  

   – 요청 수 및 유형(GET, PUT, COPY) 

   – 요청 유형

   ​		» GET 요청은 다른 요청과 다른 요금이 적용 

4. 데이터 전송 

   – 요금제는 Amazon S3 리전에서 송신된 데이터의 양에 따라 부과 

   ​		» 데이터 수신은 무료이지만 송신된 데이터에 대해서는 요금이 발생

   `Amazon S3는 기본값으로 S3버킷에 저장된 데이터는 프라이빗 데이터이며, 데이터를 퍼블릭으로 전환하려면 이 설정을 비활성화 해야한다.`

---

##  ➕ 추가 개념 정리

### 네트워크

소프트웨어 - IP 주소

하드웨어 = MAC 주소

IPv4(32bit) > 그 당시 인터넷 발전으로 인해 주소가 부족할 것이라는 생각을 못했습니다. 그 이후 IPv6가 생겼습니다.

IPv4는 32bit입니다.

00000000 00000000 00000000 00000000

0.0.0.0 ~ 255.255.255.255

Class는 A, B, C, D가 있습니다.

IP주소는 Data를 전달하기 위해 통신에 사용하는 주소입니다.

`Ex) 192.168.10.32`

맨 앞: Net-ID  맨 뒤: Host-ID

Net-ID는 고정값으로 바꿀 수 없습니다. 그러나 Host-ID는 변경이 가능합니다.

서브넷 마스크(Subnet mask): Net-ID와 Host-ID를 식별해주는 값

1은 Net-ID를 표시

0은 Host-ID를 표시

ABCDE클래스 중에 직접 쓸 수 있는것은 ABC까지다.

![image](/../images/2023-08-25-Amazon Simple Storage Service/image.png)

Subneting :IP주소를 나누는 방법

Subnet이란?

IP주소에서 하나의 네트워크가 분할 되어 나눠진 작은 네트워크

- VLSM

네트워크 엔지니어가 IP주소를 필요에 따라 분할하여 필요한 만큼 IP주소를 할당하여 IP주소의 낭비를 막는 기술

- CIDR(Classless Inter-Domain Routing) :클래스 고갈로 인해 더 이상 사용하지 못할 것을 대비한 것입니다. 슈퍼네팅(superneting)이라고도하며, IP주소 할당 방법으로 기존의 Class기반으로 할당하던 방식을 대체 합니다.

  {: .notice}

  전 세계 인터넷 라우팅 테이블의 증가 속도를 늦추는것과 IPv4주소의 고갈속도를 감소시키는것이 목적

## 핵심 요점

- Amazon S3는 완전 관리형 클라우드 스토리지 서비스  
- Amazon S3에서 사용자는 데이터를 버킷 내 객체로서 저장  
- 객체를 사실상 무제한으로 저장 가능  
- 사용량에 대해서만 요금 지불  
- 언제 어디서나 URL을 통해 Amazon S3에 액세스 가능

## Knowledge Check

1. Amazon S3 버킷에서 객체를 고유하게 식별하는 속성은 무엇입니까
   - [x] 객체 값
   - [ ] 객체 키
   - [ ] 버전
   - [ ] 메타데이터

<br>

2. Amazon S3는 몇 퍼센트의 내구성을 제공하도록 설계되었습니까?
   - [ ] 99.99 
   - [ ] 99.9999 
   - [ ] 99.999999 
   - [x] 99.999999999

<br>

3. 한 금융 회사가 장기 스토리지를 위해 가장 낮은 비용의 Amazon S3 솔루션을 사용하고자 합니다. 이 회사는 1년에 한 두 번만 데이터에 액세스하면 됩니다. 다음 중 어떤 Amazon S3 스토리지 클래스를 선택해야 합니까?
   - [x] S3 Glacier Deep Archive
   - [ ] S3 Standard - Infrequent Access(S3 Standard-IA)
   - [ ] S3 Standard
   - [ ] S3 One Zone-Infrequent Access(S3 One Zone-IA)

<br>

4. Amazon S3를 사용할 때 비용이 발생하는 작업은 무엇입니까
   - [ ] Amazon S3로 데이터 전송
   - [ ] Amazon S3에서 Amazon CloudFront로 데이터 전송
   - [x] 다른 AWS 리전으로 데이터 전송
   - [ ] 5MB를 초과하는 데이터를 Amazon S3로 전송

<br>

5. 다음 중 Amazon S3에 대한 설명은 어느 것입니까? (2개 선택)
   - [ ] 동적 웹 호스팅에 사용할 수 있습니다.
   - [x] 정적 웹 호스팅에 사용할 수 있습니다.
   - [ ] 버킷 이름은 AWS 계정마다 다르며 각 AWS 계정 내에서 고유해야 합니다.
   - [x] 버킷 이름은 범용으로, Amazon S3에 있는 어떤 기존 버킷 이름과도 중복될 수 없습니다.
   - [ ] 기본값으로 S3 버킷에 저장된 데이터는 퍼블릭 데이터이며, 데이터를 프라이빗으로 전환하려면 이 설정을 비활성화해야 합니다.