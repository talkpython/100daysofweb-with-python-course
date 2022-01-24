# Days 21-24 Async Flask apps with Quart

You're ready to build your first async Python application. This is a fun one and a skill most Python enthusiasts never develop!

## Day 1: Watch the video lessons

Today is just watching the corresponding videos from the course. They are about 30 minutes for this section of the videos (you'll finish the videos on day 3).

## Day 2: Convert a sync console / terminal app to be async

Look in the folder (relative to this file) for your starter project.

   `your_turn/day_2/web_crawl`
   
In here, there is a file called `program.py` and a requirements file. 

Start by creating a new virtual environment in Python 3.5 or higher. **Activate** the environment, then install the requirements via:

`pip install -r requirements.txt`

Now you can edit and run the program via `python program.py`

You'll see that it runs in the standard synchronous way. It does a little web scraping by downloading from [talkpython.fm](https://talkpython.fm) then pulling the title.
  
When you run it, you'll see things in order.

```
Getting HTML for episode 150
Getting TITLE for episode 150
Title found: Episode #150: Technical Lessons Learned from Pythonic Refactoring
Getting HTML for episode 151
Getting TITLE for episode 151
Title found: Episode #151: Gradual Typing of Production Applications
Getting HTML for episode 152 ...
```

Your job will be to convert the `get_html()` method to async. Recall the rules.

1. The method must be marked as `async`
2. You must `await` any async code that was called
3. You need to **run** it in an async loop

To replace requests, you'll use a library called `aiohttp`. Here's an example of getting some HTML from a site.

```python
async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
        resp.raise_for_status()

        return await resp.text()
```

Finally, you'll need to do step 3 above, run this in an async event loop. Update the `main()` method using two features built into Python to make this work:

* `asyncio.new_event_loop()`
* `loop.run_until_complete()`

Run your async version. Sadly, it will run the same speed as before because although it's async, we are waiting to do the next step and doing nothing really in parallel. 

This final step will unlock the speed and parallelism. Start all the async web calls, then wait for them as they complete.

```python
tasks = []
for n in range(150, 170):
    tasks.append((n, asyncio.create_task(get_html(n))) )

for n, t in tasks:
    html = await t
    ...
```

Now run it one more time. You should see parallelism in the results.

```
Getting HTML for episode 166
Getting HTML for episode 167
Getting HTML for episode 168
Getting HTML for episode 169
Getting TITLE for episode 150
Title found: Episode #150: Technical ...
Getting TITLE for episode 151
Title found: Episode #151: Gradual ...
Getting TITLE for episode 152 ...
```

All 20 "Getting HTML for episode" calls should basically run at the same time.

Congrats, you are now an async master!

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
