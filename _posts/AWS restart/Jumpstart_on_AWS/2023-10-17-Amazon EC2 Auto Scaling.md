---
title: "Amazon EC2 Auto Scaling"
toc_label: "Amazon EC2 Auto Scaling"
toc: true
toc_sticky: true
---

## Amazon EC2 Auto Scaling

### Amazon EC2 Auto Scaling

- 다음을 기반으로 Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스를 자동으로 시작하거나 종료합니다. 
  - 상태 확인 
  - Amazon CloudWatch에서 지원하는 사용자 정의 정책 
  - 일정 
  - 그 외 기준(예: 프로그래밍 방식) 
  - 설정한 원하는 용량을 수동으로 사용  
- 수요에 맞춰 확장하고 비용을 절감하도록 축소

### Amazon EC2 Auto Scaling 실행

![image-20231017171058238](/../images/2023-10-17-Amazon EC2 Auto Scaling/image-20231017171058238.png)

최소는 스케일 인의 바운더리 최대는 스케일 아웃의 바운더리입니다.

시작 템플렛

- Amazon Machine Image(AMI)  
- 인스턴스 유형  
- VPC  
- 보안 그룹  
- 스토리지  
- 인스턴스 키 페어  
- IAM 역할 
- 사용자 데이터  
- 태깅

![image-20231017171223152](/../images/2023-10-17-Amazon EC2 Auto Scaling/image-20231017171223152.png)

**Amazon EC2 Auto Scaling 그룹**

EC2 인스턴스의 논리적 그룹 

다음 범위에서 자동으로 조정 

- 최소  
- 원하는 값(선택 사항)  
- 최대 

Elastic Load Balancing과 통합(선택 사항) 

그룹 크기를 유지하기 위한 상태 확인 

인스턴스를 여러 가용 영역에 분산 및 밸런싱