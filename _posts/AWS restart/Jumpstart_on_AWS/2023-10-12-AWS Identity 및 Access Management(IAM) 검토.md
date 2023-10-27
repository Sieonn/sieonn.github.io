---
title: "AWS Identity 및 Access Management(IAM) 검토"
toc: true
category: Jumpstart on AWS

---

## AWS Identity 및 Access Management(IAM) 검토

---

### IAM 검토

AWS Identity 및 Access Management(IAM)

인증과 AWS 리소스에 대한 액세스를 중앙에서 관리할 수 있습니다.

- 추가 비용 없이 AWS 계정의 기능으로 제공됩니다.
- 사용자, 그룹 및 역할을 생성합니다.
- 여기에 정책을 적용하여 AWS 리소스에 대한 액세스를 제어합니다.

### AWS 서비스 액세스

프로그래밍 방식 액세스

- 액세스 키 ID와 보안 액세스 키를 인증합니다. 
- 애플리케이션 프로그램 인터페이스(API), AWS Command Line Interface(AWS CLI), 소프트웨어 개발 키트(SDK) 및 기타 개발 도구에 대한 액세스를 제공합니다.

콘솔 액세스

- 계정 ID 또는 별칭, IAM 사용자 이름 및 암호를 사용합니다. 
- 이 옵션을 활성화하면 MFA에서 인증 코드를 묻습니다.

### 보안 인증 정보의 유형

| 인증 정보의 유형        | 설명                                                         |
| ----------------------- | ------------------------------------------------------------ |
| 이메일 주소 및 암호     | AWS 계정(루트 사용자)과 연결됨                               |
| IAM 사용자 이름 및 암호 | AWS Management Console 액세스에 사용됨                       |
| 액세스 키               | 일반적으로 API 및 SDK를 통한 프로그래밍 방식 요청 및 AWS CLI와 함께 사용됨 |
| 다중 요소 인증(MFA)     | 추가 보안 계층 계정 루트 사용자 및 IAM 사용자에 대해 활성화할 수 있음 |
| 키 페어                 | Amazon Elastic Compute Cloud(Amazon EC2)와 같은 특정 AWS 서비스에만 사용됨 |



### 정책 및 권한

![image-20231012105950685](/../images/2023-10-12-AWS Identity 및 Access Management(IAM) 검토/image-20231012105950685.png)

권한정책에서 권한은 Rights, policy, permisson으로 나뉠수 있는데, Permission은 리소스에 대한 권한이라고 합니다.

권한 정책에서 정책은 json문서

경계는 Boundary를 말하는데 권한이 최대 사용되는 범위를 말한다.

권한 경계는 하나의 권한이 어디까지 사용할 수 있는가에 대한 이야기인데, 다른 경계와 충돌한다면 중복된 부분만 권한 행사를 할 수 있는 경계입니다.

관리형 정책

인라인 정책
사용자가 만들 수 있는 정책인데, 정책과 identity(사용자, 그룹, 역할)가 1대 1로 맵핑하는 권한입니다.

`IAM 정책 예시:`

```
{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "MFA-Access",
"Effect": "Allow",
"Action": "ec2:*",
"Resource": "*",
"Condition": {
"BoolIfExists": {
"aws:MultiFactorAuthPresent": "true"
},
"IpAddress": {
"aws:SourceIp": "1.2.3.4/32"
}
}
}
]
}
```

### IAM 역할 사용하기

![image-20231012110101188](/../images/2023-10-12-AWS Identity 및 Access Management(IAM) 검토/image-20231012110101188.png)

### IAM 사용자 역할 위임

사용자 기반 권한

![image-20231012110134971](/../images/2023-10-12-AWS Identity 및 Access Management(IAM) 검토/image-20231012110134971.png)

리소스 기반 권한

![image-20231012110150977](/../images/2023-10-12-AWS Identity 및 Access Management(IAM) 검토/image-20231012110150977.png)s

### IAM  모범 사례

![image-20231012110211361](/../images/2023-10-12-AWS Identity 및 Access Management(IAM) 검토/image-20231012110211361.png)

### 핵심 사항

- IAM은 세 가지 유형의 아이덴티티를 사용합니다. 
  - – 사용자 
  - – 그룹 
  - – 역할 
- AWS 리소스는 콘솔(웹 페이지)이나 AWS CLI를 통해 또는 프로그래밍 방식으로 액세스할 수 있습니다. 
- IAM 정책은 권한을 정의하는 JSON 문서입니다. 이 권한은 사용자, 그룹, 역할에 적용됩니다. •
-  역할을 통해 사용자는 일시적으로 역할로 정의된 특정 권한을 위임할 수 있습니다.
-  일상적인 관리 태스크에는 계정 루트 사용자를 사용하지 마십시오.
-  권한을 할당할 때 최소 권한의 원칙을 사용하십시오. 
- 역할을 사용해 교차 계정 액세스를 제공하십시오. 
- 가능한 경우 MFA를 사용하십시오.