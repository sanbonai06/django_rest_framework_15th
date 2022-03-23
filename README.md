# CEOS 15기 백엔드 스터디 모델링 및 drf 연습을 위한 레포

## 도커란? 

* 도커는 컨테이너 기반의 오픈소스 가상화 플랫폼이다.

다양한 프로그램, 실행환경(백엔드 프로그램, DB서버, 메시지 큐 등)을 컨테이너로 추상화하고 동일한 인터페이스를 제공 => 프로그램의 배포 및 관리를 단순하게 만들어준다.

* 컨테이너: 가상화 기술의 한 종류로 격리된 공간에서 프로세스가 동작하는 기술

### 가상화 방식의 변화

> OS를 가상화: 가상머신을 이용하여 호스트 OS위에 게스트 OS를 띄우는 방식 => 사용법은 간단하지만 무겁고 느림 


## 도커의 원리

EC2에서 서버를 만들면 Ubuntu OS로 인스턴스가 생성되지만 내부에는 프로그래머가 로컬에서 작업하는데 필요한 여러 환경들 (Ex. python, git, 여러 라이브러리 파일들)이 존재하지 않는다.
또 로컬환경과 배포환경이 다른 경우에도 여러가지 문제가 발생 할 수 있다.

=> 이러한 문제점들을 Docker가 해결해줌.

* Docker는 어떤 OS에서도 같은 환경을 만들어줌.


