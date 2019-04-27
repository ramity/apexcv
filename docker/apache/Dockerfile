FROM php:7.2.1-apache

MAINTAINER Lewis Brown "github.com/ramity"

# Copy config from host
COPY ./config/php.ini /usr/local/etc/php/php.ini
COPY ./config/symfony.conf /etc/apache2/sites-available/000-default.conf

# Update base packages
RUN apt-get update

# Download composer and required deps
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN apt-get install -y git
RUN apt-get install -y zip
RUN apt-get install -y unzip
RUN apt-get install -y zlib1g-dev

# Install php extensions
RUN docker-php-ext-install pdo pdo_mysql mysqli opcache sockets zip
RUN docker-php-ext-enable opcache
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y libicu-dev
RUN apt-get install -y g++
RUN docker-php-ext-configure intl
RUN docker-php-ext-install intl

WORKDIR /var/www/symfony

EXPOSE 80
CMD a2enmod rewrite; apache2-foreground
