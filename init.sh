#!/bin/bash

[[ -d .venv ]] || virtualenv -p python3.6 .venv
source .venv/bin/activate
pip install -r requirements.txt


RED='\033[0;31m'
NC='\033[0m' # No Color

if [[ ! -f ".env" ]]; then

    touch .env


    printf "postgres host?${RED}[127.0.0.1]${NC}"
    read postgres_host

    if [ -z $postgres_host ]; then
        printf "POSTGRES_HOST=127.0.0.1\n" >> .env
    else
        printf "POSTGRES_HOST=$postgres_host\n" >> .env
    fi


    printf "postgres port?${RED}[5432]${NC}"
    read postgres_port

    if [ -z $redis_port ]; then
        printf "POSTGRES_PORT=5432\n" >> .env
    else
        printf "POSTGRES_PORT=$redis_port\n" >> .env
    fi


    printf "postgres name?${RED}[asan]${NC}"
    read postgres_name

    if [ -z $postgres_name ]; then
        printf "POSTGRES_NAME=asan\n" >> .env
    else
        printf "POSTGRES_NAME=$postgres_name\n" >> .env
    fi


    printf "postgres user?${RED}[postgres]${NC}"
    read postgres_user

    if [ -z $postgres_user ]; then
        printf "POSTGRES_USER=postgres\n" >> .env
    else
        printf "POSTGRES_USER=$postgres_user\n" >> .env
    fi


    printf "postgres password?${RED}[321321]${NC}"
    read postgres_pass

    if [ -z $postgres_pass ]; then
        printf "POSTGRES_PASS=321321\n" >> .env
    else
        printf "POSTGRES_PASS=$postgres_pass\n" >> .env
    fi

fi

source .venv/bin/activate
python manage.py createsuperuser
python manage.py runserver