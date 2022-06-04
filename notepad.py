#!/usr/bin/env python
from app import App
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path", type=str,
                    help='path to the notes folder',
                    default='notes')

if __name__ == '__main__':
    args = parser.parse_args()

    app = App(file_path=args.path)

    app.run()
