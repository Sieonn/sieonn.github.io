---
title: "[PHOBUM](1) - Intellij 개발환경 설정"
toc: true
toc_label: "목차"
toc_sticky: true
---

## 프로젝트 기본 설정

저번 시간에 백엔드 기본 세팅을 해봤습니다.

그런데 익숙하지 않은 IDE에 많이 헤매면서 제대로  생성되지 않았기 때문에 다시 천천히 세팅해보고자 합니다.

[https://congsong.tistory.com/12?category=749196](https://congsong.tistory.com/12?category=749196) 이 분의 블로그 글을 보면서 따라합니다.



---

[open JDK  다운로드](https://github.com/ojdkbuild/ojdkbuild)를 해줍니다.

버전은 17 버전으로 다운 받을 겁니다.

<img src="/../images/2025-01-31-springboot_gradle/image-20250131205303764.png" alt="image-20250131205303764" style="zoom:67%;" />



### 폴더 생성

다운 받은 후에 폴더를 세팅합니다.

C드라이브 아래 `develop`폴더를 생성하고 `jdk`와 `workspace`폴더를 만들어줍니다.

<img src="/../images/2025-01-31-springboot_gradle/image-20250131205449227.png" alt="image-20250131205449227" style="zoom:67%;" />



그리고 `jdk`폴더에서 다운로드 받은 jdk의 압축을 풀어줍니다. 이때 압축을 해제하고 나서 폴더명을 `ojdk-17`로 변경합니다.

<img src="/../images/2025-01-31-springboot_gradle/image-20250131205727860.png" alt="image-20250131205727860" style="zoom:67%;" />



이제 윈도우에서 Java가 정상적으로 작동할 수 있게 환경 변수를 설정합니다.

<img src="/../images/2025-01-31-springboot_gradle/image-20250131205837098.png" alt="image-20250131205837098" style="zoom:67%;" />

<img src="/../images/2025-01-31-springboot_gradle/image-20250131205925505.png" alt="image-20250131205925505" style="zoom:67%;" />

새 시스템 변수를 생성해줍니다.



그 다음에 시스템 변수의 Path를 선택하여 편집을 누르고 새로만들기를 눌러서 `%JAVA_HOME%\bin`을 입력합니다.



그리고 새로 생성한 것을 최상단으로 올립니다.



이런 새 시스템변수도 만들어줍니다.

<img src="/../images/2025-01-31-springboot_gradle/image-20250131210716974.png" alt="image-20250131210716974" style="zoom:67%;" />



그다음 명령 프롬프트에 들어가서 `java`를 입력했을 때

<img src="/../images/2025-01-31-springboot_gradle/image-20250131210802496.png" alt="image-20250131210802496" style="zoom:67%;" />

이런 식으로 나오면 성공입니다.



### 스프링 부트 프로젝트 생성

스프링 이니셜라이저에 접속해서 [spring Boot 프로젝트 생성](https://start.spring.io/)을 해줍니다.

인텔리제이 Ultimate 버전은 IDE 내에서 스프링부트 프로젝트를 생성할 수 있지만 Community 버전은 인텔리제이 이니셜라이저에서 직접 생성해야합니다.

<img src="/../images/2025-01-31-springboot_gradle/image-20250131202035379.png" alt="image-20250131202035379" style="zoom:67%;" />



<img src="/../images/2025-01-31-springboot_gradle/image-20250131211356027.png" alt="image-20250131211356027" style="zoom:67%;" />

MyBatis설정하느라 고생을 많이 했기 때문에 이번에는 미리 추가해주고 시작합니다. 

로그인, 회원가입 기능을 넣어야하기 때문에 Security도 넣어주었습니다.



그리고 아까 만들었던 `workspace`폴더에 생성한 프로젝트를 압축해제 합니다.



인텔리제이에서 Project Open을 하는데 아까 프로젝트 위치를 Open 합니다.

<img src="/../images/2025-01-31-springboot_gradle/image-20250131211708463.png" alt="image-20250131211708463" style="zoom:67%;" />



<img src="/../images/2025-01-31-springboot_gradle/image-20250131211745786.png" alt="image-20250131211745786" style="zoom:70%;" />





## 인텔리제이 자바 설정

<img src="/../images/2025-01-31-springboot_gradle/image-20250131202331155.png" alt="image-20250131202331155" style="zoom:67%;" />

`File` > `Project Structure`

여기서 Project 탭에서 SDK를 원하는 버전으로 변경해줍니다.



<img src="/../images/2025-01-31-springboot_gradle/image-20250131202409884.png" alt="image-20250131202409884" style="zoom:67%;" />



<img src="/../images/2025-01-31-springboot_gradle/image-20250131202554040.png" alt="image-20250131202554040" style="zoom:67%;" />

왼쪽 메뉴에서 `SDKs`를 눌러서 JDK가 동일한지 확인 하고  같은 것으로 바꿔줍니다.



<img src="/../images/2025-01-31-springboot_gradle/image-20250131202629252.png" alt="image-20250131202629252" style="zoom:67%;" />

<img src="/../images/2025-01-31-springboot_gradle/image-20250131202719898.png" alt="image-20250131202719898" style="zoom:67%;" />



**Gradle 설치**

[여기](https://gradle.org/releases/)에서 원하는 버전을 다운로드 합니다.

![image-20250131203022712](../../images/2025-01-31-springboot_gradle/image-20250131203022712.png)

binary-only 또는 complete를 선택해서 다운받습니다.



<img src="/../images/2025-01-31-springboot_gradle/image-20250131203153009.png" alt="image-20250131203153009" style="zoom:67%;" />

`C:\gradle\`을 만들고 다운로드 받은 gradle 파일의 압축을 해제합니다.

<img src="/../images/2025-01-31-springboot_gradle/image-20250131203512464.png" alt="image-20250131203512464" style="zoom:67%;" />



시스템 환경 변수 편집 > 환경 변수 > Path 선택 후 편집 > 새로 만들기 > 찾아보기 > gradle 폴더의 bin 위치 선택

<img src="/../images/2025-01-31-springboot_gradle/image-20250131203607244.png" alt="image-20250131203607244" style="zoom:67%;" />

<img src="/../images/2025-01-31-springboot_gradle/image-20250131203644825.png" alt="image-20250131203644825" style="zoom:67%;" />



**설치확인**

CMD 창에서 `gradle -v`으로 설치 되어있는지 확인합니다.

<img src="/../images/2025-01-31-springboot_gradle/image-20250131203914493.png" alt="image-20250131203914493" style="zoom:67%;" />



이제 gradle이 정상적으로 설치가완료 되었습니다.