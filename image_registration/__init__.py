"""
some description of what this package does.
"""
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
from .model.vertex import *
from .model.region import *
from .model.channels import *
from .model.image import *


class ImageRegistration(object):
    def __init__(self, config, nuclei_file):
        """
        a brief description goes here ...
        :param config:
        :type config:

        :param nuclei_file:
        :type nuclei_file:
        """
        self.regions = self._parse_config_xml(config)
        self.nuclei_image = self._read_nuclei_image(nuclei_file, self.regions, Channels.BLUE)

    def _parse_config_xml(self, config):
        """
        This parses xml regions
        :param config:
        :type config:

        :return: A list of model.Region
        """
        regions = []
        try:
            tree = ET.parse(config)
            root = tree.getroot()
            if root.tag != "Annotations":
                raise ParseError("Invalid root element `{}`!".format(root.tag))
            for et_annotation in root:
                if et_annotation.tag != "Annotation":
                    raise ParseError("Invalid child tag `{}`!".format(et_annotation.tag))
                et_regions = et_annotation.findall("Regions")
                if len(et_regions) != 1:
                    raise ParseError("Expect exactly one `Regions` element per `Annotation` element, found `{}` "
                                     "elements.".format(len(et_regions)))
                regions_count = len(et_regions[0].findall("Region"))
                if regions_count % 2 != 0:
                    raise ParseError("Expect even number of regions per each Region element, found `{}` "
                                     "elements".format(regions_count))
                parsed_regions = 0
                for et_region in et_regions[0].findall("Region"):
                    et_vertices = et_region.findall("Vertices")
                    if len(et_vertices) != 1:
                        raise ParseError("Expect exactly one `Vertices` element per `Region` element, found `{}` "
                                         "elements.".format(len(et_vertices)))
                    vertices = []
                    for vertex in et_vertices[0]:
                        z = None
                        for item in vertex.items():
                            if item[0].lower() == "x":
                                x = item[1]
                            if item[0].lower() == "y":
                                y = item[1]
                            if item[0].lower() == "z":
                                z = item[1]
                        try:
                            vertices.append(Vertex(x, y, z))
                        except NameError:
                            raise ParseError("The vertex `{}` does not have X and/or Y coordinate(s)".format(vertex.items()))
                    parsed_regions += 1
                    if parsed_regions > regions_count / 2:
                        # add bounding regions
                        regions[parsed_regions - (regions_count / 2) - 1].set_bounding_region(vertices)
                    else:
                        # add regions
                        region = Region(et_region.get("Id"))
                        region.set_region(vertices)
                        regions.append(region)
            return regions
        except ImportError:
            raise
        except ParseError as e:
            raise ParseError("Invalid configuration at `{}`: {} -- unable to continue.".format(config, e.message))

    def _read_nuclei_image(self, image_file, regions, channel):
        """

        :param image_file:
        :type image_file:

        :param regions:
        :type regions:

        :param channel:
        :type channel: model.Channels

        :return: nuclei image
        :type: model.Image
        """
        image = Image(regions=regions)
        # TODO: read the nuclei image with given regions and channel, then return it.
        return image

    def analyze(self, image_file, channel):
        """
        function description goes here ...
        :param image_file: what is an image file ? marker ?
        :type image_file: what is the type, e.g., string ? File?

        :param channel: what is a channel ?
        :type channel: model.Channels

        :return: what does this function return ?
        """
        print "another thing"
