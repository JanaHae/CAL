# CAL
A student project at Technische Universität Darmstadt

This project is based on the NER tagger by Stanford which is licensed under the GNU General Public License. Further information can be found here: https://nlp.stanford.edu/software/CRF-NER.html

Folder NER Tagger
train.txt: The tokenized training file RI Heft 14 which was tagged manually.
TrainDocXYZ: Where XYZ can be substituted by LOC, PERS, TIT. These files are created by the script Split_Tags.py.
output_XYZ: Where XYZ can be substituted by LOC, PERS, TIT. These files were created by using the corresponding model out of the models folder.
outputMerged: This file is created by the script Merge_Tags.py out of the output_XYZ files. This is the final file, that contains all three labels, on column for each label.
properties_training.prop: Specifies all properties for learning the model. Has to be adapted to the corresponding entity class.

Folder tex
This folder contains all relevant files for building the .pdf document such as the the tex-file, the bib-file and the images.