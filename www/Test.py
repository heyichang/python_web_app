#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "He Yichang"

from . import orm
from .models import User, Blog, Comment
import asyncio
async def test():
    await orm.create_pool(user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await  u.save()

asyncio.run(test())