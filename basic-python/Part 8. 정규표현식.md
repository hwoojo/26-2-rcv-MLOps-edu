# 01. 정규 표현식이란
정규표현식이 뭐냐: 텍스트에서 일치되는 패턴을 찾는 문자열
- 일정한 패턴을 가진 문자열을 표현하는 방식
	- 문자열을 찾거나, 바꾸는 데에 활용
	- 문자열의 정합성 검증에 사용
- 파이썬의 경우, 표준 라이브러리인 re를 이용

# 02. 정규 표현식 사용하기
## 정규 표현식의 기본 개념
- 메타 문자: 패턴의 구조를 정의하는 데에 사용
- 특수 문자: 개행, 탭, 문자, 또는 숫자를 의미하는 등 사전에 정의된 특수 문자
- 문자 집합: 여러 문자와 매칭되는 패턴, 예를 들어 `[aeiou]`는 소문자 모음 한 글자를 의미
- 반복자: 패턴의 일부 또는 전체가 반복되는 것을 나타냄. `*`는 0회 이상, `+`는 1회 이상
- 그룹화: 패턴의 일부를 그룹화하여, 반복자를 사용하거나 매치된 부분을 추출하는데 사용
## 메타 문자
- `^`: 문장의 시작에 매칭
- `$`: 문장의 끝에 매칭
- `[]`: 문자 집합. 
	- 주어진 문자 집합에 포함되면 일치. `[abc]`는 a, b, c 중 한글자, `[a-z]`는 소문자 알파벳 한글자와 매칭
- `[^ ]`: 부정 문자 집합(여집합).
	- 주어진 문자 집합에 불포함되면 일치. `[^a-z]`는 소문자 알파벳이 아닌 한글자와 매칭
- `.`: 개행을 제외한 한 글자와 매칭. DOTALL 활성화시 개행 문자도 포함
- `|`: 선택 연산자. 연산자의 앞 또는 뒤의 식과 매칭되는 경우. `abc|def`는 abc 또는 def와 매칭됨.
- `()`: 하위 표현식 또는 하위 그룹으로 정의
- `\n`: n번째 하위 표현식을 가리킴. `(.+) \1`는 `the the`나 `55 55`와는 일치하지만 `thethe`와는 일치하지 않음
- `*`: 1개 이상 매칭되는 경우. `ab+c`는 abc, abcc 등에 매칭됨. `x[yz]+` xy, xz, xyyy, xyyzz 등에 매칭됨
- `?` : 0개 또는 1개 매칭되는 경우. `bc?c`는 bc, bcc에만 매칭됨
- `{m,n}`: m회 이상, n회 이하 일치되는 경우. `a{3,5}`은 aaa, aaaa, aaaaa와 매칭됨

## 특수 문자
- `\b`: 단어의 경계, 비문자를 의미. 공백, 괄호, 특수문자 등. `\bto\b`는 (to), to, to. 등과 일치하지만 top과는 일치하지 않음
- `\w`: 영문자 및 숫자, `_`에 해당하는 문자를 의미
- `\s`: 공백 문자. 스페이스, 탭, 개행 등을 의미
- `\d`: 모든 숫자들을 의미
- `\A`: 문자열의 시작 부분을 의미
- `\Z`: 문자열의 끝 부분을 의미

## 정규 표현식을 통한 탐색

- `re.search(pattern, string, flags=0)`: `string`에서 `pattern`이 일치하는 첫 번째 매치를 반환
- `re.match(pattern, string, flags=0)`: `string`의 시작 부분에서부터 `pattern`이 일치하면 해당 매치를 반환
- `re.fullmatch(pattern, string, flags=0)`: 전체 `string`이 정규식 패턴과 일치하면 그 매치를 반환
- `re.findall(pattern, string, flags=0)`: `string`에서 매치되는 모든 결과를 문자열 또는 튜플 형태로 반환

# 03. 정규 표현식 활용하기

## flags
- `re.IGNORECASE`, `re.I`: 대소문자를 구분하지 않고 매치를 수행
- `re.MULTILINE`, `re.M`: 문자열이 여러 줄로 이루어져 있을 때 각 줄의 시작과 끝에 대해 매치를 수행
- `re.DOTALL`, `re.S`: `.` 메타문자가 개행 문자를 포함하여 모든 문자와 매치
- `re.NOFLAG`: 기본 flags 값, flags 비활성화
- `|`, 여러 flags를 조합하여 적용하고자 할 때 사용

## 정규표현식을 통한 수정
- `re.sub(pattern, repl, string, count=0, flags=0)`
	- `pattern`: 찾고자 하는 정규 표현식 패턴
	- `repl`: 패턴과 매치된 부분을 대체할 문자열
	- `string`: 대상이 되는 전체 문자열
	- `count`: 치환할 최대 횟수. 기본값은 0으로, 0인 경우 모든 매치를 치환함
	- `flags`: 특수 조건 flags

## 정규식 객체 (re.Pattern)
- 정규식 객체 만들기: `re.compile(pattern, flags=0)`
- 하나의 정규식이 단일 프로그램 내에서 여러번 사용될 때, compile을 통해 정규식 객체를 재사용하는 것이 보다 효율적
- 정규식 객체 생성 시 flags를 적용할 수 있음

## 정규식 객체 (`re.Pattern`)를 통한 탐색

- `Pattern.search(string[, pos[, endpos]])`
    - `string`에서 `Pattern`과 매치되는 첫 번째 결과를 반환
    - 선택적 파라미터인 `pos`, `endpos`를 통해 시작점 및 끝점을 설정할 수 있음 (이어 탐색하기)
- `Pattern.match(string[, pos[, endpos]])`, `Pattern.fullmatch(string[, pos[, endpos]])`
    - 주어진 `string`의 시작 부분에서부터 `pattern`이 일치하면 해당 매치를 반환
    - `fullmatch`는 전체 문자열이 일치해야 함
    - 선택적 파라미터인 `pos`, `endpos`를 통해 시작점 및 끝점을 설정할 수 있음 (이어 탐색하기)

# 정규표현식 실습
## 핸드폰 번호 추출하기
- 주어진 개인 정보에서 핸드폰 번호 패턴을 정의하고, 이를 추출한다
- 한국 전화번호의 경우 `01x-xxx(x)-xxxx`형태의 규칙을 가짐
```python
import re

phone_number_pattern = re.compile(r'01[016789]-\d{3,4}-\d{4}')

personal_info = """
이름: 홍길동
주소: 서울시 강남구
전화번호: 010-1234-5678
주민등록번호: 930101-1234567
"""

match = phone_number_pattern.search(personal_info)
if match:
    print(f"핸드폰 번호: {match.group()}")
```
## CSV 파일 처리하기
- csv 파일은 ,로 내용이 구분된다.
- 구분된 내용을 그룹으로 지정하여 저장하고, 그 중 4번째와 6번째 그룹을 캡쳐하여 변수에 담는다.
- 변수에 저장된 내용을 처리한다.

```python
import re

pattern = re.compile(r'[^,]+,[^,]+,[^,]+,([^,]+),[^,]+,([^,]+)')

with open('log_file.csv', 'r') as file:
    for line in file:
        match = pattern.match(line)

        if match:
            fourth_value = match.group(1)
            sixth_value = match.group(2)

            print(f"4번째 값: {fourth_value}, 6번째 값: {sixth_value}")
        else:
            print("패턴과 매치되지 않는 라인이 있습니다.")
```

## 순서 바꾸기
- -으로 구분된 데이터 중, 두 번째 값과 세 번째 값의 순서를 바꾼다.
- 정해진 포멧대로 캡쳐하고, 캡쳐된 그룹의 순서를 바꾸어 다시 반환

```python
import re

input_string = "서울-대구-대전-부산"

result = re.sub(r'(\w+)-(\w+)-(\w+)-(\w+)', r'\1-\3-\2-\4', input_string)

print(result)
```
## 개인정보 마스킹하기
- 주어진 전화번호에 가운데 번호를 `*`로 마스킹하여 전화번호를 보호한다.
- 주어진 주민번호의 뒷6자리를 `*`로 마스킹하여 주민번호를 보호한다.

```python
import re

def mask_phone_numbers(match):
    return f"{match.group(1)}-****-{match.group(3)}"

def mask_ssn(match):
    return f"{match.group(1)}-{match.group(2)}******"

personal_info = """
이름: 홍길동
주소: 서울시 강남구
전화번호: 010-1234-5678
주민등록번호: 930101-1234567
"""

phone_number_pattern = re.compile(r'(01[016789])-(\d{3,4})-(\d{4})')
ssn_pattern = re.compile(r'(\d{6})-(\d)\d{6}')

masked_info = phone_number_pattern.sub(mask_phone_numbers, personal_info)
masked_info = ssn_pattern.sub(mask_ssn, masked_info)

print(masked_info)
```

## HTML 태그 제거하기
- HTML 태그는 `<>`로 둘러싸여있다.
- `<>`에 둘러싸인 값들을 빈 문자열로 대체하는 방식으로, HTML 태그를 제거할 수 있다.

```python
import re

def remove_html_tags(input):
    pattern = re.compile(r'<.*?>')
    result = re.sub(pattern, '', input)

    return result

input = "<p>This is <b>Python</b> and <i>Regular Expression</i>.</p>"

result = remove_html_tags(input)
print(result)
```

## 주민번호에서 생년월일 추출하기
- 주민번호의 경우 앞 6자리가 생년월일, 7번째 자리가 (1,2)이면 19xx, (3,4)이면 20xx년생이다.
- re.sub 활용 시 변환 함수를 이용한다.

```python
import re

def generate_birthday(matches):
    return f"{'19' if matches[4] in ('1', '2') else '20'}{matches[1]}. {matches[2]}. {matches[3]}"

ssn = "900101-4234567"

pattern = re.compile(r'(\d{2})(\d{2})(\d{2})-(\d)\d{6}')
result = pattern.sub(generate_birthday, ssn)

print(result)
```
