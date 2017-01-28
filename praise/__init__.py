from adjectives import adjectives
from adverbs import adverbs
from exclamations import exclamations
from smiley import smiley
from verbs import created
from verbs import creating
from pypackages import pypackages

import random

def getRandom(max):
    return random.randint(0,max-1)

def parse_template(template):
    adj_i=getRandom(len(adjectives))
    adv_i=getRandom(len(adverbs))
    exclaim_i=getRandom(len(exclamations))
    smiley_i=getRandom(len(smiley))
    created_i=getRandom(len(created))
    creating_i=getRandom(len(creating))
    pypackage_i=getRandom(len(pypackages))
    praise_string=template.replace('${adjective}',adjectives[adj_i])
    praise_string=praise_string.replace('${adverb}',adverbs[adv_i])
    praise_string=praise_string.replace('${exclamation}',exclamations[exclaim_i])
    praise_string=praise_string.replace('${smiley}',smiley[smiley_i])
    praise_string=praise_string.replace('${created}',created[created_i])
    praise_string=praise_string.replace('${creating}',creating[creating_i])
    praise_string=praise_string.replace('${package}',pypackages[pypackage_i])
    return praise_string

def help():
    print 'Please Use praise(template)'
    print 'templates is something like You are ${replacement}'
    print 'replacement could be adjective, adverb exclamation, smiley, created, creating, package'

def praise(template="You are ${adjective}!"):
    print parse_template(template)