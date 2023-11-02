---
title: "AWS CloudFormation"
toc_label: "AWS CloudFormation"
toc: true
toc_sticky: true
---

## 클라우드 배포의 당면 과제

### 클라우드 배포의 당면 과제

클라우드 배포 시 당면 과제는 다음과 같습니다.

![image-20231101114537313](/../images/2023-11-01-coludFormation/image-20231101114537313.png)

이런 일들을 해결 할 수 있는 방법이 **자동화**, 타라폼,엔서블, 클라우드 포메이션 입니다.

## AWS CloudFormation

### AWS CloudFormation

- 클라우드 인프라 리소스 모델링 및 프로비저닝 

- 대다수 AWS 서비스 지원 

  최신 기술이나 아직 업데이트 안된 문제 등 문서화 안될 수 있으나 대부분 가능합니다.

- 스택이라는 단일 단위로 리소스 세트 생성, 업데이트 및 삭제 

- 스택 및 개별 리소스에서 **드리프트**(draft)라고 하는 **변경 사항** 감지

- 스택 단위 별로 실행을 한다.

### AWS CloudFormation 용어

![image-20231101114654754](/../images/2023-11-01-coludFormation/image-20231101114654754.png)

템플릿을 S3에 올린다.

### 템플릿 구조

![image-20231101114800414](/../images/2023-11-01-coludFormation/image-20231101114800414.png)

Parameters: 템플릿에 입력 

Mappings: 정적 변수 - 일반적으로 최신 Amazon Machine Image(AMI) 

Resources: 생성할 AWS 자산 

Init: 시작 시 실행할 사용자 지정 애플리케이션 

​	WaitCondition: 사용자 데이터가 실행을 완료한 인스턴스의 신호 

Outputs: 템플릿이 생성하는 사용자 지정 리소스 값(URL, 사용자 이름 등)



### AWS CloudFormation 템플릿 편집

AWS CloudFormation과 호환되는 편집기(또는 JSON 또는 YAML 편집기)를 사용하여 **구문 분석 기능**, **자동 완성** 및 **구문 검사**와 같은 기능을 사용합니다.

![image-20231101115013472](../../images/2023-11-01-coludFormation/image-20231101115013472.png)

### 템플릿 디자인

AWS CloudFormation Designer는 끌어서 놓기 인터페이스를 사용해 AWS CloudFormation 템플릿을 생성 및 수정할 수 있게 하는 비주얼 도구입니다.

![image-20231101115102681](../../images/2023-11-01-coludFormation/image-20231101115102681.png)

### 스택 시작 및 삭제

- AWS CloudFormation 템플릿을 스택으로 시작 가능: – AWS Management Console – AWS CLI – AWS API 
- 템플릿을 시작할 때 오류가 발생하면 모든 리소스가 기본적으로 롤백됩니다. 
- 스택이 삭제되면 리소스가 롤백됩니다. – 선택적으로 스택에서 종료 방지 기능을 활성화할 수 있습니다.

### 템플릿에서 파라미터 정의

템플릿에서 파라미터를 정의하는 방법:

- 선택 사항인 Parameters 섹션을 사용하여 템플릿을 사용자 지정합니다. 
- 파라미터를 사용하면 스택을 생성하거나 업데이트할 때마다 템플릿에 사용자 지정 값을 입력할 수 있습니다.

![image-20231101115217611](/../images/2023-11-01-coludFormation/image-20231101115217611.png)

### 파라미터 참조

파라미터를 참조하는 방법:

- 파라미터를 참조하려면 Ref 내장 함수를 사용합니다. 

- 파라미터 선언의 형식과 관계없이 문자열로 변환됩니다.

  파라미터 `"KeyPairName": {"Type": "AWS::EC2::KeyPair::KeyName"}`

  파라미터 참조 `"KeyName": {"Ref": "KeyPairName"},`

- Fn::Select 함수를 사용하여 쉼표로 구분된 목록에서 값을 선택합니다.

`"AvailabilityZone" : { "Fn::Select" : [ "0", { "Ref" : "AvailableAZs" } ] }`

### Ref 및 기타 내장 함수

Ref 함수:

- AWS CloudFormation 템플릿에 정의된 참조 구성 요소를 활성화합니다. • 필요한 경우: – 파라미터 참조 – 맵 사용 – 문자열 조인 – 다른 함수 사용

{: .notice}

"MyEIP" : {<br/>&nbsp;&nbsp;&nbsp; "Type" : "AWS::EC2::EIP",<br/> &nbsp;&nbsp;&nbsp;"Properties" : {<br/>&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "InstanceId" : { "Ref" : "MyEC2Instance" } <br/>&nbsp;&nbsp;&nbsp; }<br/> } 

### 의사 파라미터

추가 사항:

- Ref 내장 함수를 사용하여 런타임 환경에 대한 정보에 액세스할 수 있습니다. 
  - 예: 리전, 스택 이름, AWS 계정 ID
- 의사 파라미터는 미리 정의되어 있으므로 템플릿의 Parameters 섹션에서 지정할 필요가 없습니다.

{: .notice}

"Outputs" { "MyStacksRegion" : {<br/> &nbsp;&nbsp;&nbsp;"Value" : { "Ref" : "AWS::Region" } }<br/> }

### 템플릿에서 매핑 정의

템플릿에서 매핑을 정의하는 방법:

- 2단계 맵에서 이름-값 페어의 조회 테이블을 정의합니다. 
- 여러 매핑 테이블을 결합하여 중첩되는 조회 결과를 생성합니다. 
- 현재 Amazon Machine Image(AMI) 값을 조회하는 데 가장 일반적으로 사용됩니다.

### 매핑 예제

![image-20231101123716992](/../images/2023-11-01-coludFormation/image-20231101123716992.png)

### 템플릿에서 리소스 정의

![image-20231101123736279](/../images/2023-11-01-coludFormation/image-20231101123736279.png)

### CloudFormation::Init

- EC2 인스턴스의 메타데이터에 대한 액세스를 제공하는 리소스 유형 • cfn-init 헬퍼 스크립트와 함께 사용할 수 있습니다. • cfn-init 헬퍼 스크립트: – AWS::CloudFormation::Init 키에서 템플릿 메타데이터를 읽습니다. – 이 정보를 사용하여 cfn-init는 EC2 인스턴스에서 다음 작업을 수행할 수 있습니다. » 패키지 설치 » 그룹 및 사용자 계정 관리 » 디스크에 파일 기록 » 명령 실행 » 서비스 활성화 또는 비활성화 » 서비스 시작 또는 중지

### 사용자 데이터 VS. CloudFormation::Init

AWS CloudFormation의 사용자 데이터:

- 파일 스크립팅(개별 인스턴스와 동일) 
- 향상된 제어 제공 
- 더 높은 오류 가능성 제공 보다 신중해야 함

CloudFormation::Init:

- 실패 시 자동으로 롤백할 수 있음
-  CloudFormation 템플릿의 사용자 데이터 필드보다 관리가 쉬움 
- 템플릿 내에서 메타데이터를 연결할 수 있음 
- Configset는 단일 CloudFormation::Init에서 여러 구성을 허용

### WaitCondition 및 WaitConditionHandle

WaitCondition 및 WaitConditionHandle은 인스턴스를 부트스트랩할 때 사용됩니다. 추가 사항:

- WaitCondition은 WaitConditionHandle이 호출되거나 시간 제한에 도달할 때까지 스택의 완료 상태를 차단합니다. 
  - WaitCondition이 충족되기 전에 수신되어야 하는 성공적인 신호의 수를 지정할 수 있습니다. 
  - 기본값: 1 
- cfn-signal 명령을 사용하여 성공 또는 실패 신호를 보낼 수 있습니다.

### WaitCondition 및 WaitConditionHandle

![image-20231101123917907](/../images/2023-11-01-coludFormation/image-20231101123917907.png)

### 템플릿에서 출력 정의

Outputs:

- 스택의 일부로 생성된 리소스에 대한 값을 반환합니다. 
- 내장 함수를 사용하여 스택의 리소스 값을 얻습니다.

![image-20231101123944508](/../images/2023-11-01-coludFormation/image-20231101123944508.png)

### 추가 AWS CloudFormation 스택 옵션

다음과 같은 AWS CloudFormation 스택을 생성할 때 추가 옵션을 지정할 수 있습니다.

- 실패 시 롤백 방지 
- 스택 정책을 설정하여 스택 업데이트 제어 
- 종료 방지 기능 활성화

{: .notice}

**aws cloudformation create-stack –-stack-name NewStack –-template-body file://path/to/template.yml –-on-failure DO_NOTHING**

### 실패한 업데이트 롤백 재정의

- 롤백이 실패하고 UPDATE_ROLLBACK_FAILED 상태에 있어도 스택에 대한 업데이트를 계속 롤백합니다. • 재정의 수행 – – 실패한 롤백의 원인을 해결합니다. – AWS CloudFormation에 업데이트 롤백을 계속하도록 지시합니다.

### 변경 세트

- 변경 세트에 구현 전에 스택에 제안된 변경 사항이 나타납니다. 
- AWS CloudFormation은 제출된 변경 사항을 스택과 비교합니다. 
- 엔지니어는 변경 사항을 보고 어떤 리소스가 추가, 수정 또는 삭제되는지 확인할 수 있습니다. 
- 그런 다음, 변경 세트를 스택에 적용하여 변경 사항을 구현할 수 있습니다

## 핵심 사항

- AWS CloudFormation을 사용하면 예측 가능하고 반복 가능한 방식으로 AWS 인프라 배포를 생성하고 프로비저닝할 수 있습니다. • AWS CloudFormation의 2가지 주요 용어는 템플릿과 스택입니다. • AWS CloudFormation 템플릿을 시작할 때 오류가 발생하면 모든 리소스가 기본적으로 롤백됩니다. • 파라미터를 통해 스택을 생성하거나 업데이트할 때마다 템플릿에 사용자 지정 값을 입력할 수 있습니다

## knowledge Check

1. **다음 중 AWS 리소스 스택을 나타내는 스크립트와 유사한 템플릿을 구축할 수 있는 Amazon Web Services(AWS) 서비스는 무엇입니까?**

   - [ ] AWS OpsWorks

   - [x] AWS CloudFormation

   - [ ] AWS CodeDeploy

   - [ ] Amazon CloudWatch 경보

2.  **다음 중 시스템 관리자가 구성 관리 솔루션을 이용하는 이유는 무엇입니까?**

   - [ ] Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스의 확장성을 높이기 위해

   - [ ] 예약된 시스템 백업을 실행하기 위해

   - [ ] 시스템에서 사용자 인증을 관리하기 위해

   - [x] 구성 작업을 자동화하고 반복 가능하게 만들기 위해

3.  **다음 중 AWS CloudFormation 템플릿에서 wait 조건의 목적은 무엇입니까?**

   - [x] 템플릿 리소스 생성을 다른 외부 구성 작업과 조율

   - [ ] 사용자 지정 입력값을 정의하고 초기화 대기

   - [ ] 출력값을 읽을 수 있을 때 알림

   - [ ] 파라미터의 유효성을 검사하고 오류가 없게 될 때까지 대기

4. **관리자가 AWS CloudFormation 템플릿을 Amazon Simple Storage Service(Amazon S3) 버킷에 저장하려고 하는데 오류가 발생했습니다. 다음 중 그 이유로 가능성이 높은 것은 무엇입니까?**

   - [ ] CloudFormation 템플릿은 YAML Ain’t Markup Language(YAML)가 아닌 JavaScript Object Notation(JSON)으로 작성됨

   - [ ] 버킷이 꽉 참

   - [x] 관리자가 버킷에 액세스하려면 권한이 필요

   - [ ] CloudFormation 템플릿에 구문 오류가 있음

5. **다음 중 Amazon Machine Image(AMI)에 대한 설명으로 옳은 것은 무엇입니까?**

   - [ ] AMI는 인스턴스가 실행된 후 인스턴스에 적용됨

   - [ ] AMI는 한 번에 한 인스턴스에만 사용됨

   - [ ] AMI는 복사할 수 없음

   - [x] AMI는 리전 수준에 고정됨