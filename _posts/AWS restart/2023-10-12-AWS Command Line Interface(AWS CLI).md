---
title: "AWS Command Line Interface(AWS CLI)"
toc: true
---

## AWS Command Line Interface(AWS CLI)



### AWS를 사용하는 3가지 방법

![image-20231012111629996](/../images/Untitled/image-20231012111629996.png)

- AWS 관리 콘솔
  -  사용하기 쉬운 AWS 그래픽 인터페이스
- AWS Command Line Interface(AWS CLI)
  - Linux, Microsoft Windows 또는 macOS 명령줄을 통해 AWS 서비스에 액세스
- 소프트웨어  개발 키드(SDK)
  - 대부분의 주요 프로그래밍 언어에서 AWS 서비스 애플리케이션 프로그램 인터페이스(API) 호출

### Linux에 AWS CLI 설치

1. pip를 사용하여 AWS CLI를 설치하려면 다음 명령을 실행합니다.

   `pip3 install awscli --upgrade --user`

2. 설치를 확인하려면 다음 명령을 실행합니다.

   `aws --version`

예상 결과

`aws-cli/1.16.137 Python/3.7.3 Linux/4.14.77-81.59-amzn2.x86_64 botocore/1.12.127`

### AWS CLI 소개

**AWS Command Line Interface(AWS CLI)**

- Linux, Microsoft Windows 및 macOS에서 사용 가능.
- aws configure 명령을 사용하여 기본 설정을 지정합니다.

![image-20231012113155317](/../images/2023-10-12-AWS Command Line Interface(AWS CLI)/image-20231012113155317.png)

### 명령줄 형식

명령줄 형식은 몇 부분으로 나눌 수 있습니다.

![image-20231012113228778](/../images/2023-10-12-AWS Command Line Interface(AWS CLI)/image-20231012113228778.png)

### AWS CLI help

AWS CLI의 모든 명령에 구문과 사용할 수 있는 명령의 예시가 있습니다. 이 예시는 <span style="background-color:#cceecc">help</span> 명령으로 액세스할 수 있습니다

![image-20231012113331183](/../images/2023-10-12-AWS Command Line Interface(AWS CLI)/image-20231012113331183.png)

### AWS CLI 출력(JSON 형식)

![image-20231012113406249](/../images/2023-10-12-AWS Command Line Interface(AWS CLI)/image-20231012113406249.png)

###  결과 제한: --query 옵션

**--query 옵션을 사용하여 결과 집합에 표시되는 필드를 제한합니다**

![image-20231012113440212](/../images/2023-10-12-AWS Command Line Interface(AWS CLI)/image-20231012113440212.png)

### 결과 제한

**--filter 옵션**

- --filter 옵션은 서버 측에서 필터링된 결과 집합을 제한하는 데 사용됩니다.

- Microsoft Windows 인스턴스만 표시:

  `aws ec2 describe-instances –-filter "Name=platform,Values=windows"`

- 해당 계정에 있는 모든 인스턴스의 InstanceID를 찾고 t2.micro 및 t2.small 인스턴스의 인스턴스 ID만 표시:

  `aws ec2 describe-instances \ `
  `--query"Reservations[*].Instances[*].InstanceId” \ `
  `–-filter “Name=instance-type,Values=t2.micro,t2.small”`

### 쿼리의 작동 원리

![image-20231012113706722](/../images/2023-10-12-AWS Command Line Interface(AWS CLI)/image-20231012113706722.png)

![image-20231012113736530](/../images/2023-10-12-AWS Command Line Interface(AWS CLI)/image-20231012113736530.png)

### 기타 AWS CLI 옵션: --dry run

--dry run 옵션:

- 요청을 수행하지 않고 필요한 권한을 확인합니다. 
-  사용 권한이 없으면 오류 응답을 제공합니다

{: .notice}

aws ec2 run-instances --image-id ami-1a2b3c4d 
--count 1 
--instance-type c5.large --key-name MyKeyPair 
--security-groups MySecurityGroup --dry-run

### 일반적인 AWS CLI 명령

![image-20231012113937754](/../images/2023-10-12-AWS Command Line Interface(AWS CLI)/image-20231012113937754.png)

### 핵심 사항

- --filter 옵션은 반환될 리소스의 세부 정보 범위를 지정하는 서버 측 작업입니다. 
-  --query 옵션은 서버에서 반환된 결과 중 표시할 개수를 제한하는 클라이언트 측 작업입니다.
-  --dry run 옵션은 요청을 하지 않고 필요한 권한을 확인합니다.  
- --output