강의 개요 + 셸 소개 
https://missing.csail.mit.edu/2026/course-shell/
---
개요
1. 이 강의는 말 그대로 CS 강의 중에서 뭔가 다들 암묵적으로 안다고 생각하는 것이나, 아니면 뭔가 알아야 하지만 은근슬쩍 넘어가는 그런 것들에 대해 짚고 가는 것들
2. 강의에서도 실습을 더 중요시 함
---
# Shell
터미널이라고 섞어 표현하기도.

이것도 컴퓨터와 상호작용 하기 위한 하나의 방법 중 하나인데, GUI 또한 그런 것. 구이라고 읽음...
결국 텍스트 또한 이러한 방식으로 컴퓨터와 상호작용하기 위함임. 

이 터미널 안에 셸이 돌아가는 형태임. 

리눅스는 보통 bash, 맥은 zsh? 라고 bash-compatitable something인듯. bash는 좀 오래 되긴 했고. zsh는 좀 더 영하긴 하고. 윈도우는 batch or PowerShell. 심지어 윈도우는 그냥 wsl 아님 vm 쓰라고 할 정도로 sh계열의 명령어에 익숙해져야 함

이러나 저러나 셸은 운영체제 커널로 전달해주기 위한 해석기 프로그램인 거고, 그 종류 중에 bash, zsh, batch, 등등이 존재한다고 이해해야 할듯. 

## 왜 그럼 Shell인가
- 빨라서
	-  단순히 뭐 성능적으로 같은 이야기가 아니라 뭔가 뭐 클릭하고 뭐 하고 하는 것보다 텍스트로 휘리릭 해버리는 게 더 낫다고 생각하는 형태인듯
- 타이핑을 통해 (프롬프트를 통해) 프로그램을 실행할 수 있기 때문
- 오픈소스와도 깊게 관련이 있음. 거의 모든 오픈소스 프로그램을 셸을 통해서 실행 / 설치가 가능하고, 그냥 오픈소스로 된 프로그램도 있고

## Shell을 써보기
실습 겸으로 해서 내 shell과 같이 보도록 하자
```bash
hwoo@fedora:~$
```
이렇게 되어있으면, 알다시피 `hwoo`는 사용자명, @ < 이건 애초부터 at이란 의미고 `fedora`는 장치명, `~`는 내가 있는 경로를 의미하게 된다. 물결은 홈 디렉토리.

```bash
hwoo@fedora:~$ date
Mon Aug 31 12:12:16 PM KST 2026
```
뭐 이런 식으로 나오는데, 이러면 난 `date`라는 프로그램을 이용한 것임. date의 경우에는 인자(argument)를 따로 받지 않는 형태

그렇다면 인자를 받는 형태도 존재할 것
```bash
hwoo@fedora:~$ echo hello world
hello world
```
echo는 내가 뒤에 적는 것을 그대로 출력하는 프로그램. 그래서 인자를 넣어줘야 한다.
그리고 기본적으로 뭔가 글자와 글자 사이를 띄우는 형태를 가지는데, 그래서

```
hwoo@fedora:~$ echo hello            world
hello world
```
이런 식이 된다. 즉, 특수 문자를 온전히 다 받는 게 아니라 인자1 -> hello, 인자2 -> world 같이 이해를 해버리는 것

```
hwoo@fedora:~$ echo "hello            world"
hello            world
```
따옴표를 감싸는 것을 통해서 특수문자 유지를 할 수 있다
이제 여긴 인자 1 -> "hello        world" 이런 식으로 하나의 인자로 받아들이게 하는 것임

학생이 한 질문
1. 그럼 이거 .java, .py 같은 일종의 프로그램 같은 건지?
	1. 그렇다. 대신 저런 echo, date, 이런 거는 다 OS를 설치하면서 같이 기본적으로 설치되는 프로그램 중 하나인 것.
2. 그러면 java나 python프로그램 또한 이런 식으로 argument를 받는 형태가 존재하는데, 그거랑 비슷한 건지?
	1. 그렇다. 파이썬으로 만든 그 형태든 아니면 자바로 만든 그 형태든 다 이거랑 비슷하다. 형태가 같다고 생각하는 게 맞을듯?

이외에 `\`와 같은 escape 문자를 넣는 것도 가능하다고 

또 다른 질문
1. 그렇다면 띄어쓰기 공백과 escape 문자 `\`는 사실상 같은 것인가?
	1. 아님. 띄어쓰기 공백은 일종의 문자를 중간에 추가하는 것이고, escape 문자를 이용하는 것은 이 다음 글자를 또 다른 문자로 취급하지 말라는 그런... 명령을 내리는 거임. 즉 같은 인자로 취급하라고 표현하는 형태인듯.

그러면 너무나 많은 프로그램을 어떻게 다 알 수 있을까
이런 걸 알려주는 게 `man`아님 `tldr`임. man은 매뉴얼의 그거, tldr은 Too long didnt read의 약자 (인터넷 슬랭)으로 줄여서 말하면, 요약하자면, 뭐 그런 거임. 모든 프로그램을 다 넣어주는 건 아니고 1. 프로그램에서 man을 위해 매뉴얼을 넣어줬을 경우 2. 아니면 기본 프로그램들 이런 경우에는 다 된다고 생각하는 편이 나을듯. 더 알고 싶다면 그냥 터미널에 `man man`치면 매뉴얼의 매뉴얼이 나와버림...

아니면 `--help`를 하면 되겠죠? 아님 `-h`일 수도 있고...

cd, change directory를 알아보자
```
cd /bin/bash
```
와 같은 느낌. 알다시피 뒤에는 디렉토리를 줘야 한다.

코딩과 동일한 형태로 상대적 경로 / 절대적 경로로 구분할 수 있겠는데 기타 다른 그것과 같이 절대 경로는 시작이 슬래쉬 / 형태고 상대 경로는 시작 슬래쉬 없이 그냥 시작함

dot 과 dotdot
dot( . )은 지금 경로를 의미
dot dot( .. )은 부모 경로를 의미 

tab은 autocomplete. 이건 뭐 늘 알던 그대로의 것이고

## PATH에 대해
$PATH, 환경변수... alias... 뭐 이런 부류

단순히 echo 이런 게 그냥 어디서든 돌아가는 이유는 얘가 환경변수로 지정이 되어있기 때문임. 실제로는 특정 경로 특정 어딘가에 존재하는 형태임. 

```
hwoo@fedora:~$ echo $PATH
/home/hwoo/.local/bin:/home/hwoo/bin:/usr/local/bin:/usr/bin:/var/lib/snapd/snap/bin
hwoo@fedora:~$ which echo
/usr/bin/echo
```

이런 식이고 실제로 디렉토리 자체로 할 수도 있지만 굳이 뭐... 그럴 필요가 없지 않으니까.

아무튼 저 $PATH에 나오는 저 디렉토리들을 순차적으로 탐색한다고 함. echo $PATH에 있는 거. 이 덕에 어느 디렉토리에 있든 간에 바로바로 진행할 수 있는 것임

Q. 그럼 만약에 저 폴더에 같은 이름의 프로그램이 여러개 존재한다면 어떻게 되는가?
A. $PATH 디렉토리들을 순차적으로, 즉 앞에 나온 것부터 돌아가면서 보게 되고, `which -a {프로그램이름}`을 통해서 이 환경변수가 실제로 어디에 있는지를 전부 알 수 있다.

list, ls
해당 디렉토리에 있는 것을 리스팅하는 ls
eza가 좀 더 인간-친화적이라고? 이거는 좀 더 찾아보는 게 좋아 보이고

경로를 주면 그 경로, 아니면 지금 열려있는 이 경로를 연다

cat
그냥 그 파일을 열어봄. 보통 텍스트 

sort
열어보는데, 대신 그 안에 내용을 정렬해서
이건 텍스트 기반 정렬을 해주는 것이기 때문에 1, 2, 3, 4... 같은 순으로 정렬되는 건 맞으나 1, 11, 2, 23, 3, 4... 등과 같이 숫자를 나열하는 형태가 텍스트의 기반으로 나열된다는 것을 아는 게 좋다.

uniq
열어보는데, 대신 그 안 내용 중 중복되는 것은 빼고.
다만 그렇게 막 똑똑해서 모든 걸 다 지워주진 않고 연속적으로 중복된 게 나오면 그것에 대해 어떻게 잘 그 해주는 거임. 4가 연속적으로 있다가 중간에 3이 하나만 있어도 그 다음에 4를 또 출력하게 된다.

근데 sort -u 도 이런 역할을 해준다고. 얘는 대신 정렬도 해주고 그것도 해주겠지?

head, tail
`head -n3 data`하면 data의 앞부분 3줄만 들고온다
tail은 뒷부분. 

grep
이건 파일 검색기 같은 거임. 물론 파일을 검색하는 건 아니고... 할 수도 있긴 한데 아무튼. 
`grep 3 data`하면 data 파일 속 3이 있는 모든 것을 출력할 것
-r로 recursive, 재귀적 검색을 통해 하위 디렉토리를 탐구할 수도 있다

sed
뭔가를 수정할 수 있다고. -i는 In-file, in-line... 결국 추가적인 파일을 만드는 형태가 아니라 그냥 거기다가 수정을 하겠단 의미. 대신 얘는 자기 스스로 프로그램 언어가 달려있다고 한다.

```
hwoo@fedora:~$ sed -i 's/pattern/replacement/g' file
```
같은 형태로 표현하는데, 

`s/`로 sed 프로그램 언어를 시작
`/`로 구분하고
`pattern`이지만 뭐 검색하고자 하면 `grep`을 넣을 수도 있고. 지금 보면 replacement를 하는 명령어처럼 보인다. 그래서 `pattern/replacement`. 검색해서 바꾸려고 했다면 `grep/hwoo`처럼 해서 hwoo라고 적힌 걸 전부 변경할 수 있었을 것
`/g`를 통해 모든 파일을 수정할 수 있음. 

글고 표현식에서 와일드카드 같은 *  이런 건 단순히 어떤 특정 프로그램에 코딩된 게 아니라 운영체제 단으로 코딩이 되어 있는 형태임. 그러니까 `ls *.txt`라고 해도 먼저 셸이 이걸 읽고 -> 와일드카드 문자임 `*`를 이해해서 형태를 바꾸고 -> 이걸 이제 ls에 전달하는 형태인 거지 ls가 알아서 저걸 이해하는 형태가 아님. 

자꾸 강의에서 glob이라 하는데 이런 패턴을 표현하는 것. `*, ? ` 과 같은 문자들을 glob이라고 한다고 함.

find
얘가 진짜 파일 탐색기
근데 이제 검색만 하는
안에 인자로 뭐 type, name, mtime, 이런 걸 줄 수 있다 mtime은 modified time. 수정 시간이 얼마나 됐느냐를 볼 수 있음
size도 잇다네 당연히 파일의 크기를 의미하는 거고
exec을 통해서 해당 파일들에 무언가를 실행할 수 있다고 함. 가령 뭐 lh 라든가. lh는 리스팅을 하는데 좀 더 많은 내용을 담게 하는 것, 대신 h는 좀 더 사람이 읽기 좋게 표현하는 것임

또한 여기서 `\;`을 넣었는데, 이건 argument에 대한 리스팅을 끝낸다는 것을 의미함. 그러니까 여기까지만 exec하겠다는 것을 구분해주기 위함임

아무튼 이렇게 다양한 명령어를 얹고 얹어서 한 번에 뭐 어떤 파일들을 찾아서 뭘 어떻게 수정할 수 있게 해주는 거임

find는 기본적으로 재귀적이라고 함. 알아서 하위 디렉토리까지 탐색을 한다고. 이런 걸 조절하려면 -maxdepth argument를 이용하면 됨


awk
파싱을 위한 명령어
뭐 파일이 있으면 2열에만 있는 거 출력, 이런 게 가능한 것임
참고로 행렬 구분은 다른 게 아니라 그냥 공백으로도 구분이 된다고. 아니면 comma로 구분할 수 있는데 이럴 때에는 파일에 -F를 추가하는 것으로 찾아볼 수 있다고

Pipe
`|`이거 
일단 하는 일은 왼쪽 프로그램을 돌리고 -> 해서 나온 것을 오른쪽 명령어에 넣는 것임. 파이프처럼 실제로 연결한다?고 생각하는 편이 나아 보임.

Angle
`>`이거 
이건 왼쪽 프로그램을 돌리고 -> 해서 나온 것을 특정 파일에 저장하는 형태임.
`date >thedate.txt`하면 그 결과를 텍스트로 저장하겠지요?

반대로 
`sort <thedate.txt`
를 통해서 안에 있는 파일 내용물을 정렬할... 수도 있다고?

또한
`date >>thedate.txt`
를 통해서 append도 가능. = 뒷열에 추가한단 뜻

다양한 프로그램 언어와 같이 `if`, `for`, `while` 등의 반복문도 있다고.

`$()`
이건 괄호 안에 있는 명령어를 실행하고, 거기서 나온 결과물을 여기 이 위치로 교환하겠다는 의미임.

bash 또한 어떠한 프로그램 언어이기 때문에 파일로 만들 수도 있음. .sh가 그런 것. 즉 터미널에서 뭔가 하나하나 적는 걸 어떠한 프로그램으로 만들어서 뭐 보일 수도 있단 이야기인듯.

`#!`이란?
이 뒤에 있는 경로를 인풋으로 이용할 수 있게 한다? 이걸 인풋으로 넣는다?

뭔가를 실행할 때에 Shell은 그 파일을 열수 있나를 생각함. 
ls -l, ll을 통해서 볼 수 있음. chmod, change modification을 통해서 바꿀 수 있음. 
executable은 x니까 chmod +x를 통해 추가할 수 있음

---
# 실습
- For this course, you need to be using a Unix shell like Bash or ZSH. If you are on Linux or macOS, you don’t have to do anything special. If you are on Windows, you need to make sure you are not running cmd.exe or PowerShell; you can use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/) or a Linux virtual machine to use Unix-style command-line tools. To make sure you’re running an appropriate shell, you can try the command `echo $SHELL`. If it says something like `/bin/bash` or `/usr/bin/zsh`, that means you’re running the right program.

난 페도라니 문제 없지롱
```
hwoo@fedora:~$ echo $SHELL
/bin/bash
```
굿

- What does the `-l` flag to `ls` do? Run `ls -l /` and examine the output. What do the first 10 characters of each line mean? (Hint: `man ls`)

`ls -l`은 기본적으로 리스팅을 하되, 더 자세한 내용을 담도록 하는 것임. 맨 앞 10자 `drwxr-xr-x.`(예시임)은 권한을 의미하는데, r은 읽기 권한, w는 쓰기 권한, x는 실행 권한을 의미. 맨 앞 글자는 해당... 파일? 이 뭔지를 의미. d면 디렉토리, -면 그냥 파일, l면 링크라고 함. 링크? 링크는 뭐야 -> 바로가기라고....

이외 9자는 r,w,x로 이루어진 3개의 덩어리임. 소유자, 그룹, 나머지를 의미함. 해당 파일의 소유자는 앞 3글자에 따라서, 그 파일이 할당된 어떠한 그룹에는 중간 3글자의 권한이, 그리고 나머지 유저들에게는 마지막 3글자의 권한이 주어지게 됨

- In the command `find ~/Downloads -type f -name "*.zip" -mtime +30`, the `*.zip` is a “glob”. What is a glob? Create a test directory with some files and experiment with patterns like `ls *.txt`, `ls file?.txt`, and `ls {a,b,c}.txt`. See [Pattern Matching](https://www.gnu.org/software/bash/manual/html_node/Pattern-Matching.html) in the Bash manual.

glob은 내가 위에 적은 거긴 한데 어떠한 패턴을 찾게 하는 명령어... 라고 해야 할지 문법이라고 해야 할지... `*, ?, {}` 등과 같은 걸로 특정 문자를 포함한 모든 파일, 뭐 빵꾸 뚤어서 보기, 뭐 등등 같은 게 된다구

```
hwoo@fedora:~/Downloads$ ls *.jpg
123213132213.jpg  I01217.jpg  I01249.jpg  I01357.jpg  result.jpg  unnamed.jpg
```

```
hwoo@fedora:~/Downloads$ ls I0121?.jpg
I01217.jpg
hwoo@fedora:~/Downloads$ ls I0????.jpg
I01217.jpg  I01249.jpg  I01357.jpg
```

이런 식

brace extension은 문자열 생성기라고 생각하면 편함. {a,b,c}.jpg -> a.jpg, b.jpg, c.jpg로 만드는데, 중요한 건 저 쉼표 사이사이 띄어쓰기를 넣어선 절대 안 됨! 저거 넣으면 프로그램을 각자 다른 argument로 이해해버림.

- What’s the difference between `'single quotes'`, `"double quotes"`, and `$'ANSI quotes'`? Write a command that echoes a string containing a literal `$`, a `!`, and a newline character. See [Quoting](https://www.gnu.org/software/bash/manual/html_node/Quoting.html).

single quote는... 그냥 뭐 문자고. double quotes는 문자열. ANSI quotes는 뭘 의미하는 거지?


```
hwoo@fedora:~/Downloads$ echo "$HOME"
/home/hwoo
hwoo@fedora:~/Downloads$ echo '$HOME'
$HOME
hwoo@fedora:~/Downloads$ echo $'$HOME'
$HOME
```
흠

1. single quote는 정말 말 그대로 문자열을 만들어서 출력하는 형태인듯? 그래서 $HOME이 따로 경로가 안 나오고 문자 그대로 나오는 것이 아닐까
2. 반대로 double quote는 안에 있는 내용물을 바꾸기도 바꾸는듯. 긍께 뭐 $HOME 같은 게 작용한단 거겠지
3. ANSI...는 뭐지. 

찾아보니까 정말 저대로 $'뭐라고뭐라고' 이런 형태를 ANSI quote라고 하는듯. 저 안에서 escape 문자를 통해서 뭐 이것저것 할 수 있다. C/python에서 하는 것처럼 \n 같은 걸로 새 줄을 만들 수 있고. 

```
hwoo@fedora:~/Downloads$ echo "hello\nworld"
hello\nworld
hwoo@fedora:~/Downloads$ echo 'hello\nworld'
hello\nworld
hwoo@fedora:~/Downloads$ echo $'hello\nworld'
hello
world
```
엥~

ANSI quote는 escape 문자 같은 걸 쓸 수 있는 형태인듯 싶음. `\n` 같은 걸 ANSI... 계열이라 하나? -> Escape sequence라고 한다고 함.

```
hwoo@fedora:~/Downloads$ echo "this is a dollar sign $, and this is a bang ! and new line character \n"
this is a dollar sign $, and this is a bang ! and new line character \n
```

뭐 이렇게?

bang은 이전 히스토리를 끌고오는 역할이 있다고. 

```
hwoo@fedora:~/Downloads$ echo "!!"
echo "echo $'hello!'"
echo $'hello!'
```
이런 식으로?
얘도 Shell의 명령어기 때문에 큰따옴표에서 작동한다

- The shell has three standard streams: stdin (0), stdout (1), and stderr (2). Run `ls /nonexistent /tmp` and redirect stdout to one file and stderr to another. How would you redirect both to the same file? See [Redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html).

일단 
1. redirect stdout to one file
이건 뭐 `ls /nonexistent /tmp > out.txt` 하면 파일로 감

2. stderr to another
얘가 좀 문제였는데 공식 문서 읽어보니 `ls /nonexistent 2> out.txt`하면 `ls: cannot access '/nonexistent': No such file or directory`가 그대로 저 텍스트로 넘어감

3. redirect both to the same file
이건 그냥 >> 통해서 append 시켰음.

one-liner가 필요하겠지?
```
ls /nonexistent /tmp 1> right.txt 2>err.txt
```
를 통해서 각각 다른 파일로 보낼 수 있었고

```
ls /nonexistent /tmp >&right.txt
```
를 통해서 둘 다 같은 파일로 보낼 수 있다?


- `$?` holds the exit status of the last command (0 = success). `&&` runs the next command only if the previous succeeded; `||` runs it only if the previous failed. Write a one-liner that creates `/tmp/mydir` only if it doesn’t already exist. See [Exit Status](https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html).

`cd /tmp/mydir || mkdir /tmp/mydir` 가 단순히 보면 정답 같긴 한데...
하지만 이 경우는 뭐 저게 숨긴 파일이라 권한 문제가 발생할 수도 있다고 하네.

그러면... 

찾아보니 test 인자로 -d가 있고, 이거 이용하면 된다고 함! 얘가 디렉토리를 찾아준다고...

- Why does `cd` have to be built into the shell itself rather than a standalone program? (Hint: think about what a child process can and cannot affect in its parent.)

cd가 빌트인이어야 다양한 프로세스 동시 작업이 가능해서? 그리고 이런 식으로 parent, 즉 shell 단에서 가지고 있는 기능이어야 기타 다른 디렉토리를 건드릴 수 있어서? 즉 부모 디렉토리가 자식 디렉토리를 건드릴 수 있고 반대로 자식이 부모를 건드릴 수 없는 것과 같이?

아니래

디렉토리가 아니고 프로세스!
용어의 문제였는듯...

- Write a script that takes a filename as an argument (`$1`) and checks whether the file exists using `test -f` or `[ -f ... ]`. It should print different messages depending on whether the file exists. See [Bash Conditional Expressions](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html).
```
#!/bin/bash
if test -f $1; then
	echo "TRUE"
else
	echo "FALSE"
fi
```

이것이었고 ... 


- Save the script from the previous exercise to a file (e.g., `check.sh`). Try running it with `./check.sh somefile`. What happens? Now run `chmod +x check.sh` and try again. Why is this step necessary? (Hint: look at `ls -l check.sh` before and after the `chmod`.)
```bash
hwoo@fedora:~/Downloads$ ./test.sh 
bash: ./test.sh: Permission denied

hwoo@fedora:~/Downloads

$ ll test.sh 
-rw-r--r--. 1 hwoo hwoo 70 Aug 31 17:48 test.sh

hwoo@fedora:~/Downloads$ chmod +x test.sh

hwoo@fedora:~/Downloads$ ./test.sh 
TRUE
```

- What happens if you add `-x` to the `set` flags in a script? Try it with a simple script and observe the output. See [The Set Builtin](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html).
`set -x test.sh`를 해봤더니... 수많은 로그가 나왔다. 
들어보니 -x는 trace 하는 거라고. 

- Write a command that copies a file to a backup with today’s date in the filename (e.g., `notes.txt` → `notes_2026-01-12.txt`). (Hint: `$(date +%Y-%m-%d)`). See [Command Substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html).

```
hwoo@fedora:~$ mv notes.txt notes_$(date +%Y-%m-%d).txt
```

- Modify the flaky test script from the lecture to accept the test command as an argument instead of hardcoding `cargo test my_test`. (Hint: `$1` or `$@`). See [Special Parameters](https://www.gnu.org/software/bash/manual/html_node/Special-Parameters.html).

저 flaky test script는
```bash
#!/bin/bash
set -euo pipefail

# Start CPU stress in background
stress --cpu 8 &
STRESS_PID=$!

# Setup log file
LOGFILE="test_runs_$(date +%s).log"
echo "Logging to $LOGFILE"

# Run tests until one fails
RUN=1
while cargo test my_test > "$LOGFILE" 2>&1; do
    echo "Run $RUN passed"
    ((RUN++))
done

# Cleanup and report
kill $STRESS_PID
echo "Test failed on run $RUN"
echo "Last 20 lines of output:"
tail -n 20 "$LOGFILE"
echo "Full log: $LOGFILE"
```

여기서 while문을 이용해서 cargo test... 뭐 이게 되어 있는데, 


```bash
while cargo test my_test > "$LOGFILE" 2>&1; do
    echo "Run $RUN passed"
    ((RUN++))
done
```
이 cargo test my_test 부분이 하드 코딩이란 의미. 여기를 인자가 뒤에 바뀌어도 받을 수 있으려면 어떻게 해야 할까요?

`$@` 아님 `$1`이면 될듯? `$@`는 알아서 뒤에 인자들을 다 받는다고. `$1`이면 개수를 또 알 수 없으니까 `$@`를 이용하는 쪽이 맞는 거 같다

- Use pipes to find the 5 most common file extensions in your home directory. (Hint: combine `find`, `grep` or `sed` or `awk`, `sort`, `uniq -c`, and `head`.)
```
missing:~$ ssh myserver 'journalctl -u sshd -b-1 | grep "Disconnected from"' \
  | sed -E 's/.*Disconnected from .* user (.*) [^ ]+ port.*/\1/' \
  | sort | uniq -c \
  | sort -nk1,1 | tail -n10 \
  | awk '{print $2}' | paste -sd,
postgres,mysql,oracle,dell,ubuntu,inspur,test,admin,user,root
```
이거 수정하면 될듯 싶은데
```
hwoo@fedora:~$ find -type f | sed 's/.*\.//' | sort | uniq -c | sort -nk1,1 | tail -n5
```

와 sed 문법이 진짜 어렵다;;

- `xargs` converts lines from stdin into command arguments. Use `find` and `xargs` together (not `find -exec`) to find all `.sh` files in a directory and count the lines in each with `wc -l`. Bonus: make it handle filenames with spaces. (Hint: `-print0` and `-0`). See `man xargs`.

```
find -type f -name '*.sh' -print0 | xargs -0 wc -l
```
xargs 사용법이 좀 애매한듯? stdout을 argument로 쓸 수 있게 만든다? 

- Use `curl` to fetch the HTML of the course website (`https://missing.csail.mit.edu/`) and pipe it to `grep` to count how many lectures are listed. (Hint: look for a pattern that appears once per lecture; use `curl -s` to silence the progress output.)

```
curl -s https://missing.csail.mit.edu/ | grep -Ec [0-9]+/[0-9]+/[0-9]+
```

그냥 단순히 와일드카드 문자를 쓰면 안 된다! 숫자는 저런 식으로 표현할 수 있고 애초에 grep에 카운트 하는 것도 달려있다는 사실.... 저 -E를 해서 extended regular expression을 이용해서 저런 식으로 어떠한 숫자 (2자리 이상도 가능) 이런 식의 표현을 이용할 수 있다!

- [`jq`](https://jqlang.github.io/jq/) is a powerful tool for processing JSON data. Fetch the sample data at `https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json` with `curl` and use `jq` to extract just the names of people whose version is greater than 6. (Hint: pipe to `jq .` first to see the structure; then try `jq '.[] | select(...) | .name'`)

```
hwoo@fedora:~$ curl https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json | jq '.[] | select(.version > 6) | .name '
```

힌트가 다 맥여주고 잇엇잖아?

- `awk` can filter lines based on column values and manipulate output. For example, `awk '$3 ~ /pattern/ {$4=""; print}'` prints only lines where the third column matches `pattern`, while omitting the fourth column. Write an `awk` command that prints only lines where the second column is greater than 100, and swaps the first and third columns. Test with: `printf 'a 50 x\nb 150 y\nc 200 z\n'`

1. Write an `awk` command that prints only lines where the second column is greater than 100
	`printf 'a 50 x\nb 150 y\nc 200 z\n' | awk '{if($2>100)print}'`
awk도 조건문이 있다고 하네용

2. swaps the first and third columns.
`printf 'a 50 x\nb 150 y\nc 200 z\n' | awk '{temp = $1 ; $1 = $3 ; $3 = temp; print}'`
이런 식으로? 그냥 단순히 스왑하는 구문을 이용해서? 앞이랑 섞으면... 
`printf 'a 50 x\nb 150 y\nc 200 z\n' | awk '{if($2>100){temp = $1 ; $1 = $3 ; $3 = temp; print}}'`
이렇게?

- Dissect the SSH log pipeline from the lecture: what does each step do? Then build something similar to find your most-used shell commands from `~/.bash_history` (or `~/.zsh_history`).

여기서 말하는 로그 파이프라인은

```bash
missing:~$ ssh myserver # 서버접속
'journalctl -u sshd -b-1  \ #로그 기록 확인 
| grep "Disconnected from"' \ # 로그 중 Disconnect from 파트 검색
  | sed -E 's/.*Disconnected from .* user (.*) [^ ]+ port.*/\1/' \
  # 해당 부분에서 괄호 안에 있는 저 글자만 딱 캡쳐해서 들고옴. 뒤에 \1로 가져오는 거
  | sort | uniq -c \ # 정렬하고 겹치는 것 (연속적으로) 합치고 카운트로 바꾸기
  | sort -nk1,1 | tail -n10 \ # 1필드를 가지고, 즉 카운트를 가지고 정렬
  # 그리고 뒤에 있는 탑 10을 가져오기
  | awk '{print $2}' | paste -sd,
  # 2열만 출력 (이름만). paste는 원래 쭉 엔터로 구분되는 걸 serial, (-s) 한줄로 만들고 -d, delimiter, 즉 쉼표로 구분
postgres,mysql,oracle,dell,ubuntu,inspur,test,admin,user,root
```

이거 

각 스텝은

```bash 
ssh myserver 'journalctl -u sshd -b-1 | grep "Disconnected from"' \
  | sed -E 's/.*Disconnected from .* user (.*) [^ ]+ port.*/\1/' \
  | sort | uniq -c \
  | sort -nk1,1 | tail -n10 \
  | awk '{print $2}' | paste -sd,
```

```bash
cat .bash_history | sed -E 's/ .*//' | sort | uniq -c | sort -nk1,1 | tail -n1 | awk '{print $2}'
```

이게 정답이겠다. sed 구문이 참 어렵긴 한데... 일단 저건 s(바꾸는데) 공백 뒤 모든 글자를 없는 글자로 치환, 정렬, 겹치는 거 없애고 숫자 카운팅, 카운팅된 숫자로 다시 정렬, 최고 1개만 보이기, awk로 1열 안 보이게 하고 2열만 프린트

`s/찾을것/바꿀것/` 을 꼭꼭 외워두자

내 1등은 놀랍게도 sudo ㅎㅎ;; 
