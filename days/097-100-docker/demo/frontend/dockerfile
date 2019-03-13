FROM base_server:latest

RUN apt-get install -y -q nginx
RUN rm /etc/nginx/sites-enabled/default
COPY site.nginx /etc/nginx/sites-enabled/site.nginx
COPY movie_exploder /app

ENTRYPOINT nginx -g "daemon off;"
