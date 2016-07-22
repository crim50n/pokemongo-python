#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Usage:
# python example.py -lm area -am ptc -l 55.837513 37.388363 55.870527 37.461121 -u USER -p PASSWORD
# python example.py -lm google -am ptc -l Moscow Kremlin -u USER -p PASSWORD

import sys
import argparse
import time

from skiplagged import Skiplagged

def parseargs():
    argparser = argparse.ArgumentParser()
    argparser.add_argument (
                '-l',
                '--location',
                nargs='+',
                help='Location Google Maps understands',
                required=True
        )
    argparser.add_argument (
                '-u',
                '--user',
                #nargs='+',
                help='Pokemon Trainer Club User',
                required=True
        )

    argparser.add_argument (
                '-p',
                '--password',
                #nargs='+',
                help='Pokemon Trainer Club Password',
                required=True
        )

    argparser.add_argument (
                '-am',
                '--auth-method',
                #nargs='+',
                help='Authentication method, specify google or ptc',
                required=True,
                dest='auth_method',
                choices=['google', 'ptc'],
                default=['ptc']
        )
    argparser.add_argument (
                '-lm',
                '--location-method',
                #nargs='+',
                help='Location method, specify area or google',
                required=True,
                dest='location_method',
                choices=['google', 'area'],
                default=['google']
        )
 
    command = argparser.parse_args(namespace=FindPokemon())

    return command

class FindPokemon(argparse.Namespace):
    def __init__(self, **kwargs):
        self.user = None
        self.password = None
        self.location = None
        self.auth_method = None
        self.location_method = None
        
        super(FindPokemon, self).__init__(**kwargs)

    def run(self):
        client = Skiplagged()
        if self.location_method == 'area':
                    bounds = (
                            (float(self.location[0]), float(self.location[1])),
                            (float(self.location[2]), float(self.location[3]))
                            )
        elif self.location_method == 'google':
                    bounds = client.get_bounds_for_address(' '.join(self.location))
        while 1:
            try:
                print client.login_with_pokemon_trainer(self.user, self.password)
                # Log in with a Google or Pokemon Trainer Club account
                if self.auth_method == 'ptc':
                    print client.login_with_pokemon_trainer(self.user, self.password)
                elif self.auth_method == 'google':
                    print client.login_with_google(self.user, self.password)
        
                # Get specific Pokemon Go API endpoint
                print client.get_specific_api_endpoint()
        
                # Get profile
                print client.get_profile()
        
                # Find pokemon
                for pokemon in client.find_pokemon(bounds):
                    print pokemon
            except Exception as e:
                print('Unexpected error: {0}'.format(e))
                time.sleep(1)

def main():
    find_pokemon = parseargs()
    find_pokemon.run()


if __name__ == '__main__':
    main()