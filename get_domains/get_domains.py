#Get all Domains
import sys
import os
sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils
import pprint

class GetDomains:
    def __init__(self):
        print('View Domains')
        self.utils = Utils(sys.argv)
        self.hostname = sys.argv[1]

    def get_domains(self):
        url = 'https://'+self.hostname+'/v1/domains'
        response = self.utils.get_request(url)
        pprint.pprint(response)
        
if __name__== "__main__":
    GetDomains().get_domains()
