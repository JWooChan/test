# Git 실습 가이드

이 가이드는 `https://github.com/JWooChan/test.git` 리포지토리를 사용하여 Git의 기본 기능부터 브랜치 병합까지 연습할 수 있도록 구성되었습니다.

## 사전 준비
터미널을 열고 실습할 디렉토리로 이동하세요. (현재 디렉토리: `/home/hyconwc/test`)

---

## 1. Git 초기화 및 Push (Init to Push)

이 단계에서는 로컬 저장소를 초기화하고, Python 파일들을 생성하여 원격 저장소에 업로드합니다.

1.  **Git 초기화 및 원격 연결** (이미 진행하셨다면 생략 가능):
    ```bash
    git init
    git remote add origin https://github.com/JWooChan/test.git
    ```

2.  **실습용 파일 준비**:
    *   `abc.py`는 이미 생성되어 있습니다.
    *   새 디렉토리 `sub`를 만들고 그 안에 `def.py`를 생성합니다.
    ```bash
    mkdir sub
    echo 'print("Hello from def.py")' > sub/def.py
    ```

3.  **파일 스테이징 및 커밋**:
    ```bash
    git add .
    git commit -m "Initial commit: Add abc.py and sub/def.py"
    ```

4.  **원격 저장소로 Push**:
    ```bash
    git branch -M main
    git push -u origin main
    ```

---

## 2. Fast-forward Merge 진행

`abc.py` 파일을 수정하며 Fast-forward 병합을 실습합니다.

1.  **새 브랜치 생성 및 이동**:
    ```bash
    git checkout -b feature-python-A
    ```

2.  **`abc.py` 수정 및 커밋**:
    ```bash
    echo 'print("Added feature A")' >> abc.py
    git add abc.py
    git commit -m "Update abc.py in feature-python-A"
    ```

3.  **Main 브랜치로 복귀 및 병합**:
    ```bash
    git checkout main
    git merge feature-python-A
    ```
    *결과 확인: "Fast-forward" 메시지가 출력되는지 확인하세요.*

---

## 3. 3-Way Merge 진행

`sub/def.py` 파일을 동시에 수정하여 3-Way Merge를 실습합니다.

1.  **새 브랜치 생성 및 이동**:
    ```bash
    git checkout -b feature-python-B
    ```

2.  **브랜치에서 `sub/def.py` 수정 및 커밋**:
    ```bash
    echo 'print("Feature B update")' >> sub/def.py
    git add sub/def.py
    git commit -m "Update def.py in feature-python-B"
    ```

3.  **Main 브랜치로 복귀**:
    ```bash
    git checkout main
    ```

4.  **Main 브랜치에서 `sub/def.py` 수정 및 커밋 (분기점 만들기)**:
    *   주의: 같은 파일의 다른 줄을 수정하거나, 아예 다른 내용을 추가하여 충돌이 나지 않게 하거나, 충돌을 유도할 수도 있습니다. 여기서는 단순히 내용을 추가합니다.
    ```bash
    echo 'print("Main branch update")' >> sub/def.py
    git add sub/def.py
    git commit -m "Update def.py in main"
    ```

5.  **병합 수행 (3-Way Merge)**:
    ```bash
    git merge feature-python-B
    ```
    *결과 확인: Merge Commit 메시지 입력 창이 뜨면 저장하고 닫습니다.*

6.  **로그 확인**:
    ```bash
    git log --graph --oneline --all
    ```

---

## 마무리
```bash
git push origin main
```
