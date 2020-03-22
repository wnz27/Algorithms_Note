'''
@Author: 27
@LastEditors: 27
@Date: 2020-02-24 17:45:36
@LastEditTime: 2020-02-24 17:59:03
@FilePath: /Algorithms_Note/test/web/__init__.py
@description: type some description
'''
from .Blueprint import Blueprint
web = Blueprint()

from . import book
print(id(web))
from . import user


