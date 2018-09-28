import os
import argparse
from image_registration import *

"""
call syntax: python run.py CONFIG_FILE NUCLEI_FILE

CONFIG_FILE: is an xml file containing ...

NUCLEI_FILE: is a SVS file containing ...
"""

parser = argparse.ArgumentParser(description='Run ImageRegistration')
parser.add_argument('config')
parser.add_argument('nuclei_file')

args = parser.parse_args()

if __name__ == "__main__":
    config = args.config if args.config else 'tests/sample_data/config.xml'
    if os.path.isfile(config) is False:
        sys.exit("First argument is expected to be a valid configuration file; received `{}` instead. ".format(config))

    nuclei_file = args.nuclei_file if args.nuclei_file else 'tests/sample_data/sample_nuclei.svs'
    if os.path.isfile(config) is False:
        sys.exit("Second argument is expected to be a valid nuclei file; received `{}` instead. ".format(config))


    print("args: \n\t{}\n\t{}\n".format(config, nuclei_file))
    ir = ImageRegistration(config=config, nuclei_file=nuclei_file, has_bounding_boxes=True)

    for x in ir.regions:
        print("!! {}\n!! {}\n\n".format(x.roi, x.bounding_region))
