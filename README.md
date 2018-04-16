# CAL
All relevant files

This project is based on the NER tagger by Stanford which is licensed under the GNU General Public License. Further information can be found here: https://nlp.stanford.edu/software/CRF-NER.html

train.txt: The tokenized training file RI Heft 14 which was tagged manually
TrainDocXYZ: Where XYZ can be substituted by LOC, PERS, TIT. These files are created by the script Split_Tags.py
output_XYZ: Where XYZ can be substituted by LOC, PERS, TIT. These files were created by using the corresponding model out of the models folder.
outputMerged: This file is created by the script Merge_Tags.py out of the output_XYZ files. This is the final file, that contains all three labels, on column for each label
