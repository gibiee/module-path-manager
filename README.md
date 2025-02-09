# module-path-manager
프로젝트의 내부 모듈들에서 간편하게 chdir와 sys.path를 설정할 수 있는 라이브러리


# 사용 예시
### 아래와 같은 디렉토리 구조의 프로젝트가 있다고 가정합니다.
```
project/
├── README.md
├── module1/
│   └── a.py
├── module2/
│   └── b.py
├── module3/
│   └── test/
│       └── c.py
└── main.py
```

- `main.py`에서 a.py, b.py를 import 한다면 아래와 같이 사용할 것입니다.
```
# main.py
from module1 import a
from module2 import b
```

- `a.py`

- `b.py`

