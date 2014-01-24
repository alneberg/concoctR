#!/usr/bin/env python
from nose.tools import assert_equal, assert_true, assert_almost_equal
from os.path import isdir,isfile
from os import listdir
import os
import sys
import subprocess

from concoctr.concoctr import ConcoctParams

file_path = os.path.realpath(__file__)

class TestConcoctParams(object):
    def setup(self):
        self.comp = "mock_comp"
        self.cov = "mock_coverage"
        self.base_args = ['--composition_file',"mock_comp",
                          "--coverage_file", "mock_coverage"]

    def test_expand(self):
        empty_p = ConcoctParams(self.comp, self.cov)
        assert_equal(empty_p.args(), self.base_args)

        only_k_p = ConcoctParams(self.comp, self.cov, kmer_length = 4)
        assert_equal(only_k_p.args(), self.base_args + ['--kmer_length', '4'])

        except_k_p = ConcoctParams(self.comp,
                                   self.cov,
                                   total_percentage_pca = 80,
                                   length_threshold = 100,
                                   covariance_type = 'full',
                                   basename = '/home/tmp_result/',
                                   )
        assert_equal(except_k_p.args(), self.base_args +
                     ['--total_percentage_pca', '80',
                      '--length_threshold', '100',
                      '--covariance_type', 'full',
                      '--basename', '/home/tmp_result/'])


        only_cov_p = ConcoctParams(self.comp,
                                   self.cov,
                                   covariance_type = 'full')
        assert_equal(only_cov_p.args(),
                     self.base_args +
                     ['--covariance_type', 'full'])
        all_p =  ConcoctParams(self.comp,
                               self.cov,
                               kmer_length = 4,
                               total_percentage_pca= 80,
                               length_threshold = 100,
                               covariance_type = 'full',
                               basename = '/home/tmp_result/'
                               )

        assert_equal(all_p.args(),
                     self.base_args +
                     ['--kmer_length', '4',
                      '--total_percentage_pca', '80',
                      '--length_threshold', '100',
                      '--covariance_type', 'full',
                      '--basename', '/home/tmp_result/'])



