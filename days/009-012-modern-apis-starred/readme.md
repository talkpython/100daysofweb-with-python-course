# Days 09-12 Building APIs with Api Star (0.5.x)

Now you have seen the videos from this chapter, you're ready to build an API using API Star!

## Day 1-2: Watch the video lessons

The first half of this 4-day block is to watch the videos and study API Star. Consider downloading and trying out the code samples developed during the course.

## Day 3: Make your own API

For this day, you will get a data set from [Mockaroo](https://mockaroo.com/) or any other resource and load it in a sensible data structure (in the demo I used a `list` of `dict`s).

Data is everywhere, but if you don't get inspiration maybe you can use this [Marvel dataset](https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv) we used for one of our code challenges. If you don't know how to parse CSV, no worries: the same repo [has code for this](https://github.com/pybites/marvel_challenge/blob/solution/marvel.py).

Next make a virtual env, activate it and `pip install apistar==0.5.41` as shown in the videos (of course you can also use `pipenv` or `Anaconda`).

Then start to build your API using the skeleton from my demo. Try to implement the `GET` endpoint today (both all items and single item).

## Day 4: Flesh out (and test) the API

Next continue your API implementing the other CRUD operations: `POST`, `PUT` (update) and `DELETE`. Make sure you add `404`s (data not there) where applicate. Maybe you want to add some custom validations as well (like the manufacturer `enum` example in the lesson). See the [API Star docs](https://docs.apistar.com/api-guide/type-system/).

Install [Postman](https://www.getpostman.com/) and run the different methods against various endpoints, do they all return the expected data and status codes?

If you have time left try to write some tests to automate the previous step. I recommend using `pytest` but that is not required. You probably do want to use [Api Star's TestClient](https://docs.apistar.com/api-guide/testing/) for convenience.

Good luck and remember: _the learning is in the practice_.

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfWeb**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofweb-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofweb-with-python-course/pulls).*
