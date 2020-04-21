#!/usr/bin/python

import json, requests, fire
from prettytable import PrettyTable

wpvulndb_curl_headers = {'Authorization': 'Token token=api-token'} 

class Vulnerability(object):

    def show(self, vuln_id):
        wpvulndb_api_endpoint = 'https://wpvulndb.com/api/v3/vulnerabilities/{0}'.format(vuln_id)
        vulnerability_report = requests.get(wpvulndb_api_endpoint, headers=wpvulndb_curl_headers).json()
        # register title
        _vuln_title = vulnerability_report["title"]
        # register vulnerability name
        for vuln_info in vulnerability_report["plugins"]:
            _vuln_name = vuln_info
        # register 'fixed in version'
        _vuln_fixed_in = vulnerability_report["plugins"][_vuln_name]["fixed_in"]
        if _vuln_fixed_in is None:
            _vuln_fixed_in = "N/A"
        
        info_string = "Title:\t{0}\nName:\t{1}\nFixed in version:\t{2}".format(_vuln_title, _vuln_name, _vuln_fixed_in)
        print(info_string)


    def list_latest(self, themes=0, plugins=0, wordpress=0):
        # fetch latest theme vulnerabilities
        pass

class Pipeline(object):

    def __init__(self):
        self.vulnerability = Vulnerability()

if __name__ == "__main__":
    fire.Fire(Pipeline)

