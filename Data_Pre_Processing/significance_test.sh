#!/usr/bin/env bash


 python significance_test.py --ppm_path 'PPMI_model/1809_1970_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_1809_1970_fastext_5_300_5.bin' --vocab_path 'PPMI_model/1809_1970_vocab.bin' --threshold 10000

python significance_test.py --ppm_path 'PPMI_model/1971_1980_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_1971_1980_fastext_5_300_5.bin' --vocab_path 'PPMI_model/1971_1980_vocab.bin' --threshold 10000

python significance_test.py --ppm_path 'PPMI_model/1981_1990_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_1981_1990_fastext_5_300_5.bin' --vocab_path 'PPMI_model/1981_1990_vocab.bin' --threshold 10000

python significance_test.py --ppm_path 'PPMI_model/1991_2000_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_1991_2000_fastext_5_300_5.bin' --vocab_path 'PPMI_model/1991_2000_vocab.bin' --threshold 10000

python significance_test.py --ppm_path 'PPMI_model/2001_2010_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_2001_2010_fastext_5_300_5.bin' --vocab_path 'PPMI_model/2001_2010_vocab.bin' --threshold 10000

python significance_test.py --ppm_path 'PPMI_model/2011_2015_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_2011_2015_fastext_5_300_5.bin' --vocab_path 'PPMI_model/2011_2015_vocab.bin' --threshold 10000
python significance_test.py --ppm_path 'PPMI_model/2011_2015_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_2011_2015_fastext_5_300_5.bin' --vocab_path 'PPMI_model/2011_2015_vocab.bin' --threshold 5000






 python significance_test.py --ppm_path 'PPMI_model/1809_1970_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_1809_1970_fastext_5_300_5.bin' --vocab_path 'PPMI_model/1809_1970_vocab.bin' --threshold 10000 --neigbours 50

python significance_test.py --ppm_path 'PPMI_model/1971_1980_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_1971_1980_fastext_5_300_5.bin' --vocab_path 'PPMI_model/1971_1980_vocab.bin' --threshold 10000 --neigbours 50

python significance_test.py --ppm_path 'PPMI_model/1981_1990_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_1981_1990_fastext_5_300_5.bin' --vocab_path 'PPMI_model/1981_1990_vocab.bin' --threshold 10000 --neigbours 50

python significance_test.py --ppm_path 'PPMI_model/1991_2000_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_1991_2000_fastext_5_300_5.bin' --vocab_path 'PPMI_model/1991_2000_vocab.bin' --threshold 10000 --neigbours 50

python significance_test.py --ppm_path 'PPMI_model/2001_2010_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_2001_2010_fastext_5_300_5.bin' --vocab_path 'PPMI_model/2001_2010_vocab.bin' --threshold 10000 --neigbours 50

python significance_test.py --ppm_path 'PPMI_model/2011_2015_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_2011_2015_fastext_5_300_5.bin' --vocab_path 'PPMI_model/2011_2015_vocab.bin' --threshold 10000 --neigbours 50

python significance_test.py --ppm_path 'PPMI_model/2011_2015_explicit_ppmi.bin' \
--sgns_path 'SGNS_trained_model/u_2011_2015_fastext_5_300_5.bin' --vocab_path 'PPMI_model/2011_2015_vocab.bin' --threshold 5000 --neigbours 50