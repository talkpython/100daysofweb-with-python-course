# Days 09-12 Building APIs with Api Star (0.5.41)

**Important**: at the time of recording the newest version of `apistar` was `0.5.41`, which let you build complete APIs. 

If you look at the [project docs](https://docs.apistar.com) today though, you'll see the following note:

> _Where did the server go?_ With version 0.6 onwards the API Star project is being focused as a framework-agnositic suite of API tooling. The plan is to build out this functionality in a way that makes it appropriate for use either as a stand-alone tool, or together with a large range of frameworks. The 0.5 branch remains available on GitHub, and can be installed from PyPI with `pip install apistar==0.5.41`.

For this reason and in order for the demo project to work we pinned it to version `0.5.41`.

---

## Day 1-2: Watch the video lessons

The first half of this 4-day block is to watch the videos and study API Star. Consider downloading and trying out the code samples developed during the course.

## Day 3: Make your own API

Now you have seen the videos from this chapter, you're ready to build an API using API Star!

For this day, you will get a data set from [Mockaroo](https://mockaroo.com/) or any other resource and load it in a sensible data structure (in the demo I used a `list` of `dict`s).

Data is everywhere, but if you don't get inspiration maybe you can use this [Marvel dataset](https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv) we used for one of our code challenges. If you don't know how to parse CSV, no worries: the same repo [has code for this](https://github.com/pybites/marvel_challenge/blob/solution/marvel.py).

Next make a virtual env, activate it and `pip install apistar==0.5.41` as shown in the videos (of course you can also use `pipenv` or `Anaconda`).

Then start to build your API using the skeleton from my demo. Try to implement the `GET` endpoint today (both all items and single item).

## Day 4: Flesh out (and test) the API

Next continue your API implementing the other CRUD operations: `POST`, `PUT` (update) and `DELETE` (**note** `PUT` requests require a trailing slash!). Make sure you add `404`s (data not there) where applicable.

Maybe you want to add some custom validations as well (like the manufacturer `enum` example in the lesson). See the [API Star docs](https://docs.apistar.com/type-system/).

Install [Postman](https://www.getpostman.com/) and run the different methods against various endpoints, do they all return the expected data and status codes?

If you have time left try to write some tests to automate the previous step. I recommend using `pytest` but that is not required. You probably do want to use [Api Star's TestClient](https://github.com/encode/apistar/blob/version-0.5.x/docs/api-guide/testing.md) for convenience (*note* this works for the version we are using in this lesson = 0.5, [starting 0.6 it's deprecated](https://docs.apistar.com/#where-did-the-server-go)).

Good luck and remember: _the learning is in the practice_.

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfWeb**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofweb-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofweb-with-python-course/pulls).*
