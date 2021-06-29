import argparse
import os

from page_loader.engine import download


def main():
    parser = argparse.ArgumentParser(description='page-loader')
    parser.add_argument('url', type=str)
    parser.add_argument('-o', '--output', help='set path for output', type=str,
                        default=os.getcwd())
    args = parser.parse_args()
    print(download(args.url, args.output))


if __name__ == '__main__':
    main()
