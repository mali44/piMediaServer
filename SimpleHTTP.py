#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
from os.path import basename

import sys
import StatusFunctions
import json, time,requests
import urllib2,threading


class MainHandler(BaseHTTPRequestHandler):

    def _set_headers(self, content_type="text/html"):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        self._set_headers("application/json")

        if self.path == "/systemStatus":
            print (StatusFunctions.StatusFunc())
            self.wfile.write((StatusFunctions.StatusFunc()))



    def do_POST(self):
        print self.rfile
        self._set_headers()
        bosAlan=StatusFunctions.hddInfo()['Kullanilmayan']
        print bosAlan


        if self.path == '/downloadFile':

            a=self.rfile.read(int(self.headers['Content-Length']))
            post_parameters = parse_qs(a)
            key=post_parameters.keys()


            url= post_parameters['tester']
            print url
            self.wfile.write(json.dumps(post_parameters))

            url=''.join(url)
            print url
            print ("Indirme Baslatiliyor...")
            if bosAlan < 952:
                print "Yetersiz Disk !"
                print "Kalan Bos Alan: "+ StatusFunctions.humanReadable()["bosAlan"]

            else:


                self.download(url)




    def download(self,urls):

        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}

        req = urllib2.Request(urls, headers=hdr)

        try:
            u = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print e.fp.read()
        filmadi=basename(urls)

        f = open(filmadi,'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Indiriliyor: %s Bytes: %s " %(filmadi,file_size)
        file_size_dl=0
        block_size=8192
        while True:
            buffer = u.read(block_size)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8) * (len(status) + 1)
            sys.stdout.write(status)
            sys.stdout.flush()
            self.wfile.write(status)
        f.close()
        print "indirme islemi bittti"




    def progressBar(self,deger):





def run(server_class=HTTPServer, handler_class=MainHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print '[%s] Listener Started' % time.strftime("%H:%M:%S")
    httpd.serve_forever()


if __name__ == "__main__":
    run(HTTPServer, MainHandler, 1025)
