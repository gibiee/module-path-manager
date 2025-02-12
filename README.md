# module-path-manager
프로젝트의 내부 모듈들에서 간편하게 chdir와 sys.path를 설정할 수 있는 라이브러리

# 설치
```sh
pip install module-path-manager
```
- https://pypi.org/project/module-path-manager/

# 사용 예시
### 아래와 같은 디렉토리 구조의 프로젝트가 있다고 가정합니다.
```sh
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

- 예시 1. `main.py`에서 `a.py`, `b.py`, `c.py`를 import 한다면 아래와 같이 사용할 것입니다.
```py
# main.py
from module1 import a
from module2 import b
from module3.test import c
```

- 예시 2. `a.py`에서 `main.py`, `b.py`, `c.py`를 import 하려면 어떻게 할까요?
  - `main.py`는 상위 디렉토리에 있습니다.
  - `b.py`는 상위 디렉토리에서 `module2` 디렉토리에 접근해야 합니다.
  - `c.py`는 상위 디렉토리에서 `module3/test` 디렉토리에 접근해야 합니다.
```py
# a.py
import os, sys
sys.path.append('../')
os.chdir('../')

import main
from module2 import b
from module3.test import c
```

- 예시 3. `b.py`에서 `main.py`, `a.py`, `c.py`를 import 하려면 위 예시와 유사한 방식으로 하면 됩니다.
```py
# b.py
import os, sys
sys.path.append('../')
os.chdir('../')

import main
from module1 import a
from module3.test import c
```

- 예시 4. 그렇다면 `c.py`에서 `main.py`, `a.py`, `b.py`를 import 하려면 어떻게 할까요?
  - `main.py`는 상위 디렉토리의 상위 디렉토리에 있습니다.
  - `a.py`는 상위 디렉토리의 상위 디렉토리에서 `module1` 디렉토리에 접근해야 합니다.
  - `b.py`는 상위 디렉토리의 상위 디렉토리에서 `module2` 디렉토리에 접근해야 합니다.
```py
# c.py
import os, sys
sys.path.append('../../')
os.chdir('../../')

import main
from module1 import a
from module2 import b
```

- 위의 예시들을 보면 모듈 간의 import가 복잡해지면서 코드가 길어지고 가독성이 떨어지는 문제가 있습니다.
- 이러한 문제를 해결하기 위해 `module-path-manager`를 사용하면 아래와 같이 간단하게 import를 할 수 있습니다.
```py
# main.py / a.py / b.py / c.py
import model_path_manager
module_path_manager.set(current_file=__file__, target_file='main.py', depth=3, syspath=True, chdir=True)

import main
from module1 import a
from module2 import b
from module3.test import c
```