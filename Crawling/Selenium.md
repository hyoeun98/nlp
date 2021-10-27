# Selenium
```
# colab 환경에서 실행
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
!pip install selenium
```

```
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless') # GUI 창이 뜨지 않음. colab은 headless 환경임
options.add_argument('--no-sandbox') # 보안 기능 해제
options.add_argument('--disable-dev-shm-usage') # 공유 메모리를 담당하는 /dev/shm dir을 사용하지 않음
```
```
URL = 'https://google.com'
driver = webdriver.Chrome('chromedriver',options=options)
driver.get(URL)
print(wd.current_url)
driver.implicitly_wait(time_to_wait=5) #로드될 때까지 5초 대기
element = driver.find_element_by_class_name('gLFyf')
# element = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# Xpath = html내의 절대경로. Ctrl + Shift + C 클릭 후 copy

```
- 검색 가능한 태그
- elements는 해당 요소들을 iterable 객체로 return

![image](https://user-images.githubusercontent.com/62679143/139018358-62af8918-22a7-4d70-be96-a2969e130469.png)
```
from selenium.webdriver.common.keys import Keys
element.send_keys('') # 키보드 입력
element.clear() # 입력 지우기
upload = driver.find_element_by_tag('input')
upload.send_keys(file_path) # 파일 업로드
```
```
from selenium.webdriver.support.ui import Select

select = Select(driver.find_element_by_name('select_name'))

select.select_by_index(index=2)
select.select_by_visible_text(text="option_text")
select.select_by_value(value='고리오')

select.deselect_all() #선택 옵션 해제
submit_btn.submit() # 제출
```
```
driver.forward() # 앞으로 가기
driver.back() # 뒤로 가기
driver.minimize_window() #최소화
driver.maximize_window() #최대화
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #맨 밑으로 스크롤
driver.save_screenshot('screenshot.png') # 스크린샷 저장
``` 
```
from selenium.webdriver import ActionChains # 연속적인 동작 실행

menu = driver.find_element_by_css_selector('.nav')
hidden_submenu = driver.find_element_by_css_selector('.nav #submenu1')

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

# 위 한 줄은 아래와 같은 동작을 수행한다.
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()

# Ctrl + C를 누른다.
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# click(on_element=None)	인자로 주어진 요소를 왼쪽 클릭한다.
# click_and_hold(on_element=None)	인자로 주어진 요소를 왼쪽 클릭하고 누르고 있는다.
# release(on_element=None)	마우스를 주어진 요소에서 뗀다.
# context_click(on_element=None)	인자로 주어진 요소를 오른쪽 클릭한다.
# double_click(on_element=None)	인자로 주어진 요소를 왼쪽 더블클릭한다.
# drag_and_drop(source, target)	source 요소에서 마우스 왼쪽 클릭하여 계속 누른 채로 target까지 이동한 뒤 마우스를 놓는다.
# drag_and_drop_by_offset(source, xoffset, yoffset)	위와 비슷하지만 offset만큼 이동하여 마우스를 놓는다.
# key_down(value, element=None)	value로 주어진 키를 누르고 떼지 않는다.
# key_up(value, element=None)	value로 주어진 키를 뗀다.
# move_to_element(to_element)	마우스를 해당 요소의 중간 위치로 이동한다.
# move_to_element_with_offset(to_element, xoffset, yoffset)	마우스를 해당 요소에서 offset만큼 이동한 위치로 이동한다.
# pause(seconds)	주어진 시간(초 단위)만큼 입력을 중지한다.
# perform()	이미 쌓여 있는(stored) 모든 행동을 수행한다(chaining).
# reset_actions()	이미 쌓여 있는(stored) 모든 행동을 제거한다.
# send_keys(*keys_to_send)	키보드 입력을 현재 focused된 요소에 보낸다.
# send_keys_to_element(element, *keys_to_send)	키보드 입력을 주어진 요소에 보낸다.
```
```
from selenium.webdriver.common.alert import Alert # 경고창 handling

Alert(driver).accept() # 수락
Alert(driver).dismiss() # 거절

print(Alert(driver).text) # 경고 내용 출력
Alert(driver).send_keys(keysToSend=Keys.ESCAPE) # esc키 입력
```
```
class Keys(object):
    """
    Set of special keys codes.
    """

    NULL = '\ue000'
    CANCEL = '\ue001'  # ^break
    HELP = '\ue002'
    BACKSPACE = '\ue003'
    BACK_SPACE = BACKSPACE
    TAB = '\ue004'
    CLEAR = '\ue005'
    RETURN = '\ue006'
    ENTER = '\ue007'
    SHIFT = '\ue008'
    LEFT_SHIFT = SHIFT
    CONTROL = '\ue009'
    LEFT_CONTROL = CONTROL
    ALT = '\ue00a'
    LEFT_ALT = ALT
    PAUSE = '\ue00b'
    ESCAPE = '\ue00c'
    SPACE = '\ue00d'
    PAGE_UP = '\ue00e'
    PAGE_DOWN = '\ue00f'
    END = '\ue010'
    HOME = '\ue011'
    LEFT = '\ue012'
    ARROW_LEFT = LEFT
    UP = '\ue013'
    ARROW_UP = UP
    RIGHT = '\ue014'
    ARROW_RIGHT = RIGHT
    DOWN = '\ue015'
    ARROW_DOWN = DOWN
    INSERT = '\ue016'
    DELETE = '\ue017'
    SEMICOLON = '\ue018'
    EQUALS = '\ue019'

    NUMPAD0 = '\ue01a'  # number pad keys
    NUMPAD1 = '\ue01b'
    NUMPAD2 = '\ue01c'
    NUMPAD3 = '\ue01d'
    NUMPAD4 = '\ue01e'
    NUMPAD5 = '\ue01f'
    NUMPAD6 = '\ue020'
    NUMPAD7 = '\ue021'
    NUMPAD8 = '\ue022'
    NUMPAD9 = '\ue023'
    MULTIPLY = '\ue024'
    ADD = '\ue025'
    SEPARATOR = '\ue026'
    SUBTRACT = '\ue027'
    DECIMAL = '\ue028'
    DIVIDE = '\ue029'

    F1 = '\ue031'  # function  keys
    F2 = '\ue032'
    F3 = '\ue033'
    F4 = '\ue034'
    F5 = '\ue035'
    F6 = '\ue036'
    F7 = '\ue037'
    F8 = '\ue038'
    F9 = '\ue039'
    F10 = '\ue03a'
    F11 = '\ue03b'
    F12 = '\ue03c'

    META = '\ue03d'
    COMMAND = '\ue03d'
```

### Ref
- [참조](https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/)
- [Selenium doc](https://selenium-python.readthedocs.io/index.html)
