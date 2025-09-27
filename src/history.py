### /src/history.py (starter)

class BrowserHistory:
    def __init__(self, start="home"):
        # TODO: choose your internal representation (two stacks)
        self._start = start
        self._cur = start
        self._back = []   # TODO
        self._fwd = []    # TODO

    def visit(self, url: str) -> None:
        # TODO: push current to back, set current, clear forward
        self._back.append(self._cur)
        self._cur = url
        self._fwd.clear()

    def back(self) -> str:
        if not self._back:
            raise IndexError("No pages in back history")
        # Peek at the next page
        if self._back[-1] == self._start:
            raise IndexError("No pages in back history")
        self._fwd.append(self._cur)
        self._cur = self._back.pop()
        return self._cur

    def forward(self) -> str:
        # TODO: move to next page; decide error behavior on underflow
        if not self._fwd:
            raise IndexError("No pages in forward history")
        self._back.append(self._cur)
        self._cur = self._fwd.pop()
        return self._cur

    def current(self) -> str:
        return self._cur
