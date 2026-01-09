FROM ubuntu:latest

RUN apt-get update && apt install -y apache2 apache2-utils
RUN apt install -y php8.3 php8.3-cli python3 ffmpeg curl wget git
EXPOSE 80
COPY ./src/supervisor.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["apachectl", "-D", "FOREGROUND"]