# DiveFace

## A dataset to train unbiased and discrimination-aware face recognition algorithms ![alt text](http://atvs.ii.uam.es/atvs/pexels-photo-1282270.jpeg)


DiveFace contains annotations equally distributed among six classes related to gender and ethnicity (male, female and three ethnic groups). Gender and ethnicity have been annotated following a semi-automatic process. There are 24K identities (4K for class). The average number of images per identity is 5.5 with a minimum number of 3 for a total number of images greater than 150K. Users are grouped according to their gender (male or female) and three categories related with ethnic physical characteristics:

   - East Asian (Group 1): people with ancestral origin in Japan, China, Korea and other countries in that region.

   - Sub-Saharan and South Indian (Group 2): people with ancestral origins in Sub-Saharan Africa, India, Bangladesh, Bhutan, among others. 

   - Caucasian (Group3): people with ancestral origins from Europe, North-America and Latin-America (with European origin).
   
   
We are aware about the limitations of grouping all human ethnic origins into only 3 categories. According to studies, there are more than 5K ethnic groups in the world. We categorized according to only three groups in order to maximize differences among classes.  

Please cite [1] below if you make use of the dataset:

[1] A. Morales, J. Fierrez, R. Vera-Rodriguez. SensitiveNets: Learning Agnostic Representations with Application to Face Recognition. arXiv:1902.00334, 2019. [[pdf](https://arxiv.org/ftp/arxiv/papers/1902/1902.00334.pdf)]

## Download:

DiveFace files:  dowload "**txt**" files containing the annotations [[link](https://github.com/BiDAlab/DiveFace/tree/master/files)] and the script [[link](https://github.com/BiDAlab/DiveFace/blob/master/create_diveface.py)] to generate the database from Megaface dataset 

Downloading this dataset implies agreement to follow the same
conditions of non-commercial research for any modification and/or
re-distribution of the dataset in any form.

## How to use DiveFace:

1) Download Megaface training set (Tightly Cropped - Face detection box region only). Meface is property of the University of Washington. Please, read carefully the licence here: http://megaface.cs.washington.edu/dataset/download_training.html

2) Each DiveFace file contains 4K identities belonging to each of the six classes (number of images varies among identities). Annotations are included in the .txt files according to the following format: identity_folder_name/file_name 

3) Download create_diveface.py script and DiveFace files on the same directory.

4) To create DiveFace run the script:

   ``
      python3 create_diveface.py --mega <PATH_TO_MEGAFACE> --dive <PATH_TO_DIVEFACE> 
   ``
   
   This will create the full database. But if you want to have the balanced one (3 images per user) run the script with -b:
   
   ``
      python3 create_diveface.py --mega <PATH_TO_MEGAFACE> --dive <PATH_TO_DIVEFACE> -b
   ``

Additionally any entity using this dataset agrees to the following conditions:

THIS DATASET IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

### IMPORTANT: Meface dataset is not longer distributed by the University of Washington. We are leaveraging DiveFace images from the original dataset (Flickr 100M dataset). We will add the images soon. Authors are not responsible of the usage of the datataset. Nowadays, there are important concerns about the usage of public database to train face recognition technologies without explicit consent. We are aware of these concerns, and new regulations are expected to be more specific about these usages. 

## Contact:

For more information visit: https://sensitivenets.com/
or E-mail: aythami.morales@uam.es

