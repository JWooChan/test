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

---

## 4. 실전 협업 시나리오 (기능 개선 및 재병합)

이미 병합된 `feature-python-B` 브랜치를 다시 사용하여 기능을 개선하고, `main` 브랜치에 반영하는 실전 흐름을 연습합니다.

**상황 가정**:
*   팀원들이 `main` 브랜치에 계속 코드를 업데이트하고 있다고 가정합니다.
*   나는 `feature-python-B` 브랜치에서 추가 작업을 진행해야 합니다.

1.  **작업 브랜치로 이동 (`checkout`)**:
    ```bash
    git checkout feature-python-B
    ```

2.  **기능 개선 작업 및 커밋**:
    `sub/def.py` 파일에 새로운 함수를 추가해 봅니다.
    ```bash
    echo 'def new_feature(): print("New feature in B")' >> sub/def.py
    git add sub/def.py
    git commit -m "Add new_feature function"
    ```

3.  **Main 브랜치 최신화 (협업 필수 과정)**:
    내 작업을 합치기 전에, `main` 브랜치에 다른 팀원의 작업이 올라왔을 수 있으므로 먼저 확인해야 합니다.
    ```bash
    git checkout main
    git pull origin main
    ```
    *(현재는 혼자 하므로 가져올 게 없다고 나올 수 있지만, 습관을 들이는 것이 좋습니다.)*

4.  **병합 (`merge`)**:
    ```bash
    git merge feature-python-B
    ```
    *이번에는 충돌 없이 깔끔하게 병합될 것입니다 (Fast-forward 혹은 Recursive).*

5.  **원격 저장소 반영 (`push`)**:
    ```bash
    git push origin main
    ```

6.  **작업 브랜치 정리 (선택 사항)**:
    작업이 완전히 끝났다면 브랜치를 삭제합니다.
    ```bash
git branch -d feature-python-B
```

---

## 5. 심화 시나리오: 날짜와 요일 (Date & Day)

`main` 브랜치에서 기본 기능을 만들고, `feature` 브랜치에서 이를 확장하는 조금 더 복잡한 시나리오입니다.

**목표**:
1.  `main`: 사용자에게 **날짜**를 입력받는 `date.py` 생성
2.  `feature-day`: `date.py`를 수정하여 **요일**까지 입력받도록 기능 확장
3.  `main`에 병합

### 5-1. Main 브랜치에서 날짜 기능 구현
먼저 `main` 브랜치로 이동하여 기본 코드를 작성합니다.

1.  **Main 이동**:
    ```bash
    git checkout main
    ```

2.  **`date.py` 생성 및 커밋**:
    ```bash
    cat <<EOF > date.py
    date = input("오늘 날짜를 입력하세요 (예: 2023-10-25): ")
    print(f"입력하신 날짜는 {date} 입니다.")
    EOF
    
    git add date.py
    git commit -m "Add date.py with date input"
    ```

### 5-2. Feature 브랜치에서 요일 기능 추가 (기존 브랜치 활용)
기존에 사용하던 `featureB` (또는 `feature-python-B`) 브랜치를 재사용하여 기능을 확장합니다.

1.  **기존 브랜치로 이동**:
    ```bash
    git checkout featureB
    ```
    *(만약 브랜치 이름이 `feature-python-B`라면 해당 이름으로 이동하세요.)*

2.  **Main 브랜치 내용 가져오기 (동기화)**:
    `main`에서 만든 `date.py`를 가져오기 위해 병합을 수행합니다.
    ```bash
    git merge main
    ```
    *(커밋 메시지 창이 뜨면 저장하고 닫습니다.)*

3.  **`date.py` 수정 (요일 기능 추가)**:
    기존 코드를 수정하여 요일도 물어보게 만듭니다.
    ```bash
    cat <<EOF > date.py
    date = input("오늘 날짜를 입력하세요 (예: 2023-10-25): ")
    day = input("오늘 요일을 입력하세요 (예: 수요일): ")
    print(f"오늘은 {date}, {day} 입니다.")
    EOF
    ```

4.  **커밋**:
    ```bash
    git add date.py
    git commit -m "Add day of week input to date.py"
    ```

### 5-3. 병합 및 마무리
기능 구현이 끝났으니 `main`에 합칩니다.

1.  **Main 이동 및 병합**:
    ```bash
    git checkout main
    git merge featureB
    ```

2.  **결과 확인 및 Push**:
    ```bash
    python3 date.py
    git push origin main
    ```

---

## 6. Rebase 실습 (히스토리 재작성)

Rebase는 브랜치의 기준점을 변경하여 히스토리를 깔끔하게 일직선으로 만드는 기법입니다. Merge와 달리 병합 커밋이 생기지 않습니다.

**Rebase vs Merge 차이점**:
*   **Merge**: 두 브랜치의 변경사항을 합치는 새로운 커밋 생성 (히스토리 보존)
*   **Rebase**: 내 커밋들을 다른 브랜치 끝으로 "이동" (히스토리 재작성)

### 6-1. 분기점 만들기
먼저 과거 커밋에서 새 브랜치를 만들어 Y자 모양의 분기를 생성합니다.

1.  **특정 커밋으로 이동** (예: `5d556ed` 커밋):
    ```bash
    git log --oneline --all
    # 원하는 커밋 해시를 찾습니다 (예: 5d556ed)
    git checkout 5d556ed
    ```

2.  **새 브랜치 생성**:
    ```bash
    git checkout -b feature-rebase
    ```

3.  **새로운 파일 추가 및 커밋**:
    ```bash
    echo 'print("Rebase feature")' > rebase_test.py
    git add rebase_test.py
    git commit -m "Add rebase_test.py"
    ```

4.  **추가 커밋 하나 더**:
    ```bash
    echo 'print("Another commit")' >> rebase_test.py
    git add rebase_test.py
    git commit -m "Update rebase_test.py"
    ```

### 6-2. Rebase 수행
이제 `feature-rebase` 브랜치를 `main`의 최신 상태 위로 이동시킵니다.

1.  **현재 상태 확인**:
    ```bash
    git log --graph --oneline --all
    ```
    *Y자 모양으로 갈라진 것을 확인하세요.*

2.  **Rebase 실행**:
    ```bash
    git rebase main
    ```
    *`feature-rebase`의 커밋들이 `main`의 최신 커밋 위로 재적용됩니다.*

3.  **결과 확인**:
    ```bash
    git log --graph --oneline --all
    ```
    *일직선으로 변경된 것을 확인하세요. 커밋 해시도 변경되었을 것입니다.*

### 6-3. Main에 병합 (Fast-forward)
Rebase 후에는 Fast-forward 병합이 가능합니다.

1.  **Main으로 이동**:
    ```bash
    git checkout main
    ```

2.  **병합**:
    ```bash
    git merge feature-rebase
    ```
    *Fast-forward 메시지가 나옵니다.*

3.  **Push**:
    ```bash
    git push origin main
    ```

### 6-4. 주의사항
> [!WARNING]
> **Rebase는 이미 Push된 커밋에는 사용하지 마세요!**
> 
> 커밋 해시가 변경되므로 다른 사람과 공유한 브랜치를 Rebase하면 충돌이 발생합니다. Rebase는 로컬에서만 작업한 브랜치에만 사용하세요.
```
