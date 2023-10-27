---
title: "AWS Systems Manager"
toc: true
category: Jumpstart on AWS
---

## 도구 및 자동화 개요

- AWS Systems Manager의 목적과 기능 및 관련 기능 설명하기
- AWS Tool for PoserShell의 목적과 기능 설명하기
- 소프트웨어 개발 키트(SDK), AWS CloudFormation 및 AWS OpsWorks와 같은 도구 및 자동화에 사용되는 추가 개발 도구 식별하기
- Amazon Simple Storage Service(Amazon S3)를 사용하여 정적 웹사이트를 호스트하는 방법 설명하기

1. **AWS Systems Manager**

2. **추가 관리 및 개발 도구**

3. **Amazon S3 에서 정적 웹사이트 호스트**

## AWS System Manager

---

### AWS Systems Manager 개요

![image-20231012124347438](/../images/2023-10-12-도구 및 자동화개요/image-20231012124347438.png)

Fleet Manager:

리눅스를 들어가지 않고 Fleet Manager를 통해서 copy, move가 가능합니다.

### AWS Systems Manager 기능

![image-20231012124415246](/../images/2023-10-12-도구 및 자동화개요/image-20231012124415246.png)

### AWS Systems Manager 기능: 자동화

**자동화**

전체 AWS 리소스에서 공통적이고 반복적인 IT 운영 및 관리 작업을 안전하게 자동화합니다.

![image-20231012124515561](/../images/2023-10-12-도구 및 자동화개요/image-20231012124515561.png)

### AWS Systems Manager 기능: Run Command

**Run Command**

- 미리 정의된 명령 사용
- 자체 생성
- 인스턴스 또는 태그 선택
- 제어 또는 일정 선택
- 실행

### AWS Systems Manager 기능: 관리자

**세션 관리자**

인바운드 포트를 열거나 베스천 호스트를 사용하거나 Secure Shell(SSH) 키를 유지 관리할 필요 없이 인스턴스에 안전하게 연결합니다.

![image-20231012124736474](/../images/2023-10-12-도구 및 자동화개요/image-20231012124736474.png)

### AWS Systems Manager 기능: 패치 관리자

**패치관리자**

Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스 또는 온프레미스 머신의 대규모 그룹에 운영 체제 및 소프트웨어 패치를 자동으로 배포합니다.

![image-20231012124846387](/../images/2023-10-12-도구 및 자동화개요/image-20231012124846387.png)

### AWS Systems Manager 기능: 유지 관리 기간

**유지 관리 기간** 

인스턴스에서 관리 및 유지 관리 작업을 실행할 시간을 예약합니다

![image-20231012124924132](/../images/2023-10-12-도구 및 자동화개요/image-20231012124924132.png)

### AWS Systems Manager 기능: 상태 관리자

**상태 관리자**

Amazon EC2  또는 온프레미스 인스턴스의 일관된 구성을 유지 관리합니다.

![image-20231012131521097](/../images/2023-10-12-도구 및 자동화개요/image-20231012131521097.png)

### AWS Systems Manager 기능: 파라미터 스토어

![image-20231012131602864](/../images/2023-10-12-도구 및 자동화개요/image-20231012131602864.png)

### AWS Systems Manager 기능: 인벤토리

**인벤토리**

인스턴스와 인스턴스에 설치된 소프트웨어에 대한 정보를 수집합니다.

![image-20231012131657041](/../images/2023-10-12-도구 및 자동화개요/image-20231012131657041.png)

### AWS Systems Manager 기능: 인사이트

**인사이트**

인사이트 대시보드에는 각 리소스에 대한 운영 데이터가 표시됩니다.

- AWS CloudTrail의 애플리케이션 프로그램 인터페이스(API) 호출
- AWS Config의 리소스 구성 변경 사항
- 소프트웨어 인벤토리
- 리소스 그룹별 패치 규정 준수 상태

![image-20231012131839388](/../images/2023-10-12-도구 및 자동화개요/image-20231012131839388.png)

### 핵심 사항

- Systems Manager를 사용하면 AWS 리소스 전체에서 **일반적인 반복 IT 작업 및 관리 작업 자동화**를 안전하게 할 수 있습니다. 
-  Systems Manager는 **AWS 및 온프레미스 리소스**에서 운영 작업을 **자동화**하는 데 도움이 되는 기능 모음을 제공합니다. 
-  **패치 관리자** 및 **유지 관리 기간** 기능을 사용하여 **사전 정의된 일정**에 따라 **운영 체제 패치를 적용**할 수 있습니다.