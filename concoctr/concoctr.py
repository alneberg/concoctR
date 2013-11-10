import subprocess
from collections import OrderedDict

class ConcoctParams(object):
    def __init__(self, composition_file=None,
                 coverage_file=None,
                 kmer_length=None, 
                 total_percentage_pca=None, 
                 length_threshold=None, 
                 covariance_type=None):
        self.composition_file = composition_file
        self.coverage_file = coverage_file
        self.kmer_length = kmer_length
        self.total_percentage_pca = total_percentage_pca
        self.length_threshold = length_threshold
        self.covariance_type = covariance_type

    @property
    def options(self):å
        return OrderedDict([('--composition_file', self.composition_file),
                ('--coverage_file', self.coverage_file),
                ('--kmer_length', self.kmer_length),
                ('--total_percentage_pca', self.total_percentage_pca),
                ('--length_threshold', self.length_threshold),
                ('--covariance_type', self.covariance_type)])

    def args(self):
        cmd_l = []
        for k,v in self.options.iteritems():
            if v:
                cmd_l.append(str(k))
                cmd_l.append(str(v))
        return cmd_l

class ConcoctR(object):
    
    def __init__(self):
        pass

    def run_concoct(self, concoct_params, drmaa_s=None, drmaa_jt=None):
        """ drmaa_s is a drama session
        drmaa_jt is a drmaa job template """
        if drmaa_s:
            raise NotImplementedError
        else:
            subprocess.Popen(['CONCOCT'] + concoct_params.args())

