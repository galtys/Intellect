"""
Copyright (c) 2011, The MITRE Corporation.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. All advertising materials mentioning features or use of this software
   must display the following acknowledgement:
   This product includes software developed by the author.
4. Neither the name of the author nor the
   names of its contributors may be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

'''
Created on Aug 18, 2011

@author: Michael Joseph Walsh
'''

import logging, time

import thread, random
from threading import Lock

def grow_wool(sheep):
    while True:
        time.sleep(random.randint(2, 5))

        logging.getLogger("example").debug("{0}: adding some wool".format(sheep.name))
        sheep.bags_of_wool = sheep.bags_of_wool + 1

        if sheep.bags_of_wool == 3:
            logging.getLogger("example").debug("{0}: wait around for retirement".format(sheep.name))
            break

class BlackSheep():

    number = 0

    def __init__(self):
        '''
        BlackSheep Initializer
        '''
        self.bags_of_wool = 0
        BlackSheep.number = BlackSheep.number + 1
        self._name = "Sheep #{0}".format(BlackSheep.number)

        self.lock = Lock()
        thread.start_new_thread(grow_wool, (self,))


    @property
    def name(self):
        return self._name

    @property
    def bags_of_wool(self):
        value = self._bags_of_wool
        return value

    @bags_of_wool.setter
    def bags_of_wool(self, value):
        self.lock.acquire()
        self._bags_of_wool = value
        self.lock.release()
