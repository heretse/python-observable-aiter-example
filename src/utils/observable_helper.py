import asyncio
import functools
import reactivex as rx
from reactivex.disposable import Disposable
from reactivex import create

class ObservableHelper:
    def __init__(self, loop):
        self.loop = loop

    def from_aiter(self, iter):
        def on_subscribe(observer, scheduler):
            async def _aio_sub():
                try:
                    async for i in iter:
                        observer.on_next(i)
                    self.loop.call_soon(observer.on_completed)
                except Exception as e:
                    self.loop.call_soon(functools.partial(observer.on_error, e))

            task = asyncio.ensure_future(_aio_sub(), loop=self.loop)
            return Disposable(lambda: task.cancel())

        return create(on_subscribe)
