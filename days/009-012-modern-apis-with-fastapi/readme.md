# Days 09-12 Building APIs with FastAPI

This exercise section is going to have you laughing, no doubt. You're going to use FastAPI to create an API that will return a random programming-related joke.

---

## Days 1-3: Watch the video lessons

The first segment of this 4-day block is to watch the videos and study FastAPI. Consider downloading and trying out the [code sample developed during the course](https://github.com/talkpython/100daysofweb-with-python-course/tree/master/days/009-012-modern-apis-with-fastapi/demo).

## Day 4: Funny Business

Now you have seen the videos from this chapter, you're ready to build an API using FastAPI!

We are going to use the [pyjokes](https://pyjok.es) package. This is usually marketed as a CLI tool to get a joke in your terminal. But it also [has an API](https://pyjok.es/api/). It's this API that we can use to build a joke API.

###  Foundations

Before we talk about the details of your journey, let me give you a couple of foundational concepts from FastAPI so that you don't need to search the web *too* much (programming always involves some searching or AI-asking).

**FastAPI Starter Structure**

Simple FastAPI apps usually look something like this:

```python
import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/')
def some_action():
  return {"message": "Hello"}

if __name__ == '__main__':
  uvicorn.run(api, port=8001, host="127.0.0.1")
```

Incredible how simple these web apps are these days in their bare form.

**Passing data to actions**

The above api endpoint `some_action` is fun, but takes no data. If we wanted to pass a number, say `start_index`, we could do it like this using the `{}` wrappers in the URL:

```python
@api.get('/{start_index}')
def some_action(start_index):
```

But this is a string and index implies an integer. We could cast it ourselves, but FastAPI does that for us with validation by simply specifying the type in code, some_action(start_index**: int**):

```python
@api.get('/{start_index}')
def some_action(start_index: int):
```

**Constrained enums and string values**

Finally, in this exercise, you'll work with a small set of valid string values. For example, the pyjokes methods take a `category` of **neutral**, **all**, or **chuck** (as in Norris). We can express that way better with an enum (StrEnum specifically). Note: This type is only available in Python 3.11 or higher.

```python
class JokeCategory(enum.StrEnum):
    all = 'all'
    chuck_norris = 'chuck'
    neutral = 'neutral'
```

It's preferable to use this as the type in FastAPI because FastAPI will automatically reject all inputs that are not one of those three string values.

### Your Joke API

Use what we've given you above along with `pyjokes`, which you'll need to install as a dependency along with fastapi and uvicorn, to build a FastAPI that will listen at then URL:

`http://127.0.0.1:8001/api/laugh/chuck/en`

And pass in both the category and language (again see [the pyjokes API](https://pyjok.es/api/) for how to use it and valid inputs).

The response should be a JSON value such as:

```json
{
  "category": "chuck",
  "language": "en",
  "joke": "Every SQL statement that Chuck Norris codes has an implicit 'COMMIT' in its end."
}
```

Be creative, explore and have fun. Remember: _the learning is in the practice_.

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfWeb**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofweb-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofweb-with-python-course/pulls).*
