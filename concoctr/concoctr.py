import subprocess
from collections import OrderedDict

from logbook import Logger

class ConcoctParams(object):
    def __init__(self, composition_file=None,
                 coverage_file=None,
                 kmer_length=None, 
                 total_percentage_pca=None, 
                 length_threshold=None, 
                 covariance_type=None,
                 basename=None):
        self.composition_file = composition_file
        self.coverage_file = coverage_file
        self.kmer_length = kmer_length
        self.total_percentage_pca = total_percentage_pca
        self.length_threshold = length_threshold
        self.covariance_type = covariance_type
        self.basename = basename
        self.max_n_processors = 1

    @property
    def options(self):
        return OrderedDict([
                ('--composition_file', self.composition_file),
                ('--coverage_file', self.coverage_file),
                ('--kmer_length', self.kmer_length),
                ('--total_percentage_pca', self.total_percentage_pca),
                ('--length_threshold', self.length_threshold),
                ('--covariance_type', self.covariance_type),
                ('--basename', self.basename),
                ('-m', self.max_n_processors)])

    def args(self):
        cmd_l = []
        for k,v in self.options.iteritems():
            if v:
                cmd_l.append(str(k))
                cmd_l.append(str(v))
        return cmd_l

class ConcoctR(object):
    
    def __init__(self):
        self.log = Logger('ConcoctR')

    def run_concoct(self, concoct_params, drmaa_s=None, drmaa_jt=None, sbatch_script=None):
        """ drmaa_s is a drama session
        drmaa_jt is a drmaa job template """
        if drmaa_s:
            drmaa_jt.remoteCommand = "concoct " + " ".join(concoct_params.args())
            job_id = drmaa_s.runJob(drmaa_jt)
            self.log.info("Jobid {0} with command: {1}".format(
                    drmaa_jt.remoteCommand, job_id))
            return job_id
        else:
            if sbatch_script:
                subprocess.Popen(['sbatch', sbatch_script])
            else:
                cla = ['concoct'] + concoct_params.args()
                subprocess.Popen(cla)
                self.log.info("Command line call with command: {0}".format(cla))
                
            return None
    
    def generate_sbatch_script(self, concoct_params, sbatch_params, file_name):
       """ Generate a shell script that can be submitted with sbatch. """
       with open(file_name, 'w+') as f:
           f.write("#!/bin/bash" + '\n')
           for sp in sbatch_params:
               f.write("#SBATCH " + sp + '\n')
           command = " ".join(['concoct'] + concoct_params.args())
           f.write(command + '\n')
       
