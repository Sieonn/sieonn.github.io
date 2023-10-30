---
title: "AWS Transfer Family 및 기타 마이그레이션 서비스"
toc_label: "AWS Transfer Family 및 기타 마이그레이션 서비스"
toc: true
toc_sticky: true
---

**AWS Transfer Family**는 SFTP용 AWS Transfer, FTPS용 AWS Transfer 및 FTP용 AWS Transfer를 통합한 이름입니다. AWS Transfer는 SFTP, FTPS 및 FTP 를 통해 Simple Storage Service (Amazon S3)에서 파일을 송수신할 수 있는 완전관리형 지원을 제공합니다.

## 핵심 데이터 모델 개념

### AWS Transfer Family

AWS Transfer Family는 다음 프로토콜 유형을 지원합니다. 

AWS Transfer Family는 SFTP용 AWS Transfer, FTPS용 AWS Transfer 및 FTP 용 AWS Transfer를 통합한 이름입니다. 

FTP는 파일 전송 프로토콜(File Transfer Protocol)의 약자로, 데이터 전송에 사용되는 네트워크 프로토콜입니다. 

SFTP는 SSH 파일 전송 프로토콜(SSH File Transfer Protocol)의 약자로, 인터넷을 통한 보안 데이터 전송에 사용되는 네트워크 프로토콜입니다. 

FTPS는 SSL을 통한 파일 전송 프로토콜(File Transfer Protocol over SSL)의 약자로, FTP가 확장된 프로토콜입니다. FTPS는 전송 계층 보안(TLS)과 보안 소켓 계층(SSL) 암호화 프로토콜을 사용하여 트래픽을 암호화합니다. 

### SFTP 전송에 사용되는 AWS

- AWS Transfer Family는 SFTP, FTPS 및 FTP 표준과 완전하게 호환됩니다.  
- Microsoft Active Directory, Lightweight Directory Access Protocol (LDAP), Okta 등과 같은 아이덴티티 공급자 시스템과 직접 연결됩니다.

SFTP용 AWS Transfer 

|기존 워크플로 유지|간편한 사용|데이터가 Amazon Simple Storage Service (Amazon S3) 버킷에 저장됨|

|SFTP용 AWS Transfer |

### AWS Transfer Family

![image-20231030141940070](/../../images/2023-10-30-AWS Transfer Family 및 키타 마이그레이션 서비스/image-20231030141940070.png)

## AWS DataSync

**AWS DataSync**는 온프레미스 스토리지 시스템과 AWS 스토리지 서비스 간의 데이터 이동을 간소화, 자동화, 가속화하는 온라인 데이터 전송 서비스입니다. AWS 스토리지 서비스 간에도 데이터를 전송합니다

### AWS DataSync

**DataSync**는 Network File System (NFS Server Message Block (SMB) 파일 서버, 셀프 매니지드 객체 스토리지, AWS Snowcone, S3 버킷, Amazon Elastic File System (Amazon EFS) 파일 시스템 Windows File Server 용 Amazon FSx 파일 시스템 간에 데이터를 복사할 수 있습니다. 

**AWS DataSync**

- 효율적이고 빠름
- 관리형 서비스
- AWS DataSync 에이전트(NFS 프로토콜)
- 온프레미스와 AWS 간 동기화
- 인터넷 또는 AWS Direct Connect를 통해 연결

## 핵심 데이터 모델 개념 및 용례

### AWS DataSync

![image-20231030142056202](/../../images/2023-10-30-AWS Transfer Family 및 키타 마이그레이션 서비스/image-20231030142056202.png)

### DataSync 용례

**주요 용례**

- **데이터 마이그레이션** - 네트워크를 통해 활성 데이터 세트를 Amazon S3, Amazon EFS 또는 Windows File Server용 Amazon FSx로 신속하게 이동시킵니다.  
- **콜드 데이터 아카이브** - 온프레미스 스토리지에 저장된 콜드 데이터를 Amazon S3 Glacier 또는 Amazon S3 Glacier Deep Archive와 같은 내구성 있고 안전한 장기 스토리지로 이동시킵니다.  
- **데이터 보호** - 요구 사항에 맞으면서 가장 비용 효율적인 스토리지 클래스를 선택하여 데이터를 Amazon S3 스토리지 클래스로 이동시킵니다.  
- **적시의 클라우드 내 처리를 위한 데이터 이동** - 온프레미스에서 데이터를 생성하는 시스템에서 작업할 때 처리를 위해 AWS와 데이터를 송수신합니다. 

## AWS Snowball

**AWS Snowball**은 안전하고 견고한 디바이스를 제공하는 서비스입니다. AWS 컴퓨팅 및 스토리지 기능을 엣지 환경으로 가져오고 AWS와 데이터를 주고 받을 수 있습니다.

 **AWS Snowball Edge**는 AWS Snowball 서비스에서 제공하는 엣지 컴퓨팅 및 데이터 전송 디바이스입니다. Snowball Edge는 40개의 vCPU 컴퓨팅 용량과 함께 80테라바이트의 사용 가능한 블록 또는 Amazon S3와 호환되는 객체 스토리지를 제공합니다. 

**AWS Snowcone**은 가장 크기가 작은 디바이스로, 사용 가능한 스토리지가 8테라바이트입니다. Snowcone은 견고하고 안전하며 데이터 센터 외부에서 사용하도록 설계되었습니다. 

**AWS Snowmobile**은 45피트(13.7m) 길이의 배송 컨테이너로, **최대 100PB의 데이터**를 저장할 수 있습니다. Snowmobile은 **수 페타바이트 또는 엑사바이트 규모**의 디지털 미디어 마이그레이션과 데이터 센터 폐쇄 시 적합합니다. 이것은 보다 안전하고 빠른 데이터 전송을 위해 고객의 현장으로 방문합니다. 

## 핵심 데이터 모델 개념 및 용례

### AWS Snowball

![image-20231030142219712](/../../images/2023-10-30-AWS Transfer Family 및 키타 마이그레이션 서비스/image-20231030142219712.png)

### AWS Snowball 데이터 전송 용례

**주요 용례**

- **센서 또는 머신** - 병원, 공장 현장 또는 기타 엣지 로케이션에서 센서 또는 시스템이 지속적으로 생성하는 데이터를 AWS에 전송합니다.  
- **원격 위치에서 데이터 수집** - 연결이 제한적이거나, 대역폭에 제약이 있거나, 네트워크 연결 비용이 많이 들거나, 기존 환경에 문제가 있거나, 데이터가 원격 위치에서 수집되는 상황에서 데이터를 전송하는 데 도움이 됩니다.  
- **미디어 및 엔터테인먼트 집계 콘텐츠** - 미디어 및 엔터테인먼트, 드론 작업자 및 기타 콘텐츠 제작자는 Snowball을 사용하여 영화 세트 및 사진 촬영 카메라의 콘텐츠를 수집 및 인코딩한 후에 데이터를 Amazon S3으로 마이그레이션합니다. 

### AWS에서의 데이터 전송 및 마이그레이션

![image-20231030142312175](/../../images/2023-10-30-AWS Transfer Family 및 키타 마이그레이션 서비스/image-20231030142312175.png)

## 핵심 사항

- AWS Transfer Family는 다양한 프로토콜을 사용하여 Amazon S3와 데이터를 송수신할 수 있는 완전관리형 서비스 그룹입니다.  
- AWS DataSync는 인터넷 또는 AWS Direct Connect를 통해 온프레미스 스토리지 시스템과 AWS 스토리지 서비스 간 데이터 이동 및 복제를 단순화, 자동화 및 가속화하는 데이터 전송 서비스입니다.  
- AWS Snowball은 대규모 데이터를 전송해야 하는 고객을 위한 디바이스 기반 솔루션입니다. 