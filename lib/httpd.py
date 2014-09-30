#!/usr/bin/python2.6
#coding=utf-8
#author lixp@500wan.com 
#edit 2014-09-10 15:17:11

import urllib
import urllib2
from logger import Log
logger = Log().getLog()

class Httpd(object):
    """实现http的相关请求"""

    @staticmethod
    def post(requrl, param, to=5):
        param = urllib.urlencode(param)
        data = None
        try:
            req = urllib2.Request(url=requrl, data=param) 
            res = urllib2.urlopen(url=req,timeout=to)
            data = res.read()
        except HTTPError, e:
            print "Error code: %d" % e.code
            logger.debug("Error code: %d" % e.code)
        except URLError, e:
            print "Error reason: %s" % e.reason
            logger.debug("Error reason: %s" % e.reason)
        finally:
            return data

    @staticmethod
    def get(requrl, param, to=5):
        param  = urllib.urlencode(param)
        requrl = requrl + '?' + param
        data = None
        try:
            req = urllib2.Request(requrl) 
            res = urllib2.urlopen(url=req,timeout=to)
            data = res.read()
        except urllib2.HTTPError, e:
            logger.debug("Error code: %d" % e.code)
        except urllib2.URLError, e:
            logger.debug("Error reason: %s" % e.reason)
        finally:
            return data
            
