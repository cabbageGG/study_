#!/bin/env python
# -*- coding:utf-8 -*-

class HtmlOutPuter(object):
    def __init__(self):
        self.datas = []

    def collect_data(self,url_data):
        if url_data is None:
            return 
        self.datas.append(url_data)

    def html_output(self):
        fout = open('out_html.html', 'w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')        
        fout.close()