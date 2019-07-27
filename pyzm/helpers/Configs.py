"""
Module Configs
=================
Hold all ZM Config data. No need for a separate config class
"""


from pyzm.helpers.Base import Base

import requests

class Configs(Base):
    def __init__(self,logger=None, api=None):
        Base.__init__(self, logger)
        self.api = api
        self._load()

    def _load(self,options={}):
        self.logger.Debug(1,'Retrieving config via API')
        url = self.api.api_url +'/configs.json'
        r = self.api.make_request(url=url)
        self.configs = r.get('configs')

    def list(self):
        return self.configs

    
    def find(self, id=None, name=None):
        if not id and not name:
            return None
        match = None
        if id:
            key = 'Id'
        else:
            key = 'Name'
    
        for config in self.configs:
            if id and config['Config']['Id'] == id:
                match = config
                break
            if name and config['Config']['Name'].lower() == name.lower():
                match = config
                break
        return {
            'id': int(match['Config']['Id']),
            'name': match['Config']['Name'],
            'value': match['Config']['Value'],
        }
    
    def set(self, name=None, val=None):
        if not val:
            return
        if not name:
            return
        url = self.api.api_url + '/configs/edit/{}.json'.format(name)
        data = {'Config[Value]':val}
        return self.api.make_request(url=url, payload=data, type='put')
        
        


    
