# Days 97-100 Docker

In this your-turn, you will develop the web app we created during the presentation.

## Day 1: Watch the Docker videos

The first day of this 4-day block is to watch the videos. You should watch them from lecture 1 (Chapter into) -> lecture 19 (Your turn, day 2). 

## Day 2: Dockerize one of your applications

At this point, you've seen a lot of Docker.  It's time to try it for yourself.

During this section, you will build out a docker container for one of your web applications. 

Feel free to choose the easy path and simply recreate the movie service in a docker container as you just saw in the videos.

Or you can be more adventurous and choose one of the Python web apps you built in this course. 

Remember that building docker containers is basically just configuring a Linux machine with command line options. So you can refer back to the deployment chapter for help as well.

## Building a docker container tips

Here are a few key ideas to help you on the way.

Commands:

* **docker build** .
* **docker run CONTAINER_ID**
* **docker run -it CONTAINER_ID bash** # for interactive mode
* **docker ps**
* **docker kill CONTAINER_ID**

Example docker file (from the demo):

```
FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y -q httpie
RUN apt-get install -y -q glances

RUN apt-get install -y -q nginx
RUN rm /etc/nginx/sites-enabled/default
COPY site.nginx /etc/nginx/sites-enabled/site.nginx
COPY movie_exploder /app

ENTRYPOINT nginx -g "daemon off;"
```

## Day 3: Watch videos second half

This day is just watching the second set of videos. You should watch them to **Your turn, day 4**.

## Day 4: Round out the app with the real service

You've mastered docker. However, you've seen the power of docker-compose for simple multi container applications. 

Build a docker-compse.yml file that will manage and run your application you build on day 2.

Have fun and check the demo code for the sample docker-compose file.

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfWeb**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofweb-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofweb-with-python-course/pulls).*
