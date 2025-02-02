<a href="https://www.islas.org.mx/"><img src="https://www.islas.org.mx/img/logo.svg" align="right" width="256" /></a>
# geoambiental

Clases para manipular y cargar datos geoambientales
====

[![Build Status](https://travis-ci.org/IslasGECI/geoambiental.svg?branch=develop)](https://travis-ci.org/IslasGECI/geoambiental) [![Coverage Status](https://codecov.io/gh/islasgeci/geoambiental/branch/develop/graph/badge.svg)]((https://codecov.io/gh/islasgeci/geoambiental))

El repositorio *geoambiental* contiene las clases `Map`, `Field`, `TimeSeries` y `Profile`. Las clases definidas en este repositorio se usan para comunicar la capa _procesamiento_ (_negocio_) con la capa _graficado_ (_presentación_). La salida de las funciones en la capa de _procesamiento_ son objetos que pertenecen a las clases de este repositorio y a su vez son la entrada de las funciones en la capa de _graficado_.

## Diagrama UML

### Estado actual
![uml](/referencias/uml-geoambiental-actual.svg)

### Estado deseado
![uml](/referencias/uml-geoambiental-deseado.svg)
