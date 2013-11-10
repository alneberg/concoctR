from concoctr.concoctr import ConcoctParams, ConcoctR
import os

file_dirname_path = os.path.dirname(__file__)
test_data_path = os.path.join(file_dirname_path,"..","tests","test_data")
composition = os.path.join(test_data_path,"composition.fa")
coverage = os.path.join(test_data_path, "coverage")

con_p = ConcoctParams(composition,
                      coverage,
                      kmer_length = 4,
                      total_percentage_pca= 80,
                      limit_kmer_count = 100,
                      covariance_type = 'full')

cr = ConcoctR()
cr.run_concoct(con_p)
