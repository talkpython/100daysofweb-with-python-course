# Days 37-40 introduction to Pyramid web framework

Now you have seen the videos from this chapter, you're ready to build a Pyramid-based web application. The actual app you build should be something fun but also not too big and challenging. Build something with just a few pages and then go from there.

That's why I found a list of simple web app ideas you can use for your first sample app in this chapter. Check out this blog post's simple app ideas. There are many and I'm sure you'll find one that is somewhat appealing to you.

[**flaviocopes.com/sample-app-ideas**](https://flaviocopes.com/sample-app-ideas/#simple-apps)

Look through that list and pick one you think you can tackle in a couple of hours.

## Day 1-2: Watch the video lessons

The first half of this 4-day block is to watch the videos. You can think of this chapter as paying it forward for the next two chapters with Michael. The videos were a little longer than normal but you'll earn that time back later in the course.

## Day 3: Create your website and routes

It's time to come back to your web app you picked in the beginning of this section. Make a short list of the pages / urls needed to make the site work. For each page, add the basic data items needed as well.

Use mockaroo to generate test data if you want realistic sample data: **[mockaroo.com](https://www.mockaroo.com)**

Then it's time to create your project using Cookiecutter. I recommend the starter template, but you can choose whichever one you want.

The basic steps are to install cookiecutter (and make sure it's in your path):

```
pip3 install --user --upgrade cookiecutter
```

Then run the template in the directory where you want the project created:

```
$ cookiecutter https://github.com/Pylons/pyramid-cookiecutter-starter
```

Then answer the questions from the template according to the app idea you chose. Remember to use Chameleon for your template language if you want to follow as close as possible.

Add all the routes with corresponding view methods and HTML templates for them. Don't worry about making these pretty. Also don't implement the data exchange or proper HTML in those templates. Save that for day 4.

Finally, add the SQLAlchemy data model. I recommend you simply copy the `db`, `data`, and `bin` folders from my demo code and adjust the imports and data classes accordingly. Don't forget to call the global init function in your `__init__.py` for the app startup.

If you are using mockaroo data, then edit the import behavior in the module from the `bin` folder.

## Day 4: Start using your data model and add a little design

You should have imported data and basic page structure from day 3. Now you can write the queries and return the data to the templates to make your site go. If you have extra time, give it a little CSS magic and grab an image from [unsplash](https://unsplash.com/) and / or [The noun project](https://thenounproject.com/)

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfWeb**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofweb-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofweb-with-python-course/pulls).*


