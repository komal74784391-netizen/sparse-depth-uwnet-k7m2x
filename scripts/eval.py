import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--checkpoint', required=True)
    args = parser.parse_args()
    print('evaluating', args.checkpoint)


if __name__ == '__main__':
    main()
