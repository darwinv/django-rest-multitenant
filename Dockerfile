# imagen oficial de ubuntu
FROM ubuntu:20.04

# Instalamos la dependencias, por default nos trae python 3.8
RUN apt-get update && \
    apt-get install --no-install-recommends -y python3-pip python3.8-dev && \
    apt-get install vim && \
    apt-get install git -y postgresql-client postgresql-dev


# colocando el PYTHONUNBUFFERED a un valor no vacío, podemos
# ver los logs de python en nuestro contenedor
ENV PYTHONUNBUFFERED 1


# creamos el directorio de nuestra aplicación
RUN mkdir /app/

# seteamos el directorio y copiamos toda nuestra app
# es necesario asegurarse mantener actualizado el dockerignore
# para no pasar data que no queremos dockerizar
WORKDIR /app/
ADD . /app/

# instalamos pipenv
RUN pip install pipenv

# agregamos nuestros archivos de pipfile al directorio de la app
ADD ./Pipfile /app/
ADD ./Pipfile.lock /app/


# instalamos la dependencias
RUN pipenv install --dev
