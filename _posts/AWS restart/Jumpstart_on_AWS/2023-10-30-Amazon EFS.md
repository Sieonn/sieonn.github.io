---
title: "Amazon Elastic File System(Amazon EFS)"
toc_label: "Amazon Elastic File System(Amazon EFS)"
toc: true
toc_sticky: true
---

## Amazon Elastic File System(Amazon EFS)

Amazon EFS는 AWS 클라우드 서비스와 온프레미스 리소스에서 사용할 수 있는, 확장 가능하며 탄력적인 완전관리형 네트워크 파일 시스템(NFS) 스토리지입니다. 

### Amazon EFS

**기능** 

- 페타바이트 규모의 대기 시간이 짧은 파일 시스템  
- 탄력적 용량  
- NFS 지원  
- 모든 Amazon Elastic Compute Cloud(Amazon EC2)용 Linux 기반 Amazon Machine Image(AMI)와 호환

{: .notice}

Linux 기반 워크로드용 파일 시스템 스토리지

- 공유 파일 스토리지
- 페타 바이트 규모 파일 시스템
- 네트워크 파일 시스템 지원
- 모든 Amazon EC2용 Linux 기반 AMI와 호환

###  Amazon EFS 이점

-  탄력성

  AWS 서비스와 함께 사용할 수 있는 간단하고 확장 가능하며 탄력적인 파일 스토리지를 제공합니다.

- 동적 탄력성

  파일을 추가 또는 제거하면 자동으로 확장하거나 축소됩니다.

- 완전관리형

  Linux 워크로드용 공유 파일 시스템 스토리지를 제공합니다.

### Amazon EFS 성능 속성

성능 모드

- 범용  최대 I/O

스토리지 클래스

- 스탠더드  저빈도 액세스

처리량 모드

- 버스팅 처리량  프로비저닝된 처리량

## Amazon EFS 아키텍처 및 설정 예시

### Amazon EFS 아키텍처

Amazon EFS 아키텍처 다이어그램

![image-20231030135709697](/../../images/2023-10-30-/image-20231030135709697.png)

### Amazon EFS 파일 시스템 설정

1. Amazon EFS 파일 시스템을 생성합니다. 
2. 인스턴스 VPC에 탑재 대상을 생성합니다. 
3. 파일 시스템을 탑재 대상에 탑재합니다. 
4. EC2 인스턴스를 탑재 대상에 연결합니다.

## Amazon EFS 구현 및 리소스

### Amazon EFS 구현

Amazon EFS 아키텍처 다이어그램 재현

1. Amazon EC2 리소스를 생성하고 EC2 인스턴스를 시작합니다.
2. Amazon EFS 파일 시스템을 생성합니다. 
3. 적절한 서브넷에 탑재 대상을 생성합니다. 
4. EC2 인스턴스를 탑재 대상에 연결합니다. 
5. 리소스를 정리하고 AWS 계정을 보호합니다.

### Amazon EFS 리소스

탑재 대상 

- 서브넷 ID  
- 보안 그룹  
- 파일 시스템당 하나 이상  
- VPC 서브넷에서 생성  
- 가용 영역당 하나  
- Amazon EFS에 연결하려는 인스턴스는 동일한 VPC에 있어야 합니다.

태그 

 키-값 페어

## Amazon EFS 용례

### Amazon EFS 용례

Amazon EFS는 광범위한 워크로드 및 애플리케이션에 성능을 제공하도록 설계되었습니다.

{: .notice}

- 홈 디렉터리
- 엔터프라이즈 애플리케이션용 파일 시스템
- 애플리케이션 테스트 및 개발
- 데이터베이스 백업
- 웹  서비스 및 콘텐츠 관리
- 미디어 워크플로
- 빅 데이터 분석

## 핵심 사항

- Amazon EFS는 네트워크를 통해 파일 스토리지를 제공합니다.  
- 사용 사례: 
  - 빅 데이터 및 분석 
  - 미디어 처리 워크플로
  - 콘텐츠 관리
  - 웹 서비스
  - 홈 디렉터리  
- 콘솔, API 또는 AWS CLI에서 액세스할 수 있습니다.  
- Amazon EFS는 NFS 프로토콜을 사용하는 완전관리형 파일 시스템 스토리지 서비스입니다.  
- Amazon EFS를 사용하여 공유 파일 시스템 스토리지가 필요한 AWS 또는 온프레미스의 Linux 기반 워크로드를 지원하십시오.