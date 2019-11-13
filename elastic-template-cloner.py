import argparse
import json
import urllib2
from pipenv.vendor import requests


class TemplateCloner:
    def __init__(self, args):
        self.args = args

    def upload(self):
        for template_name in self.args.templates:
            contents = urllib2.urlopen(self.args.origin + "/_template/" + template_name).read()
            aliases = json.loads(contents)
            data = json.dumps(aliases[template_name])
            headers = {"content-type": "application/json"}
            requests.request('PUT', self.args.destination + "/_template/" + self.args.prefix + template_name, headers=headers, data=data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--origin", dest="origin", help="origin url (http://origin:9200)",required=True)
    parser.add_argument("-d", "--destination", dest="destination", help="destination url (http://destination:9200)",required=True)
    parser.add_argument("-p", "--prefix", dest="prefix", help="prefix to append to new templates", default="")
    parser.add_argument("-t", "--templates", nargs='+', dest="templates", help="space separated list of templates (e.g. templateA templateB ...)", required=True)

    args = parser.parse_args()
    uploader = TemplateCloner(args)
    uploader.upload()

main()
