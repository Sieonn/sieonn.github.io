---
title: "AWS Elastic Beanstalk"
toc: true
toc_sticky: true
toc_label: "AWS Elastic Beanstalk"
---

## AWS Elastic Beanstalk 소개

###  Elastic Beanstalk란

- 서비스형 플랫폼(PaaS) 
- 신속한 웹 애플리케이션 배포, 크기 지정 및 관리 
- 관리의 복잡도 감소 
- 다음과 같이 리소스를 꾸준히 제어합니다.  
  - 인스턴스 유형 선택  
  - 데이터베이스 선택  
  - Amazon EC2 Auto Scaling 설정 및 조정  
  - 애플리케이션 업데이트  
  - 서버 로그 파일에 액세스  
  - 로드 밸런서에서 보안 HTTP(S) 활성화

다양한 플랫폼 및 언어를 지원합니다. 

- Packer Builder 
- 단일 컨테이너, 다중 컨테이너 또는 사전 구성된 Docker 
- Go 
- Java SE 
- Java with Tomcat 
- IIS를 사용하는 Windows Server의 .NET 
- Node.js 
- PHP 
- Python 
- Ruby 

Elastic Beanstalk는 무료입니다. 사용한 기본 서비스 비용만 지불하면 됩니다.

### Elastic Beanstalk 구성 요소

![image-20231017105036368](/../images/2023-10-17-AWS Elastic Beanstalk/image-20231017105036368.png)

## 학습 내용 확인

1. AWS Elastic Beanstalk 환경이 배포되면 사용자가 수정할 수 있는 리소스는 무엇입니까?
2. 엔지니어는 로드 밸런서, Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스 4개, Amazon Relational Database Service(Amazon RDS)에서 실행되는 MySQL 데이터베이스가 포함된 AWS Elastic Beanstalk 환경을 배포합니다. (참고: 배포되는 리소스의 비용은 고려하지 마십시오.) Elastic Beanstalk를 사용하여 이 환경을 배포하는 데 드는 비용은 얼마입니까?

## 핵심 사항

- AWS Elastic Beanstalk는 애플리케이션 배포 프로세스를 간소화하여 개발자 생산성을 향상시킵니다.
  - 관리 복잡성을 줄입니다. 
- Elastic Beanstalk는 무료입니다. 요금은 사용한 서비스에 대해서만 지불하면 됩니다. 