# Days 53-56 Django part 2: registration & login

In the coming 4 days we're going to further enhance our Quotes app adding user authentication.

We will `pip install django-registration`, [version 3.0](https://django-registration.readthedocs.io/en/3.0/) and implement its [two-step activation workflow](https://django-registration.readthedocs.io/en/3.0/activation-workflow.html).

This involves emailing an activation link, for which we will use [SendGrid](https://sendgrid.com), an _email delivery service_. Its free tier should get us started.

As I am writing this README (Oct 2018), `django-registration` 3.0 is pretty new, and it got a big overhaul! You can read more about it [here](https://www.b-list.org/weblog/2018/sep/04/three-dot-oh/). The timing could not be better to explore this new version!

Specially getting the _templating_ right took me some trial and error, so you don't have to go through that struggle yourself :)

As registration/login is such a common task when building a web app, mastering this lesson will give you a very useful skill to add to your toolbox!

Just sit back, relax and follow along with the videos, then practice yourself. Here is the plan for the coming 4 days:

## Day 1. + 2. - Watch the videos 

You can watch the videos during today and tomorrow (approx. 30 min a day).

Here I left some room to catch up on [Django part 1](https://github.com/talkpython/100daysofweb-with-python-course/tree/master/days/045-048-django-intro) which was quite dense.

Update 28th of May 2020: I had to add `DEFAULT_FROM_EMAIL` to settings.py (thanks [Iain](https://twitter.com/shutteritch/status/1265408235756040197))

## Day 3. + 4. - Practice yourself

Check out the starter Quote app from the [last Django lesson](https://github.com/talkpython/100daysofweb-with-python-course/tree/master/days/045-048-django-intro/demo) and follow along with the steps in my videos.

The best way to learn and commit this to muscle memory is to go through the steps at least once yourself.

Of course you don't have to use the Quotes app, ideally if you started a Django app during days 45-48, you should try to extend that with `django_registration`.

Have fun and share your work with us so we can sign up for your awesome app :)

Good luck and again remember: _the learning is in the practice_.

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfWeb**.

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofweb-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofweb-with-python-course/pulls).*
