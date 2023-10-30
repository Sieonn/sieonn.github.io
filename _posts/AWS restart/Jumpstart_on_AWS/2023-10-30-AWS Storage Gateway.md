---
title: "AWS Storage Gateway"
---

## Storage Gateway

**Storage Gateway**는 온프레미스 애플리케이션에서 AWS 클라우드 스토리지를 사용할 수 있도록 지원하는 하이브리드 스토리지 서비스입니다. Storage Gateway는 백업, 아카이브, 재해 복구(DR), 클라우드 데이터 처리, 스토리지 계층화 및 마이그레이션에 사용할 수 있습니다

## 핵심 데이터 모델 개념

### Storage Gateway

- 애플리케이션은 가상 머신 또는 하드웨어 게이트웨이 어플라이언스를 통해 이 서비스에 연결됩니다.  
- Storage Gateway는 표준 스토리지 프로토콜을 사용합니다. – Network File System(NFS) – Server Message Block(SMB) – Internal Small Computer Interface(iSCSI)  
- 게이트웨이가 AWS 스토리지 서비스에 연결됩니다. – Amazon Simple Storage Service(Amazon S3) – Amazon Simple Storage Service Glacier – Amazon Elastic Block Store(Amazon EBS)  
- Storage Gateway는 AWS에서 다음을 위한 스토리지를 제공합니다. 
  - 파일 `(Ex) EFS`
  - 볼륨 `(Ex) EBS`
  - 가상 테이프

온프레미스 애플리케이션이 AWS Cloud에 있는 데이터에 액세스할 수 있게 해주는 하이브리드 클라우드 스토리지

|File Gateway|Volume Gateway|Tape Gateway|

### Storage Gateway는 세 가지 솔루션을 제공합니다.

|                     | File Gateway                           | Volume Gateway                        | Tape Gateway                                                 |
| ------------------- | -------------------------------------- | ------------------------------------- | ------------------------------------------------------------ |
| 목적                | 클라우드 기반 파일 스토리지 제공       | 클라우드 기반 스토리지 볼륨 제공      | 클라우드 기반 가상 테이프 스토리지 제공                      |
| AWS 스토리지 서비스 | - Amazon S3 <br /> - Amazon S3 Glacier | - Amazon S3 <br />- Amazon EBS 스냅샷 | - Amazon S3  Amazon S3 Glacier <br />- Amazon S3 Glacier Deep Archive |
| 프로토콜            | - NFS <br />- SMB                      | iSCSI                                 | iSCSI                                                        |

**온프레미스 배포**(세가지 Gateway의 공통 사항)

모든 게이트웨이 솔루션은 다음에서 실행할 수 있는 가상 머신(VM)으로 온프레미스 환경에 배포됩니다. 

- VMware ESXi 
- Microsoft Hyper-V `(Ex) SMB`
- Linux 커널 기반 가상 머신

### Storage Gateway

![image-20231030140930238](/../../images/2023-10-30-AWS Storage Gateway/image-20231030140930238.png)

## 스토리지 게이트웨이가 AWS Cloud와 접속하는 방법

### File Gateway

![image-20231030141001778](/../../images/2023-10-30-AWS Storage Gateway/image-20231030141001778.png)

### Volume Gateway

![image-20231030141015473](/../../images/2023-10-30-AWS Storage Gateway/image-20231030141015473.png)

### Tape Gateway

![image-20231030141026537](/../../images/2023-10-30-AWS Storage Gateway/image-20231030141026537.png)

## Storage Gateway 용례

### Storage Gateway 용례

하이브리드 클라우드의 세 가지 주요 용례 

- 클라우드에 더 많이 백업하고 아카이브합니다.  클라우드 기반 파일 공유를 통해 온프레미스 스토리지를 줄입니다.  온프레미스 애플리케이션에서 AWS에 저장된 데이터에 낮은 대기 시간으로 액세스합니다.

## 핵심 사항

- Storage Gateway는 온프레미스에 위치하며, 로컬 환경을 AWS Cloud로 연결합니다.  
- 일부 스토리지는 온프레미스에 있어야 하지만 일부 스토리지는 클라우드 스토리지 서비스(Amazon S3, Amazon S3 Glacier, Amazon EBS)에 오프로드할 수 있는 하이브리드 시나리오에 Storage Gateway를 사용하십시오.  
- Storage Gateway는 파일, 볼륨, 테이프의 세 가지 옵션을 제공합니다.