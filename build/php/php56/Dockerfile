FROM php:5.6-fpm


COPY ./sources.list.jessie /etc/apt/sources.list


RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install pdo \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install mysqli  mcrypt  mysql  zip 

# fix https://github.com/docker-library/php/issues/116
RUN apt-get update && apt-get install -y libssl-dev && rm -rf /var/lib/apt/lists/*



# composer
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/ 



WORKDIR /tmp

# 安装 redis 扩展
ADD ./resources/redis-4.3.0.tar.gz .
RUN mkdir -p /usr/src/php/ext \
    && mv /tmp/redis-4.3.0 /usr/src/php/ext/redis \
    && docker-php-ext-install redis


# memcache
ADD ./resources/memcache-2.2.7.tgz .
RUN cd /tmp/memcache-2.2.7 && phpize && ./configure && make && make install && rm -rf /tmp/memcache-2.2.7


# mongo
RUN pecl install mongo-1.6.14 \
    && docker-php-ext-enable mongo

# xdebug 
RUN pecl install xdebug-2.5.0 \
    && docker-php-ext-enable  xdebug 

RUN docker-php-source delete