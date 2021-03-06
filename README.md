# IPP

## Plataforma web del Índice de Precios Popular


Esta plataforma se utiliza para el relevamiento y procesamiento de datos del IPP, a partir de los cuales se realizan informes periódicos, accesibles desde el sitio web del [Instituto de Economía Popular](http://indep.libre.social/category/informes-estadisticos/) (IndEP)


## Instalación

_Suponemos que se está utilizando sistema operativo GNU/Linux. En otro sistema algún comando puede variar o no estar disponible._


Para instalar la plataforma, se debe crear un entorno virtual:
```
virtualenv ipp_workenv
```

Activar el entorno recién creado:
```
source ipp_workenv/bin/activate
```

Instalar los requerimientos:
```
pip install -r https://raw.githubusercontent.com/nicoechaniz/IPP/master/requirements.txt
```

Y clonar este repositorio:
```
git clone https://github.com/nicoechaniz/IPP.git
```

Si vas a correr los tests, debes instalar PhantomJS manualmente o con el gestor de paquetes de tu distribuciòn, ejemplos:

- Archlinux:

```
sudo pacman -S phantomjs
```

- Debian o Ubuntu:
(guía completa: https://gist.github.com/julionc/7476620)

_En el ejemplo se descarga phantomjs en /opt/, pero puede ser en cualquier ubicación._

```
cd /opt/
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar xvfj phantomjs-2.1.1-linux-x86_64.tar.bz2
ln -s /opt/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/
```

Si todo fue bien, deberíamos poder correr los tests sin errores:
```
IPP/manage.py test bdd --behave_lang es

```

Si está FireFox instalado, podemos correr los tests en el navegador con:
```
IPP/manage.py test bdd --behave_lang es --behave_browser firefox
```

## Documentación

La [guía de uso de la plataforma](http://indep.libre.social/document/instructivo-plataforma-ipp/) se publica en el sitio web del IndEP.
