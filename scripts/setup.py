# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe

setup(name="zonaFresnel", 
 version="1.0", 
 description="Breve descripcion", 
 author="sergio2021", 
 author_email="infosergio2021@gmail.com", 
 url="jaja.com", 
 license="free", 
 scripts=["shanon.py"], 
 console=["shanon.py"], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)