# gff-phylocsf-human
Use the scripts here to summarize PhyloCSF scores for GFF files of human genomic regions. This script is based on Devon Ryan's pyBigWig library that lets you access bigWig (bw) files remotely, and on bw files provided by the Broad Institute and the UCSC Genome Browser.

## Usage

You have to install the pyBigWig library by, for example, BioConda.

`conda install -c bioconda pybigwig`

You may want to do it in a conda virtual environment. If the above does not work, please refer to [pyBigWig's GitHub page](https://github.com/dpryan79/pyBigWig).

Then, you can score entries in a GFF file with a command like this (using the example file provided in this repository):

`python extract_phylocsf.py A431_novel_peptides.2017.gff3 > A431_phyloCSF.txt`

The script will take a while to run, but it prints output that hopefully gives an idea about how long it will take.

## Details

PhyloCSF scores are provided in six reading frames (+0, +1, +2, -0, -1, -2). There is a different bigWig file for each reading frame, so the script opens one of those at a time and queries each bw file with each genomic region. The pyBigWig.stats() function will return the mean PhyloCSF score for the region. We simply take a mean value above zero to mean that there is coding potential, and a negative value means there isn't. Previously, we used a slightly (only slightly) more detailed way of looking at the scores where we compared the number of positively scored bases in an interval with the number of negatively scored ones, and called the region coding if the number of positively scored bases was larger. You might want to use a different definition. 
