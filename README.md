# MobileSmartSystem
## 라즈베리파이를 이용한 주차 후방카메라 제안서

<h4>1. 작품개요</h4>
평소 자동차를 좋아해서 어떤 프로젝트를 해볼까 고민하다가 실제 차량에 들어가는 옵션인 후방카메라를 구현해보고 싶어서 선택했습니다. 차의 후방에 라즈베리와 카메라, 초음파센서 등을 연결하고 차가 후진기어를 넣고 장애물에 설정한 값보다 가까워지면 led에 불이 들어온다. 그리고 실시간으로 차가 후진하는 모습이 컴퓨터로 출력되고 실제 차량에 들어가는 옵션에 가깝게 하기위해서 구역도 나눠서 안전거리 또한 구현했습니다

![image](https://github.com/JungHanLeee/MobileSmartSystem/assets/89134202/36bc4db8-ccd4-4be6-92cd-31198f47e264)

<h4>2. 구현 방법</h4>
<h5>2.1 하드웨어 부분</h5>
카메라, 초음파센서, led
초음파 Echo – GPIO 16
       Trig – GPIO 20
	LED – GPIO 6

<h5>2.2 소프트웨어 부분</h5>
윈도우에서 실행하는 viewer.py
라즈베리파이에서 실행하는 gpio.py
장치와 센서를 제어하는 controller.py

<h4>실행 과정 및 결과</h4>
후진기어를 화면상에 위치한 버튼으로 가정하겠습니다.

![image](https://github.com/JungHanLeee/MobileSmartSystem/assets/89134202/da81fd3e-4e33-4afb-83c7-1cb873c6cd38)

후진기어로 변속했을 때 카메라와 초음파 센서가 켜집니다.

![image](https://github.com/JungHanLeee/MobileSmartSystem/assets/89134202/5168aaf5-e96f-4d69-9408-4c4d2fc9f124)

물체가 설정 값 보다 가까워졌을 때 불빛이 점멸합니다.

![image](https://github.com/JungHanLeee/MobileSmartSystem/assets/89134202/8f24b027-922a-40e2-886c-9e1e9f4e4034)

후진기어 버튼을 다시 누르면 카메라와 초음파 센서 작동이 멈춤니다.

<h5>결론</h5>
하드웨어와 소프트웨어를 종합적으로 배울 수 있어서 좋았다 다음에는 또 기회가 온다면 더욱 발전시켜 어라운드뷰로 하고 싶다.
