#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines unit tests for :mod:`colour.io.iestm2714` module.
"""

from __future__ import division, unicode_literals

import os
import shutil
import sys

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest
import tempfile

from colour.io.ies_tm2714 import IES_TM2714_Header, IES_TM2714_Spd

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2008 - 2014 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['RESOURCES_DIRECTORY']

RESOURCES_DIRECTORY = os.path.join(os.path.dirname(__file__), 'resources')

FLUORESCENT_FILE_HEADER = {
    'Manufacturer': 'Unknown',
    'CatalogNumber': 'N/A',
    'Description': 'Rare earth fluorescent lamp',
    'DocumentCreator': 'byHeart Consultants',
    'Laboratory': 'N/A',
    'UniqueIdentifier': 'C3567553-C75B-4354-961E-35CEB9FEB42C',
    'ReportNumber': 'N/A',
    'ReportDate': 'N/A',
    'DocumentCreationDate': '2014-06-23',
    'Comments': 'Ambient temperature 25 degrees C.'}

FLUORESCENT_FILE_SPECTRAL_DESCRIPTION = {
    'SpectralQuantity': 'relative',
    'BandwidthFWHM': 2.0,
    'BandwidthCorrected': True}

FLUORESCENT_FILE_SPECTRAL_DATA = {
    400.0: 0.034,
    403.1: 0.037,
    405.5: 0.069,
    407.5: 0.037,
    420.6: 0.042,
    431.0: 0.049,
    433.7: 0.060,
    437.0: 0.357,
    438.9: 0.060,
    460.0: 0.068,
    477.0: 0.075,
    481.0: 0.085,
    488.2: 0.204,
    492.6: 0.166,
    501.7: 0.095,
    507.6: 0.078,
    517.6: 0.071,
    529.9: 0.076,
    535.4: 0.099,
    539.9: 0.423,
    543.2: 0.802,
    544.4: 0.713,
    547.2: 0.999,
    548.7: 0.573,
    550.2: 0.340,
    553.8: 0.208,
    557.3: 0.139,
    563.7: 0.129,
    574.8: 0.131,
    578.0: 0.198,
    579.2: 0.190,
    580.4: 0.205,
    584.8: 0.244,
    585.9: 0.236,
    587.5: 0.256,
    590.3: 0.180,
    593.5: 0.218,
    595.5: 0.159,
    597.0: 0.147,
    599.4: 0.170,
    602.2: 0.134,
    604.6: 0.121,
    607.4: 0.140,
    609.4: 0.229,
    610.2: 0.465,
    612.0: 0.952,
    614.6: 0.477,
    616.9: 0.208,
    618.5: 0.135,
    622.1: 0.150,
    625.6: 0.155,
    628.4: 0.134,
    631.2: 0.168,
    633.2: 0.087,
    635.6: 0.068,
    642.7: 0.058,
    648.7: 0.058,
    650.7: 0.074,
    652.6: 0.063,
    656.2: 0.053,
    657.0: 0.056,
    660.6: 0.049,
    662.6: 0.059,
    664.2: 0.048,
    686.0: 0.041,
    687.6: 0.048,
    689.2: 0.039,
    692.4: 0.038,
    693.5: 0.044,
    695.5: 0.034,
    702.3: 0.036,
    706.7: 0.042,
    707.1: 0.061,
    710.2: 0.061,
    711.0: 0.041,
    712.2: 0.052,
    714.2: 0.033,
    748.4: 0.034,
    757.9: 0.031,
    760.7: 0.039,
    763.9: 0.029,
    808.8: 0.029,
    810.7: 0.039,
    812.7: 0.030,
    850.1: 0.030}


class TestIES_TM2714_Header(unittest.TestCase):
    """
    Defines :class:`colour.io.iestm2714.IES_TM2714_Header` class unit tests
    methods.
    """

    def test_required_attributes(self):
        """
        Tests presence of required attributes.
        """

        required_attributes = ('mapping',
                               'manufacturer',
                               'catalog_number',
                               'description',
                               'document_creator',
                               'unique_identifier',
                               'measurement_equipment',
                               'laboratory',
                               'report_number',
                               'report_date',
                               'document_creation_date',
                               'comments')

        for attribute in required_attributes:
            self.assertIn(attribute, dir(IES_TM2714_Header))


class TestIES_TM2714_Spd(unittest.TestCase):
    """
    Defines :class:`colour.io.iestm2714.IES_TM2714_Spd` class unit tests
    methods.
    """

    def setUp(self):
        """
        Initialises common tests attributes.
        """

        self.__temporary_directory = tempfile.mkdtemp()

    def tearDown(self):
        """
        After tests actions.
        """

        shutil.rmtree(self.__temporary_directory)

    def test_required_attributes(self):
        """
        Tests presence of required attributes.
        """

        required_attributes = ('mapping',
                               'path',
                               'header',
                               'spectral_quantity',
                               'reflection_geometry',
                               'transmission_geometry',
                               'bandwidth_FWHM',
                               'bandwidth_corrected')

        for attribute in required_attributes:
            self.assertIn(attribute, dir(IES_TM2714_Spd))

    def test_required_methods(self):
        """
        Tests presence of required methods.
        """

        required_methods = ('read',)

        for method in required_methods:
            self.assertIn(method, dir(IES_TM2714_Spd))

    def test_read(self, spd=None):
        """
        Tests
        :attr:`colour.io.iestm2714.IES_TM2714_Spd.read` method.

        Parameters
        ----------
        spd : IES_TM2714_Spd, optional
            Optional IES TM-27-14 spectral power distribution for read tests.
        """

        if spd is None:
            spd = IES_TM2714_Spd(os.path.join(RESOURCES_DIRECTORY,
                                              'Fluorescent.spdx'))

        self.assertTrue(spd.read())
        self.assertDictEqual(spd.data, FLUORESCENT_FILE_SPECTRAL_DATA)

        for test, read in ((FLUORESCENT_FILE_HEADER, spd.header),
                           (FLUORESCENT_FILE_SPECTRAL_DESCRIPTION, spd)):
            for key, value in test.items():
                for specification in read.mapping.elements:
                    if key == specification.element:
                        self.assertEquals(
                            getattr(read, specification.attribute),
                            value)

    def test_write(self):
        """
        Tests
        :attr:`colour.io.iestm2714.IES_TM2714_Spd.write` method.
        """

        spd_r = IES_TM2714_Spd(
            os.path.join(RESOURCES_DIRECTORY, 'Fluorescent.spdx'))

        spd_r.read()

        spd_r.path = os.path.join(self.__temporary_directory,
                                  'Fluorescent.spdx')
        self.assertTrue(spd_r.write())
        spd_t = IES_TM2714_Spd(spd_r.path)

        self.test_read(spd_t)
        self.assertEquals(spd_r, spd_t)


if __name__ == '__main__':
    unittest.main()