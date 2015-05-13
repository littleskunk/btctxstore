#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from btctxstore.api import BtcTxStore


_api = BtcTxStore()


write = _api.write
write_bin = _api.write_bin

read = _api.read
read_bin = _api.read_bin

