from typing import Any

class LookAheadIterator:
    iterable: Any = ...
    look_ahead: Any = ...
    markers: Any = ...
    default: Any = ...
    value: Any = ...
    def __init__(self, iterable: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def set_default(self, value: Any) -> None: ...
    def next(self): ...
    def __next__(self): ...
    def look(self, i: int = ...): ...
    def last(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def push_marker(self) -> None: ...
    def pop_marker(self, reset: Any) -> None: ...

class LookAheadListIterator:
    list: Any = ...
    marker: int = ...
    saved_markers: Any = ...
    default: Any = ...
    value: Any = ...
    def __init__(self, iterable: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def set_default(self, value: Any) -> None: ...
    def next(self): ...
    def __next__(self): ...
    def look(self, i: int = ...): ...
    def last(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def push_marker(self) -> None: ...
    def pop_marker(self, reset: Any) -> None: ...
