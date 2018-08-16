# Days 33-36 Data access with SQLAlchemy

Now you have seen the videos from this chapter, you're ready to build a data-driven application using a database ORM - SQLAlchemy.

## Day 1-2: Watch the video lessons

The first half of this 4-day block is to watch the videos and study SQLAlchemy. Consider downloading and trying out the code samples developed during the course.

## Day 3: Start your database project

For this day, you will pick a database project from a list of ideas. You will model the data and create the basic project structure. This includes:

* The classes that build the database model (SQLAlchemy entities)
* Setup the connection to the DB (sqlite)
* Put the unit of work pieces in place (session_factory, etc)




## Day 3: Watch the web videos

Now it's back to learning. Watch the second half of this chapter and get ready for day 4 where you put that into action.

## Day 4: Make your existing web app async

Let's freestyle a little here.

You're already created a Flask app from when we introduced Flask back at the beginning of the course. Take that, or any other Flask app you've built.

If you can't find a good example, you're welcome to borrow the one we used in the lessons here. There is a copy at:

`your_turn/day_4/cityscape_api`

Make a copy of this web site so you can mess it up. :)

Make one of your view methods arbitrary slow by making it wait. Import `time`, and add a `time.sleep(2)` to make it 2 seconds slower.

Now, convert it to Quart.

1. Be sure to install `quart`
2. Replace the word `flask` with `quart` everywhere
2. Make the view method async
3. `await` the slow things (time via asyncio.sleep() or something else)
4. Run it in `hypercon` as we did in the videos
5. Make sure it still works and it should scale better 

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfWeb**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofweb-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofweb-with-python-course/pulls).*
