#!/usr/bin/env python
# -*- coding:utf-8 -*-

import configparser


class HotelConf:

    def __init__(self):
        conf_file = '/home/zhu/git/ctrip/ctrip/conf/hotel.conf'
        config = configparser.ConfigParser()
        config.read(conf_file)

        self.hotel_info = self.get_db_conf(config['hotel_info'])

    @staticmethod
    def get_db_conf(section):
        conf = {'start_url': section.get('start_url')}
        return conf

