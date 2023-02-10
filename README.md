# How to create observable from an async iterator 

## Deacription
This is an example to demonstrate how to create observable to from an async iterator.

[Asyncio](https://docs.python.org/3.10/library/asyncio.html)
[RxPY](https://github.com/ReactiveX/RxPY)

## Usage 
Define async iterator
```
async def ticker(to, delay=.5):
    for i in range(to):
        yield i
        await asyncio.sleep(delay)
```

Create observable from the async iterator by observable helper
```
from utils.observable_helper import ObservableHelper

async def main():
    observables = []
    for i in range(random.randrange(5)):
        observables.append(observable_helper.from_aiter(ticker(to=random.randrange(15), delay=delay_array[random.randrange(len(delay_array))])))
    ...
```

Subscribe for the combine latest of all observables
```
async def main():
    ...
    done = asyncio.Future()

    def on_error(e):
        print("error: {}".format(e))
        done.set_result(False)

    def on_completed():
        print("completed")
        done.set_result(True)

    disposable = rx.combine_latest(*observables).subscribe(
        on_next=lambda i: print("next: {}".format(i)),
        on_error=lambda e: on_error,
        on_completed=on_completed
    )

    await done
    disposable.dispose()

```

## Install required packages
```
pip3 install -r requirements.txt

```

## Run and output result
```
$ python3 src/main.py

next: (0, 0)
next: (0, 1)
next: (0, 2)
next: (0, 3)
next: (1, 3)
next: (1, 4)
next: (1, 5)
next: (1, 6)
next: (1, 7)
next: (1, 8)
next: (1, 9)
next: (1, 10)
next: (1, 11)
next: (1, 12)
completed

```

## Other licenses