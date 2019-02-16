# Days 93-96 Frontend Web Apps with Vue.js

In this your-turn, you will deploy one of the web apps that you have created during this course.

## Day 1: Watch the first half of the video lessons

The first day of this 4-day block is to watch the videos. You should watch them from lecture 1 (Chapter into) -> lecture 18 (Your turn, day 2). 

## Day 2: Build out the app with fake data 

Now that you know some Vue.js, it's time to put it to use! Find the starter project in the folder `your_movie_exploder` (adjacent to this file). Open that in your editor. 

If you are using PyCharm or WebStorm, be sure that the Vue.js plugin is installed and enabled. We have already confirmed this version of the site as an `npm` package and installed the required dependencies. That means the Vue.js plugin should just work in the JetBrains tools, and maybe others too.

Because APIs can be so ephemeral and their schema unstable, we have decided to use the exact same app and service over at [movie_service.talkpython.fm](http://movie_service.talkpython.fm/). 

So your goal on this day will be to build out the 1st half of that app. You will build it out to use fake data (which you will save from the service). On the **4th day**, you'll start working with the real service using `axios`.

Here are a few steps and code concepts to help you on this journey.

### Creating the Vue.js app

To create the Vue.js app, you will create an instance passing the *settings* object. Do this in `js/site.js`.

```
var app = new Vue({
    el: '#app',
    data: {
        search_text: null,
    }
})
```

For this work, you'll need to set the id of the card block of HTML in `views/index.html` to `app`.

### Showing data in HTML as a string

To show data, you use the handlebar style, in HTML:

```
<div>
   {{search_text}}
</div>
```

### Bi-directionally bindings

To bind bi-directionally, use the model on elements that can change (input, select, etc):

```
<input type="text" v-model="search_text" />
```

Play around with this in your app to see that it's working.

To loop over data, use `v-for`, for exampe:

```
<div class="movie" v-for="m in movies">
</div>
```

For conditional rendering, it's `v-if` `and v-else`:

```
<span class="year" v-if="m.year > 0">{{m.year}}</span>
<span class="year" v-else>NO YEAR</span>
```

### Adding functions

To add functions to your app, use the methods field in the *settings* object:

```
methods: {
        the_function: function() {
            ...
        }
    }
```

### Hooking events

To hook events, use the @ directive on HTML elements. Here is an exampe:

```
<input type="text" v-model="search_text"  @keyup.enter="the_function()" />
```

### Setting attributes

One final bit of code you'll need to make this app work is the ability to set attributes. To do that, you'll use `:attribute_name="binding_value"`. For exampe:

```
<option v-for="g in genres" :value="g">{{g}}</option>
```

With all of this background info. Go ahead and write the app to work up to the point we had it with fake data. For that you'll need to create and include a fake_data.js file. Just save the data from the service.


## Day 3: Watch videos second half

...

## Day 4: Round out the app with the real service

...

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfWeb**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofweb-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofweb-with-python-course/pulls).*


