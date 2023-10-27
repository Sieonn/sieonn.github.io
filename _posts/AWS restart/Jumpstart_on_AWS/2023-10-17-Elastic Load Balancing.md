---
title: "Elastic Load Balancing"
toc: ture
toc_label: "Elastic Load Balancing"
toc_sticky: true
---

## Elastic Load Balancing

### 로드 밸런서란 무엇입니까?

- Amazon Elastic Compare Cloud 인스턴스, 컨테이너, 인터넷 프로토콜 주소 등 여러 대상에 수진 애플리케이션 트래픽을 자동으로 분산시킵니다.

![image-20231017124517012](/../images/2023-10-17-Elastic Load Balancing/image-20231017124517012.png)

### ELB 로드 밸런서

![image-20231017124534615](/../images/2023-10-17-Elastic Load Balancing/image-20231017124534615.png)

![image-20231017124553449](/../images/2023-10-17-Elastic Load Balancing/image-20231017124553449.png)

L7이 ALB

L4 이 MLB

## 로드 밸런서 용례

### 용례

- 보안

  단일 지점을 통해 액세스

- 분리

  애플리케이션 환경 분리

- 내결함성

  고가용성 및 내 결함성 제공

- 확장성

  탄력성 및 확장성 증가

### Classic Load Balancer

용례 

- 단일 지점을 통해 서버에 액세스 
- 애플리케이션 환경 분리 
- 고가용성 및 내결함성 제공 
- 탄력성 및 확장성 증가

![image-20231017144128142](/../images/2023-10-17-Elastic Load Balancing/image-20231017144128142.png)

![image-20231017144144957](/../images/2023-10-17-Elastic Load Balancing/image-20231017144144957.png)

### Network Load Balancer

용례 

- 갑작스럽고 변동이 심한 트래픽 패턴 
- 가용 영역당 단일 고정 IP 주소 
- 최고의 성능을 필요로 하는 애플리케이션에 적합
- HTTP 응답 보기 
- 정상 및 비정상 호스트의 수 참조 
- 가용 영역 또는 로드 밸런서를 기준으로 지표 필터링

## 학습 내용 확인

1. 어떤 ELB 로드 밸런서가 웹사이트에 적합합니까?
2. 새 애플리케이션에 대한 트래픽을 처리하려면 로드 밸런서를 선택해야 합니다. 애플리케이션은 잠재적으로 초당 수십만 개의 요청을 수신할 수 있습니다. 요청이 갑자기 급증하기도 합니다.  Network Load Balancer가 좋은 선택인 이유는 무엇입니까?

## 핵심 사항

- ELB는 로드 밸런싱 서비스입니다. 
- 로드 밸런서는 자동으로 수신 트래픽 로드를 분산합니다.  
- ELB는 다음 3가지 유형의 로드 밸런서를 제공합니다.  
  - Application Load Balancer  
  - Network Load Balancer  
  - Classic Load Balancer 
- ELB는 여러 모니터링 도구를 제공합니다