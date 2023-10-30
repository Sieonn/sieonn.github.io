---
title: "Amazon Elastic Block Store(Amazon EBS)"
---



### AWS 스토리지 서비스

사진

### 블록 수준 스토리지와 객체 수준 스토리지 비교

- **블록 스토리지**

  해당 문자가 포함된 블록 하나(파일 일부)를 변경함

- **객체 스토리지**

  전체 파일을 업데이트해야 함

- **차이점**

  이 차이점은 스토리지 솔루션의 처리량, 대기 시간 및 비용에 큰 영향을 미칩니다. 



## Amazon Elastic Block Store(Amazon EBS)

### Amazon EBS란 무엇입니까?

- Amazon EBS는 **영구적인 블록 스토리지 볼륨을 제공**합니다. 

- 각 EBS 볼륨은 <span class="hlm">**가용 영역 내에서 자동으로 복제**</span>됩니다.  

  {: .notice}

  **다른 존과는 연결 할 수 없습니다.** 내가 생성한 볼륨이 인스턴스와 존이 다르면 접근 할 수 없습니다. 다른 존에서 사용하려면 미러링을 해야합니다.

- Amazon EBS를 사용하면 **몇 분 내에 사용량을 늘리거나 줄일 수 있습니다.**

  

  

### Amazon EBS

**Amazon EBS는 블록 수준 스토리지를 제공합니다.**

Amazon EBS를 사용하여 개별 스토리지 볼륨을 생성하고 Amazon EC2 인스턴스에 연결할 수 있습니다. • 

- 볼륨은 가용 영역 내에서 자동으로 복제됩니다. • 
- 볼륨은 Amazon S3로 자동 백업될 수 있습니다. • 
- 용도: 
  - – Amazon EC2 인스턴스용 부트 볼륨 및 스토리지 – 
  - 파일 시스템 내 데이터 스토리지 – 
  - 데이터베이스 호스트 – 엔터프라이즈 애플리케이션

스냅샷, 암호화, 탄력성 

- 스냅샷:
  - 특정 시점 스냅샷 • 
  - 언제든지 새 볼륨을 다시 생성 
- 암호화: • 
  - 암호화된 EBS 볼륨 • 
  - 추가 비용 없음 
- 탄력성: • 
  - 용량 증가 • 
  - 다른 유형으로 변경

### Amazon EBS: 비용

스냅샷 및 데이터 전송 

- 스냅샷 • 
  - Amazon S3에 Amazon EBS 스냅샷을 추가하는 비용은 저장되는 데이터의 월별 GB 단위로 계산됩니다.

## EBS 볼륨 유형

### Amazon EBS - 볼륨 및 IOPS

볼륨 • 

- 볼륨은 인스턴스와 별개로 유지됩니다. • 
- 모든 볼륨 유형은 월별 프로비저닝된 양을 기준으로 요금이 부과됩니다.

초당 입출력 작업 수(IOPS) • 

- 범용(SSD) – 
  - 스토리지가 해제될 때까지 월별 프로비저닝한 양(GB 단위)을 기준으로 요금이 부과됩니다. • 
- 마그네틱 – 
  - 볼륨에 대한 요청 수를 기준으로 요금이 부과됩니다. • 
- 프로비저닝된 IOPS(SSD) – 
  - 프로비저닝한 양의 IOPS를 기준으로 요금이 부과됩니다(사용한 일수 또는 개월 수의 비율로).

### Amazon EBS 볼륨 유형

<style type="text/css"><center>
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 1em;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:12px;
  font-weight:normal;overflow:hidden;padding:7px 1em;word-break:normal;}
.tg .tg-oiir{background-color:#8e8ffa;border-color:#fff;font-family:inherit;font-size:14px;font-weight:bold;text-align:center;
  vertical-align:top}
.tg .tg-rdv1{border-color:#c1bebe;color:$dark-gray;font-family:inherit;font-size:12px;text-align:center;vertical-align:top}
    .tg .tg-y9zo{background-color:#8e8ffa;border-color:#fff;font-family:inherit;font-size:14px;text-align:center;vertical-align:top}</center>
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-y9zo" rowspan="2"></th>
    <th class="tg-oiir" colspan="2">솔리드 스테이트 드라이브(SSD)</th>
    <th class="tg-oiir" colspan="2">하드 디스크 드라이브(HDD)</th>
  </tr>
  <tr>
    <th class="tg-y9zo">범용</th>
    <th class="tg-y9zo">프로비저닝된 IOPS</th>
    <th class="tg-y9zo">처리량 최적화</th>
    <th class="tg-y9zo">콜드</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-rdv1">최대 볼륨 크기</td>
    <td class="tg-rdv1">16테비바이트(TiB)</td>
    <td class="tg-rdv1">16TiB</td>
    <td class="tg-rdv1">16TiB</td>
    <td class="tg-rdv1">16TiB</td>
  </tr>
  <tr>
    <td class="tg-rdv1">볼륨당 최대 IOPS</td>
    <td class="tg-rdv1">10,000</td>
    <td class="tg-rdv1">32,000</td>
    <td class="tg-rdv1">500</td>
    <td class="tg-rdv1">250</td>
  </tr>
  <tr>
    <td class="tg-rdv1">볼륨당 최대 처리량 </td>
    <td class="tg-rdv1">초당 160메비바이트(MiB/s)</td>
    <td class="tg-rdv1">500MiB/s</td>
    <td class="tg-rdv1">500MiB/s</td>
    <td class="tg-rdv1">250MiB/s</td>
  </tr>
</tbody>
</table>

## EBS 볼륨 유형의 용례

### EBS 볼륨: 용례

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:9px 10px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:9px 10px;word-break:normal;}
.tg .tg-9t5p{background-color:#8e8ffa;border-color:#ffffff;color:#ffffff;font-family:inherit;font-size:14px;font-weight:bold;
  text-align:center;vertical-align:middle}
.tg .tg-sdct{background-color:#8E8FFA;border-color:#ffffff;color:#ffffff;font-family:inherit;font-size:14px;font-weight:nomal;
  text-align:center;vertical-align:middle}
.tg .tg-67p5{border-color:#c1bebe;color:$dark-gray;font-family:inherit;font-size:12px;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-9t5p" colspan="2">솔리드 스테이트 드라이브(SSD)</th>
    <th class="tg-9t5p" colspan="2">하드 디스크 드라이브(HDD)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-sdct">범용</td>
    <td class="tg-sdct">프로비저닝된 IOPS</td>
    <td class="tg-sdct">처리량 최적화</td>
    <td class="tg-9t5p">콜드</td>
  </tr>
  <tr>
    <td class="tg-67p5">- 대부분의 워크로드에 권장됨<br>- 시스템 부트 볼륨<br>- 기상 데스크톱<br>- 대기 시간이 짧은 대화형 앱<br>- 개발 및 테스트 환경</td>
    <td class="tg-67p5">- I/O 집약적 워크로드<br>- 관계형 데이터베이스<br>- NoSQL 데이터베이스</td>
    <td class="tg-67p5">- 저렴한 가격에 일관되고 빠른 처리량이 <br>&nbsp;&nbsp;요구되는 스트리밍 워크로드<br>- 빅 데이터<br>- 데이터 웨어하우스<br>- 로그처리<br>- 부트 볼륨이 될 수 없음</td>
    <td class="tg-67p5">- 자주 액세스하지 않는 대량의 데이터 <br>&nbsp;&nbsp;볼륨을 처리량 중심으로 저장<br>- 스토리지 비용이 최대한 낮아야지 하는 시나리오<br>- 부트 볼륨이 될 수 없음</td>
  </tr>
</tbody>
</table>

