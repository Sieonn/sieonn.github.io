---
title: "Amazon CloudFront"
toc: true
toc_sticky: true
toc_label: "Amazon CloudFront"
---

## Amazon CloudFront

### Amazon CloudFront란?

- Amazon CloudFront는 정적 및 동적 웹 콘텐츠(예: .html, .css, .js 및 이미지 파일)를 사용자에게 더 빨리 배포하도록 지원하는 웹 서비스입 니다.
- Amazon CloudFront는 엣지 로케이션이라고 하는 데이터 센터의 전 세계 네트워크를 통해 콘텐츠를 제공합니다

Amazon CloudFront는 뛰어난 성능, 보안 및 개발자 편의를 위해 구축된 콘텐츠 전송 네트워크 서비스(CDN)입니다.

캐싱을 통해 사용자에게 좀 더 빠른 전송 속도를 제공함을 목적으로합니다. CloudFront는 전 세계 Edge server(Location)을 두고 Client에 가장 가까운 Edge Server를 찾아 대기(지연) 시간(Latency)를 최소화 시켜 빠른 데이터를 제공합니다.



- Amazon CloudFront는 정적 및 동적 웹 콘텐츠를 사용자에게 더 빨리 배포하도록 지원하는 웹 서비스 입니다.

  {: .notice}

  웹 콘텐츠 예 -  html, css, .js 및 이미지 파일

- Amazon CloudFront는 **엣지 로케이션**이라고 하는 데이터 센터의 전 세계  네트워크를 통해 콘텐츠를 제공합니다.

![다운로드](/../images/2023-10-19-Amazon CloudFront/다운로드.png)

Origin Server: 원본 데이터를 가지고 있는 서버입니다. 보통 AWS Origin Server는 S3, EC2 instance입니다.

Edge Server(= Edge Location): AWS 에서 실질적으로 제공하는 전 세계에 퍼져있는 서버입니다. Edge Server에는 요청 받은 데이터에 대해서 **빠르게 응답**해주기 위해 **Cache 기능을 제공** 합니다.

### Edge Server의 Cache는 무슨 특징이 있나요?

\- 기본적으로 한번 발생한 요청에 대해서는 Edge Server에 캐싱된 상태로 저장됩니다.

 

\- Edge Server의 기본 TTL은 24시간이고 사용자의 설정에 따라 변경이 가능합니다. (TTL 수정 시 Edge Server에 반영되는 시간이 한 시간 가량 소요됩니다.)

 

\- 이러한 캐시의 설정 후 반영 시간 때문에 전체 데이터에 대한 TTL을 수정하는 게 아닌 각 개별 데이터에 대해서 invalidation API(특정 파일을 캐시에서 삭제하는 기능)을 통해 삭제할 수 있습니다.

 

\- Invalidation API는 동시에 최대 3개의 요청을 발생시킬 수 있으며, 각 요청은 최대 1000개까지 가능합니다.

 

\- Invalidation API는 Edge Node에 반영되기까지 5~10분 정도의 시간이 소요됩니다.

### 엣지 로케이션 및 리전 엣지 캐시

![image-20231019150318136](/../images/2023-10-19-Amazon CloudFront/image-20231019150318136.png)

### Amazon CloudFront: 주요 기능

- **고성능:** 
  -  짧은 대기 시간  
  - 빠른 데이터 전송 속도  
- **비용 효율적:**  
  - 고객에게 콘텐츠를 전송하는 데 사용한 데이터 전송 및 요청에 대한 요금 지불  
  - 최소 약정 또는 선결제 없음  
- **다른 AWS 서비스와 연동**

### Amazon CloudFront: 비용 예측

트래픽 분산:  

- 요금제는 지리적 리전에 따라 다름  
- 엣지 로케이션 기반 

요청:  

- 요청의 수 및 유형  
- 지리적 리전 

데이터 전송:  

- Amazon CloudFront 엣지 로케이션에서 전송된 데이터의 양

## 핵심 사항

- CloudFront는 엣지 로케이션을 사용하여 가용성, 확장성, 성능이 뛰어난 방식으로 콘텐츠를 안전하게 전송하는 **콘텐츠 전송 네트워크(CDN)** 서비스입니다.  
- CloudFront는 **다른 AWS 서비스와 연동**하여 최소 약정 없이 짧은 대기 시간과 빠른 데이터 전송 속도로 사용자에게 콘텐츠를 배포할 수 있습니다. 
-  CloudFront 비용은 **지리적 리전, 요청의 수 및 유형, 전송된 데이터 양**을 기준으로 계산됩니다. 







