FROM php:8.1-apache

# Arguments defined in docker-compose.yml

# Install system dependencies
RUN apt update \
    && apt install -y \
        g++ \
        libicu-dev \
        libpq-dev \
        libzip-dev \
        libpng-dev \
        zip \
        zlib1g-dev \
        imagemagick \
        libmagickwand-dev \
        nodejs \
        npm \
    && a2enmod ssl \
    && a2enmod rewrite \
    && docker-php-ext-install \
        intl \
        opcache \
        pdo \
        pdo_pgsql \
        bcmath \
        exif \
        gd \
        zip \
    && pecl install imagick \
    && docker-php-ext-enable exif imagick \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# Get latest Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && echo 'post_max_size = 200M' > /usr/local/etc/php/php.ini \
    && echo 'memory_limit = 2048M' >> /usr/local/etc/php/conf.d/docker-php-memlimit.ini \
    && echo 'memory_limit = 120' >> /usr/local/etc/php/conf.d/docker-max_executiontime.ini \

# Set working directory
WORKDIR /var/www

RUN service apache2 restart

COPY ./src/ /var/www/html
COPY ./entrypoint.sh /

RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

COPY apache_host.conf /etc/apache2/sites-available/000-default.conf
