FROM php:7.3-fpm

COPY ./sources.list.stretch /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install pdo \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install mysqli \
    && pecl install mongodb \
    && docker-php-ext-enable mongodb 


RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/ 


WORKDIR /tmp

# 安装 redis 扩展
ADD ./resources/redis-5.1.1.tgz .
RUN mkdir -p /usr/src/php/ext \
    && mv /tmp/redis-5.1.1 /usr/src/php/ext/redis \
    && docker-php-ext-install redis


# 增加 Memcached 扩展 
RUN apt-get update && \ 
apt-get install -y --no-install-recommends zlib1g-dev libmemcached-dev && \
rm -r /var/lib/apt/lists/* && \
pecl install memcached && \
docker-php-ext-enable memcached


# ADD ./resources/mcrypt-1.0.3.tgz .
# RUN cd /tmp/mcrypt-1.0.3 && phpize && ./configure && make && make install && rm -rf /tmp/mcrypt-1.0.3


ADD ./resources/xdebug-2.8.0.tgz .
RUN cd /tmp/xdebug-2.8.0 && phpize && ./configure && make && make install && rm -rf /tmp/xdebug-2.8.0


RUN apt-get install libmcrypt-dev
RUN pecl install mcrypt-1.0.2 && docker-php-ext-enable mcrypt

RUN docker-php-source delete