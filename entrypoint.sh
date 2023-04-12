#!/usr/bin/env bash

set -uex

RUN() {
    su www-data -s /bin/bash -c "$1"
}

pushd /var/www/html

    chown -R www-data:www-data /var/www/html

popd

apache2-foreground


