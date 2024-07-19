---
title: "[LG 유플러스] Servlet"
toc: true
toc_lable: "목차"
toc_stick: true 
---

### 서블릿<small>Servlet</small>

Java Application

<small>자바응용프로그램</small>  ⬅️ <span style="color:red">main() 포함</span>



일반적으로 get방식



### 서블릿 실행방법

1. \http://192.168.0.96:8080/TomTest/servlet/com/ureca.MyServlet

2. WEB-INF/web.xml에 작성된 서블릿 클래스를 등록

   ➡️ 등록과 함께 서블릿에 대한 가상의 경로를 매핑시켜 호출

3. @annotation으로 서블릿을 등록

   @WebServlet("path")<small>(Servlet에서)</small> ➡️ @RequestMapping("Path")<small>(Sping에서)</small>



Servlet/JSP의 수식어 ➡️ 웹어플리케이션<small>(웹서비스하는 프로그램)</small>

- Servlet 용도

  1. 브라우저에 출력할 화면구성
  2. Controller기능<small>(MVC 패턴 구조에서 사용)</small>

- JSP용도

  1. 브라우저에 출력할 화면 구성

     ➡️ HTML+Java<small>서버와 데이터 공유</small>

# JSP(Java Server Pages) 개요

- **Java Server Pages (JSP)**: 자바를 기반으로 한 서버 사이드 스크립트 언어로, 웹 애플리케이션을 개발하는 데 사용됩니다.
- **클라이언트 스크립트**: JavaScript (브라우저에서 실행)
- **서버 스크립트**: JSP (JVM에서 실행)

### 주요 특징
- **웹 애플리케이션 개발**: JSP는 브라우저에서 실행되는 웹 페이지를 개발하는 데 사용됩니다.
- **서블릿 컨테이너(Apache Tomcat)**: JSP 페이지는 서블릿 컨테이너를 통해 실행됩니다.
- **HTML + Java 코드**: JSP는 HTML 코드와 자바 코드를 혼합하여 사용합니다.

### 실행 절차
1. **JSP 페이지 요청**: `http://ip:port/컨텍스트루트/경로/hello.jsp`
2. **페이지 존재 여부 확인**: 페이지가 없으면 404 에러 발생
3. **서블릿 클래스 존재 여부 확인**: 없으면 생성
4. **컴파일 여부 확인**: 컴파일되지 않았으면 컴파일
5. **메모리 로딩 여부 확인**: 메모리에 로딩되지 않았으면 로딩
6. **init() 메소드 호출**: 최초 호출인 경우
7. **service() 메소드 호출**: 각 요청마다

### JSP 기본 태그
1. **Declaration (선언)**: `<%! ... %>`
    ```jsp
    <%!
        int su;
        int su2 = 20;

        public String getMsg() {
            return "건강하세요~!!";
        }
    %>
    ```

2. **Scriptlet (스크립트릿, 실행)**: `<% ... %>`
    ```jsp
    <%
        int su3;
        int su4 = 40;
        su = 10; // 멤버 초기화
        su3 = 30; // 지역 변수 초기화

        if (조건식) { }
        for (int i = 0; i < 3; i++) {
            System.out.println("안녕");
        }
    %>
    ```

3. **Expression (표현식, 출력식)**: `<%= ... %>`
    ```jsp
    <%= 2 + 3 %>              <!-- out.print(2 + 3); -->
    <%= "안녕" %>              <!-- out.print("안녕"); -->
    <%= su4 %>                <!-- out.print(su4); -->
    <%= getMsg() %>           <!-- out.print(getMsg()); -->
    ```

4. **Comment (주석)**: `<%-- ... --%>`
    ```jsp
    <%-- JSP 주석 --%>
    ```

### JSP 지시어 (Directives)
1. **page 지시어**: JSP 페이지의 속성을 정의
    ```jsp
    <%@ page contentType="text/html;charset=UTF-8" %>
    <%@ page import="java.util.ArrayList, java.util.Calendar" %>
    ```

2. **include 지시어**: 다른 페이지를 포함
    ```jsp
    <%@ include file="경로명" %>
    ```

3. **taglib 지시어**: 외부 태그 라이브러리를 사용할 때
    ```jsp
    <%@ taglib uri="경로" prefix="접두사" %>
    ```

### JSP 기본 객체 (내장 객체)
1. **request**: 사용자 입력 정보 처리 (`javax.servlet.http.HttpServletRequest`)
    ```jsp
    request.getParameter("name");
    ```

2. **response**: 응답을 처리 (`java.servlet.http.HttpServletResponse`)
    ```jsp
    response.sendRedirect("이동경로");
    ```

3. **session**: 클라이언트 세션 정보 처리 (`javax.servlet.http.HttpSession`)
    ```jsp
    session.setAttribute("name", value);
    ```

4. **application**: 애플리케이션 관련 정보 처리 (`javax.servlet.ServletContext`)
    ```jsp
    application.getAttribute("name");
    ```

5. **pageContext**: 현재 페이지 관련 정보 (`javax.servlet.jsp.PageContext`)
    ```jsp
    pageContext.getRequest();
    ```

6. **out**: 브라우저 출력 객체 (`javax.servlet.jsp.JspWriter`)
    ```jsp
    out.print("안녕");
    ```

7. **config**: 현재 JSP의 초기화 환경 (`javax.servlet.ServletConfig`)
8. **page**: 현재 JSP 페이지 클래스 (`java.lang.Object`)
9. ** &#8203;:citation[oaicite:0]{index=0}&#8203;

# JSP(Java Server Pages) 개요
- **Java Server Pages (JSP)**: 자바를 기반으로 한 서버 사이드 스크립트 언어로, 웹 애플리케이션을 개발하는 데 사용됩니다.
- **클라이언트 스크립트**: JavaScript (브라우저에서 실행)
- **서버 스크립트**: JSP (JVM에서 실행)

### 주요 특징
- **웹 애플리케이션 개발**: JSP는 브라우저에서 실행되는 웹 페이지를 개발하는 데 사용됩니다.
- **서블릿 컨테이너(Apache Tomcat)**: JSP 페이지는 서블릿 컨테이너를 통해 실행됩니다.
- **HTML + Java 코드**: JSP는 HTML 코드와 자바 코드를 혼합하여 사용합니다.

### 실행 절차
1. **JSP 페이지 요청**: `http://ip:port/컨텍스트루트/경로/hello.jsp`
2. **페이지 존재 여부 확인**: 페이지가 없으면 404 에러 발생
3. **서블릿 클래스 존재 여부 확인**: 없으면 생성
4. **컴파일 여부 확인**: 컴파일되지 않았으면 컴파일
5. **메모리 로딩 여부 확인**: 메모리에 로딩되지 않았으면 로딩
6. **init() 메소드 호출**: 최초 호출인 경우
7. **service() 메소드 호출**: 각 요청마다

### JSP 기본 태그
1. **Declaration (선언)**: `<%! ... %>`
    ```jsp
    <%! 
        int su; 
        int su2 = 20; 
        public String getMsg() { 
            return "건강하세요~!!"; 
        } 
    %>
    ```

2. **Scriptlet (스크립트릿, 실행)**: `<% ... %>`
    ```jsp
    <%
        int su3;
        int su4 = 40;
        su = 10; // 멤버 초기화
        su3 = 30; // 지역 변수 초기화

        if (조건식) { }
        for (int i = 0; i < 3; i++) {
            System.out.println("안녕");
        }
    %>
    ```

3. **Expression (표현식, 출력식)**: `<%= ... %>`
    ```jsp
    <%= 2 + 3 %>              <!-- out.print(2 + 3); -->
    <%= "안녕" %>              <!-- out.print("안녕"); -->
    <%= su4 %>                <!-- out.print(su4); -->
    <%= getMsg() %>           <!-- out.print(getMsg()); -->
    ```

4. **Comment (주석)**: `<%-- ... --%>`
    ```jsp
    <%-- JSP 주석 --%>
    ```

### JSP 지시어 (Directives)
1. **page 지시어**: JSP 페이지의 속성을 정의
    ```jsp
    <%@ page contentType="text/html;charset=UTF-8" %>
    <%@ page import="java.util.ArrayList, java.util.Calendar" %>
    ```

2. **include 지시어**: 다른 페이지를 포함
    ```jsp
    <%@ include file="경로명" %>
    ```

3. **taglib 지시어**: 외부 태그 라이브러리를 사용할 때
    ```jsp
    <%@ taglib uri="경로" prefix="접두사" %>
    ```

### JSP 기본 객체 (내장 객체)
1. **request**: 사용자 입력 정보 처리 (`javax.servlet.http.HttpServletRequest`)
    ```jsp
    request.getParameter("name");
    ```

2. **response**: 응답을 처리 (`java.servlet.http.HttpServletResponse`)
    ```jsp
    response.sendRedirect("이동경로");
    ```

3. **session**: 클라이언트 세션 정보 처리 (`javax.servlet.http.HttpSession`)
    ```jsp
    session.setAttribute("name", value);
    ```

4. **application**: 애플리케이션 관련 정보 처리 (`javax.servlet.ServletContext`)
    ```jsp
    application.getAttribute("name");
    ```

5. **pageContext**: 현재 페이지 관련 정보 (`javax.servlet.jsp.PageContext`)
    ```jsp
    pageContext.getRequest();
    ```

6. **out**: 브라우저 출력 객체 (`javax.servlet.jsp.JspWriter`)
    ```jsp
    out.print("안녕");
    ```

7. **config**: 현재 JSP의 초기화 환경 (`javax.servlet.ServletConfig`)
8. **page**: 현재 JSP 페이지 클래스 (`java.lang.Object`)
9. **exception**: 예외 처리 (`java.lang.Throwable`)

### JSP 액션 태그
1. **include**: 다른 페이지를 포함
    ```jsp
    <jsp:include page="포함될 페이지 경로" />
    ```

2. **forward**: 페이지 이동
    ```jsp
    <jsp:forward page="이동할 페이지 경로" />
    ```

3. **useBean**: 클래스 객체 생성 및 사용
    ```jsp
    <jsp:useBean id="obj" class="pack.A" scope="page" />
    ```

4. **setProperty**: 빈의 속성 설정
    ```jsp
    <jsp:setProperty name="obj" property="속성명" value="데이터" />
    ```

5. **getProperty**: 빈의 속성 가져오기
    ```jsp
    <jsp:getProperty name="obj" property="속성명" />
    ```

### 표현 언어 (Expression Language, EL)
- **표현 언어 기본 문법**
    ```jsp
    ${param.name}
    ${sessionScope.user}
    ${cookie.username.value}
    ```

- **예제**
    ```jsp
    <%
        String name = request.getParameter("username");
    %>
    사용자 이름: ${param.username}
    ```

### JSTL (JSP Standard Tag Library)
1. **코어 태그** (`http://java.sun.com/jsp/jstl/core`)
    - 변수 지원: `<c:set>`, `<c:remove>`
    - 흐름 제어: `<c:if>`, `<c:choose>`, `<c:forEach>`, `<c:forTokens>`
    - URL 처리: `<c:import>`, `<c:redirect>`, `<c:url>`

2. **XML 태그** (`http://java.sun.com/jsp/jstl/xml`)
3. **국제화 태그** (`http://java.sun.com/jsp/jstl/fmt`)
4. **데이터베이스 태그** (`http://java.sun.com/jsp/jstl/sql`)
5. **함수 태그** (`http://java.sun.com/jsp/jstl/functions`)

### 문제 및 예제
1. **조회수 출력**: count.jsp
    ```jsp
    <%
        Integer count = (Integer) application.getAttribute("count");
        if (count == null) {
            count = 1;
        } else {
            count++;
        }
        application.setAttribute("count", count);
    %>
    조회수: <%= count %>회
    ```

2. **로그인 폼 데이터 출력**: param_test.jsp
    ```jsp
    <%
        String id = request.getParameter("id");
        String pwd = request.getParameter("pwd");
    %>
    전달 아이디: <%= id %>
    전달 비번: <%= pwd %>
    ```

3. **계산기**: calc.jsp & result.jsp
    - calc.jsp:
    ```html
    <form action="result.jsp">
        <input type="text" name="su1">
        <select name="oper">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/option>
        </select>
        <input type="text" name="su2">
        <input type="submit" value="계산">
    </form>
    ```

    - result.jsp:
    ```jsp
    <%
        try {
            int su1 = Integer.parseInt(request.getParameter("su1"));
            String oper = request.getParameter("oper");
            int su2 = Integer.parseInt(request.getParameter("su2"));
            int result = 0;
            switch (oper) {
                case "+": result = su1 + su2; break;
                case "-": result = su1 - su2; break;
                case "*": result = su1 * su2; break;
                case "/": result = su1 / su2; break;
            }
            out.println("결과값: " + su1 + " " + oper + " " + su2 + " = " + result);
        } catch (Exception e) {
            out.println("잘못된 입력입니다.");
        }
    %>
    ```

### 구구단 출력: gugudan.jsp
```jsp
<table border="1">
    <%
        for (int i = 1; i <= 9; i++) {
            out.print("<tr>");
            for (int j = 2; j <= 9; j++) {
                out.print("<td>" + j + " * " + i + " = &#8203;:citation[oaicite:0]{index=0}&#8203;
```