#!/usr/bin/env python3
import requests

def main():
    r = requests.get('http://api.open-notify.org/astros.json')

    print(f"People in space: {r.json()['number']}")
    for astros in r.json()['people']:
        print(f"{astros['name']} on the {astros['craft']}")
main()

