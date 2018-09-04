#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  doc-download-button.py
#

from __future__ import print_function
import re
from codecs import open
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import zlib
import sys
if sys.version_info[0] >= 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen

print('INFO    -  Fetching docs inventory...')
inv_lines = urlopen('http://pvgeo.readthedocs.io/en/latest/objects.inv').read().split(b'\n')
inv = [ln for ln in inv_lines if b'#' not in ln[0:1]]
raw_inv = zlib.decompress(b'\n'.join(inv))

def produceURL(att):
    return 'http://docs.pvgeo.org/en/latest/%s' % att[3].replace('$', att[0])

LOOKUP = dict()
for line in raw_inv.splitlines():
    att = line.decode('utf-8').split()
    LOOKUP[att[0]] = produceURL(att)

DLBTN_SYNTAX = re.compile(r'\{btn:\s*(.+?)\s*\}')
LOOKUP_SYNTAX = re.compile(r'\{lookup:\s*(.+?)\s*\}')

class PVGeoExtension(Extension):
    def __init__(self, configs={}):
        self.config = {
            'base_path': ['.', 'Default location from which to evaluate ' \
                'relative paths for the include statement.'],
            'encoding': ['utf-8', 'Encoding of the files used by the include ' \
                'statement.']
        }
        for key, value in configs.items():
            self.setConfig(key, value)

    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add(
            'include', PVGeoExtensionPreprocessor(md,self.getConfigs()),'_begin'
        )


class PVGeoExtensionPreprocessor(Preprocessor):
    '''This includes an ability to make a download button'''
    def __init__(self, md, config):
        super(PVGeoExtensionPreprocessor, self).__init__(md)
        self.base_path = config['base_path']
        self.encoding = config['encoding']

    def _genlink(self, name):
        try:
            return ["[**Take a look at `%s`'s code docs here**](%s)" % (name.split('.')[-1], LOOKUP[name])]
        except KeyError:
            print('%s: not found in docs inventory' % name)
            return ['']

    def _genButton(self, link, width=r'width:100%'):
        return ['''<a href="%s"><button class="btn" style="%s"><i class="fa fa-download"></i> Download</button></a>''' % (link, width)]

    def run(self, lines):
        done = False
        while not done:
            for line in lines:
                loc = lines.index(line)
                m = DLBTN_SYNTAX.search(line)
                loo = LOOKUP_SYNTAX.search(line)
                if loo:
                    text = self._genlink(loo.group(1))
                    line_split = LOOKUP_SYNTAX.split(line,maxsplit=0)
                    if len(text) == 0: text.append('')
                    #text = ['File Included From: %s' % filename] + text
                    text[0] = line_split[0] + text[0]
                    text[-1] = text[-1] + line_split[2]
                    lines = lines[:loc] + text + lines[loc+1:]
                    break
                elif m:
                    text = self._genButton(m.group(1))
                    line_split = DLBTN_SYNTAX.split(line,maxsplit=0)
                    if len(text) == 0: text.append('')
                    #text = ['File Included From: %s' % filename] + text
                    text[0] = line_split[0] + text[0]
                    text[-1] = text[-1] + line_split[2]
                    lines = lines[:loc] + text + lines[loc+1:]
                    break
            else:
                done = True
        return lines


def makeExtension(*args,**kwargs):
    return PVGeoExtension(kwargs)
