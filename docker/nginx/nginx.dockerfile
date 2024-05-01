FROM nginx:1.25


RUN mkdir /var/places_remember/

RUN mkdir /var/places_remember/static
COPY ./static /var/places_remember/static

RUN mkdir /var/places_remember/media

RUN rm /etc/nginx/conf.d/default.conf


COPY ./nginx.conf /etc/nginx/conf.d