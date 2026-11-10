import argparse

from src.data.sonar import sonar_to_pointcloud
from src.models.uwnet import SonarFusionBlock


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='configs/icra.yaml')
    args = parser.parse_args()
    model = SonarFusionBlock(64)
    print('training fusion model with', args.config)


if __name__ == '__main__':
    main()
