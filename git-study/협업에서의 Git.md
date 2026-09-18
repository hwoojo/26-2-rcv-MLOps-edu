# Branch
협업을 한다고 하면 가장 중요한 것이 뭘까? 브랜치다.

수정을 할 때에도, 기능을 추가할 때에도, 긴급한 일이 발생을 해도, 거의 모든 상황에서 소스 코드를 건드릴 때에는 항상 브랜치로 구분을 한 다음에 병합하는 식으로 하게 된다.

## 추가적으로 알면 좋은 것들

`git push -d`는 왜 branch를 삭제하는가
git 명령어들을 좀 구분할 필요가 있음. push가 업로드, pull이 다운로드, 뭐 이런 식으로 기능적으로 생각할 게 아니라 이 명령어들이 정확히 어떤 일을 하는 앤지, 어떻게 작동하는 애인지 알게 된다면 왜 업로드 같은 곳에나 쓰던 push가 branch를 삭제하는 것에 이용되는 건지 알 수 있음. 즉, 명령어의 본질을 알아야 하는 것.

push는 기본적으로 원격 저장소의 ref를 내가 원하는 값으로 갱신하도록 요청하고, 더 나아가서 그 ref가 가리키는 데 필요한 git object를 전송하는 것에 있음.

즉, 내가 뭔가 로컬에서 업데이트 한 다음에 올리기 위해서 git commit하고 push 할 때, 이 스냅샷을 C라고 하겠다.
1. 원격 저장소에 main ref를  C로 바꾸라는 요청을 보냄
2. 그러나 로컬에서 수정한 것이므로 원격에는 C가 없을 것임. 
3. 그러므로 C와 필요한 object들을 보내줌
이런 역할을 하는 것.

즉 삭제하는 것도 가능하단 것임. 로컬에서 이제 '원격에 있는 이 ref를 삭제해줘' 같은 요청을 보내는 것. 이전에 적었지만 branch들은 ref를 통해서 구분되고 관리되기 때문에 걔를 가리키던 ref가 사라지게 되면 얘도 자연스럽게 사라진다. 

그럼 더 넓게
- branch 생성
- 업데이트
- 삭제
- tag 생성 / 업데이트 / 삭제 (얘들도 ref처럼 붙이는 애들이니까)
- 기타 ref 관리
가 전부 가능한 기능이란 것을 알 수 있다
# 원격 저장소에서 불러오기
`git pull` vs `git remote update`
둘 다 원격 저장소에서 불러오는 형태인데 뭐가 다른 걸까

```bash
git remote update
```
먼저 알아보자면, 얘는 사실 이런 명령어의 연속이다
```bash
git fetch origin
git fetch upstream
git fetch <기타 등등 remote>
```
만약에 다른 remote가 존재하지 않고 하나의 remote만 있다면 사실상 fetch랑 같다.
즉, 추가적인 작업이 있는 게 아니라 원격 저장소가 가지고 있던 remote를 업데이트 하는 것과 같으며, 결국 내가 작업하고 있는 HEAD가 바뀌진 않는다.

```bash
git pull
```
를 알아보자면

```bash
git fetch origin
git fetch upstream
git fetch <기타 등등>
git merge # 혹은 git rebase
```
뒤에 merge 혹은 rebase가 붙는다. 근데 rebase는 협업에서는 잘 이용되지 않으니까, merge라고 보는 편이 더 좋을 것이다. 저건 참고로 config에서 수정하는 걸로 된다고.

즉, remote를 업데이트 하는 것 넘어서 현재 브랜치의 upstream을 현재 브랜치 (내 로컬에 있는) 것에 통합을 시켜버린다.

Q. 엥? branch가 아니라 remote? 그럼 한 프로젝트에 remote가 여러개인 경우도 있는가? 
A. 그렇다. fork를 하면 이런 식으로 remote가 여러개 생긴다.

Q. 엥? 협업을 할 때엔 branch를 쓰는 게 아니었나? 갑자기 fork를 하는 이유는?
A. 무조건 branch는 아니다. fork 기반 협업 또한 흔하다. 근데 회사 말고 오픈소스 프로젝트 같은 곳에 많이 쓴다.

좀 더 알아보자.

# GitHub에서 협업과 권한
branch 기반 협업이라 하면 다들 흔히 생각하는 '같은 팀 내부에서 하나의 저장소를 가지고 작업'
- 팀원들이 모두 같은 저장소에 push 권한이 있고
- 각자 다른 branch에서 작업 후 PR해 merge

fork 기반 협업이라 하면 마치 '오픈소스 원본 프로젝트에 내 프로젝트를 진행'
- 원본 프로젝트가 존재하고 이에 대한 push 권한이 없음
- 따라서 fork한 다음에 복사본을 만들어서 거기다가 작업
- 이 경우 원본 repo가 upstream과 같은 ref를 달고 하나의 remote가 되고
- 내가 작업하는 이 repo는 origin과 같은 ref를 달고 하나의 remote가 된다

그러면 이런 생각을 할 수 있다. 만약에 누군가 코드를 망칠 가능성이 있을 수 있으니까 코드 보호를 위해서 다른 개발자에게 main에 접근 권한을 빡세게 막기 위해 회사에서도 fork 기반 협업을 할 수도 있지 않을까? 모두 다 fork를 통해서 코드를 복사 후 적고, 무조건 PR을 통해서만 수정을 할 수 있도록?

정답은 '그럴 수는 있다. 그렇지만...'인데, 왜냐면 이 push하는 권한과 뭔가 코드를 작성하는 write하는 코드를 구분할 수 있다. branch 별로도!

즉, branch 별로 누가 쓸 수 있을지, 누가 push를 할 수 있을지도 정할 수 있다. 이런 건 깃허브 웹 페이지 내에 세팅으로 존재한다고. 

contributor을 총 read, triage, write, admin, 등등으로 권한을 부여할 수 있고, 이걸 통해서 관리가 되기 때문에 push request를 누가 할 수 있는지 결정해 main 브랜치를 지킬 수 있다.

그렇다면 오픈소스 프로젝트는? 오픈소스 프로젝트는 수많은 사람이 수정하고자 하기 때문에 그게 어렵다. 이 코드를 수정하고 싶어하는 사람을 모두 다 contributor로 받아들이고 권한을 하나하나 주는 것이 거의 불가능에 가깝고, 과정 또한 번거롭기 때문에 차라리 fork를 통해 개인 소유 프로젝트로 만들고, 이걸 또 PR을 하는 식으로 해서 관리하게 된다.

# PR, Pull Request 요청하기

일단 PR은 branch / fork 단위로 요청할 수 있다. 내가 branch 구분해서 작업하다가 요청하거나, 아니면 fork해서 이것저것 만져본 다음에 이걸 원작자에게 주고 싶다면 주는 식으로. 따라서 그냥 branch에 커밋한 다음에 그걸 Pull Request 하면 되는데

그냥 깃허브 사이트에서 해도 되고, 아니다 난 CLI에서 하고 싶다 그렇다면 github CLI를 이용해서 `gh pr create`로 PR도 CLI에서 만들 수 있다.

---
이번엔 다양한 상황들을 만들어보고 해결해보자.
# 충돌, conflict 해결하기 
일단 충돌 상황을 만들어보고 싶다면
1. main branch에 특정 파일을 만들거나 수정
2. 다른 branch에서 그 파일을 수정
3. 이후 두 branch merge 시도

```bash
❯ git merge test
Auto-merging test.md
CONFLICT (add/add): Merge conflict in test.md
Automatic merge failed; fix conflicts and then commit the result.
```
문제가 발생했다

```
<<<<<<< HEAD
이건 메인 브랜치

=======
이건 테스트 브랜치에서 작성
>>>>>>> test
```
이런 식으로 되었다. 실제로 내가 적지 않은 구분선이 생겼다. 깃 측에서 이거 두 개가 충돌이 났다 (HEAD는 내가 작업하고 있던 main에서 발생, merge하려고 했던 test에서 발생)

```
이제 이건 수정 후 텍스트
```
라고 다 지운 후 수정하고 
커밋하면

```shell
❯ git log --oneline --graph --decorate --all
*   d1946c5 (HEAD -> main) Merge branch 'test'
|\
| * ef05eae (test) editting in test branch
* | 25d3124 test.md for conflict error test
|/
* b3ca3eb (origin/main, origin/HEAD) Make git study folder and the first version of note
```
이런 식으로 내가 만들었던 또 다른 branch가 합쳐졌음이 보인다

## 추가로
이런 걸 테스트 했지만 이걸 굳이 GitHub에 올릴 필요는 없어 보인다.
```bash
❯ git status
On branch main
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```
이 로컬 커밋이 대충 3개 정도 차이가 있다고 한다. 원격 저장소와. 하지만 굳이 테스트한 걸 GitHub에 올릴 필요는 없어 보이니까 

```bash
git restore .
# 만약 stage에도 내리려면 git restore --staged . 
```

로 되돌릴 수 있다.

하지만 난 커밋까지 해버렸는데? 다시 깃헙 저장소 상태로 돌아가려면?
```bash
git fetch origin
git reset --hard origin/main
```
명령어로 내 branch를 되돌릴 수 있다

```bash
26-2-rcv-MLOps-edu  main ⇡
❯ git restore .
26-2-rcv-MLOps-edu  main ⇡
❯ git restore --staged .
26-2-rcv-MLOps-edu  main ⇡
❯ git fetch origin
26-2-rcv-MLOps-edu  main ⇡
❯ git reset --hard origin/main
HEAD is now at b3ca3eb Make git study folder and the first version of note
26-2-rcv-MLOps-edu  main
❯
```
위로 화살표 그려진 게 내 셸에서 보여주는 push할 게 있다는 표시인데, restore을 해도 안 사라지다가 아예 reset을 시키자 사라진 걸 볼 수 있다. 왜냐면 난 커밋까지 했었기 때문

```bash
26-2-rcv-MLOps-edu  main
❯ ls
git-study  missing-semester  README.md
```
만들었던 test.md도 사라진 걸 볼 수 있다.

# 수정하는 상황
```
repo: team-practice
branch: main

파일:
README.md
app.py
```
내가 팀에서 일을 하는데 이런 이슈가 올라왔다. 

```
Issue #12
Title: Add greet command

app.py에 greet(name) 함수를 추가해주세요.

예:
greet("hwoo")
→ Hello, hwoo!
```
그리고 이런 사규가 있다고 한다
```
1. main에 직접 push 금지
2. Issue별로 branch 생성
3. 작업 완료 후 GitHub에 push
4. PR을 main으로 생성
```

그럼 난 어떤 식으로 작업을 해야 할까?

일단 `git status`를 확인해보자. 난 내 토이 프로젝트 파일과 레포에다가 해보겠다.

```bash
LocalAppManager  main
❯ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```
일단 지금은 main에 내가 있다. 일단 직접 push를 해서는 안 되니 branch 구분을 해보자
``` bash
LocalAppManager  main
❯ git branch feature/greet
LocalAppManager  main
❯ git switch feature/greet
Switched to branch 'feature/greet'
LocalAppManager  feature/greet
❯
```
greet라는 기능을 만들기 위해 새로운 branch를 생성하고 이동했다. 말했듯이 switch 대신 checkout을 써도 되긴 하다.

아님 더 간단하게 하려면 `git switch -c feature/greet`를 통해 branch를 만듦과 동시에 바꿀 수도 있다

```bash
LocalAppManager  feature/greet
❯ nvim app.md

greet("hwoo"):
print(hello {input}!)

```
프로그래밍 하기 귀찮으니 이런 텍스트를 md 파일로 만들었다

```bash
❯ nvim app.md
LocalAppManager  feature/greet ? took 1m24s
❯ git add app.md
LocalAppManager  feature/greet +
❯ git commit
[feature/greet 2db3a7e] make add function 
 1 file changed, 2 insertions(+)
 create mode 100644 app.md
```
git add로 스테이징 해주고 커밋을 해주자

commit 메시지는 일단 test make 정도로 적었다. 실무에선 더 잘 적어야 함 ;;

```bash
❯ git branch -v
* feature/greet 2db3a7e test make
  main          250df9f change format / linting
```
```bash
❯ git diff main...HEAD
diff --git a/app.md b/app.md
new file mode 100644
index 0000000..f7f155b
--- /dev/null
+++ b/app.md
@@ -0,0 +1,2 @@
+greet("hwoo"):
+print(hello {input}!)
```

이제 이걸 PR하면 되겠다.

그러면 좋겠지만 아니다. 왜냐면 아직 저건 로컬 브랜치기 때문.

```bash
git push -u origin feature/greet
```
를 통해 원격 remote origin에 feature/greet 브랜치를 생성해준다

이제는 진짜 PR을 할 수 있겠다.

# 잘못된 merge를 했을 때
```bash
LocalAppManager  feature/greet
❯ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
LocalAppManager  main
❯ git merge feature/greet
Updating 250df9f..2db3a7e
Fast-forward
 app.md | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 app.md
```
괜찮다고 생각하고 merge를 했다. 

근데 뭔가 저 기능 때문에 갑자기 서비스가 먹통이 됐다! 그렇다면 어떻게 해야 할까?

```bash
LocalAppManager  main ⇡
❯ git reset --hard origin/main
HEAD is now at 250df9f change format / linting
```
push를 하지 않아 로컬 브랜치에 있다면 이런 식으로 초기화 할 수 있겠지만...

push를 했다고 가정하면?!
일단 log를 보자
```bash
LocalAppManager  main
❯ git log --oneline --graph --decorate --all
* 2db3a7e (HEAD -> main, origin/main, feature/greet) test make
* 250df9f (origin/master) change format / linting
* 9fe1b13 Refresh project documentation and desktop launcher configuration
* 142edf3 initial commit
```

2db3a7e가 문제가 발생한 push의 해시
250df9f이 되돌려야 하는 스냅샷이겠다

```bash
LocalAppManager  main
❯ git revert 250df9
[main 7328cdf] Revert "change format / linting"
 39 files changed, 192 insertions(+), 613 deletions(-)
 delete mode 100644 Dockerfile
 delete mode 100644 uv.lock
```
```
LocalAppManager  main ⇡ took 4s
❯ ls
app.md  build            docs     pyproject.toml  src    TODO.md
assets  CONTRIBUTING.md  LICENSE  README.md       tests  venv
```
```bash
LocalAppManager  main ⇡
❯ git log --oneline --graph --decorate --all
* 7328cdf (HEAD -> main) Revert "change format / linting"
* 2db3a7e (origin/main, feature/greet) test make
* 250df9f (origin/master) change format / linting
* 9fe1b13 Refresh project documentation and desktop launcher configuration
* 142edf3 initial commit
```

엥? 뭔가 이상하다! 
왜 app.md는 그대로 있을까?
그리고 쌩뚱맞게 
```bash
 delete mode 100644 Dockerfile
 delete mode 100644 uv.lock
```
이건 왜 지운 걸까? 

알고 보니 git revert는 내가 돌리고자 하는 곳으로 돌리는 게 아니라 내가 지우고자 하는 애의 해시를 넘겨야 한단 것!
지금은 이런 식으로 하면 이 전전 수정인 Docker와 uv 파일을 추가했던 걸 되돌리게 된다.
이로서 알 수 있는 점은 git revert는 시간을 되돌리는 장치가 아니라 해당 작업에서 수정했던 점을 되돌리게 한다는 것. 즉, 이 전전 부모의 것만 되돌리고 전 부모의 것, 부모의 것은 그대로 남긴 상태로 되돌릴 수도 있단 것을 알게 된다. 

좋다. 그럼 다시 되돌리기를 되돌리자. 다행히 저런 행동을 하고 나서 push를 하지 않았다. 그렇다면 
```shell
LocalAppManager  main ⇡
❯ git reset --hard origin/main
HEAD is now at 2db3a7e test make
```
이것으로 다시 되돌릴 수 있다.

```shell
LocalAppManager  main
❯ git log --oneline --graph --decorate --all
* 2db3a7e (HEAD -> main, origin/main, feature/greet) test make
* 250df9f (origin/master) change format / linting
* 9fe1b13 Refresh project documentation and desktop launcher configuration
* 142edf3 initial commit
```
다시 test make라 적힌 저 feature/greet이 가장 위에 올라와있다

```shell
LocalAppManager  main
❯ git revert 2db3a7e
[main 9e03bc5] Revert "test make"
 1 file changed, 2 deletions(-)
 delete mode 100644 app.md
LocalAppManager  main ⇡ took 4s
❯ git log --oneline --graph --decorate --all
* 9e03bc5 (HEAD -> main) Revert "test make"
* 2db3a7e (origin/main, feature/greet) test make
* 250df9f (origin/master) change format / linting
* 9fe1b13 Refresh project documentation and desktop launcher configuration
* 142edf3 initial commit
```
이번엔 옳은 해시를 넣어주자
```shell
LocalAppManager  main ⇡
❯ ls
assets  CONTRIBUTING.md  docs     pyproject.toml  src    TODO.md  venv
build   Dockerfile       LICENSE  README.md       tests  uv.lock
```
이젠 app.md 파일이 사라진 것을 알 수 있다.

