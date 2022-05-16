FROM ubuntu:20.04
# Maintainer’s information(name & email)
LABEL maintainername="Wenlin Wang"
LABEL maintaineremail="wenlin.wang@student.unimelb.edu.au"
# Define a variable of PHP version
LABEL PHPVER="7.4"
# Define time zone
ENV TZ=Australia/Melbourne
# Set time zone 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ> /etc/timezone \
    && apt-get update \
        # Install build dependencies and libraries
        && apt-get install software-properties-common -y\
        # Add the repository of php
        && add-apt-repository ppa:ondrej/php && apt-get update \
        # Install Nginx, PHP(version 7.4), and PHP-FPM
        && apt-get install nginx php7.4 php7.4-fpm -y

# Add the modified Nginx setting file to replace the default one
ADD $PWD/nginx.ini /etc/nginx/sites-enabled/default

# Copy the testing html and php to the root folder 
COPY $PWD/index.html /var/www/html/

# Expose and publish the port 80 for Nginx
EXPOSE 80

# Volume (web's root folder)
VOLUME /var/www/html

# Set the working directory
WORKDIR /var/www/html

# Start Nginx and PHP-FPM (using entrypoint)
ENTRYPOINT ["/bin/bash", "-c", "/usr/sbin/service php7.4-fpm start && nginx -g 'daemon off;'"]