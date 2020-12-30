# Welcome to MiREDiBase!

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

MiREDiBase (*miR*NA *Edi*ting Data*base*) is a catalog of known miRNA editing sites (*Adenosine-to-Inosine* and *Cytosine-to-Uracil*) and an online resource for functional prediction of miRNA editing. 

## How to run MiREDiBase on your local machine.
To try MiREDiBase out on your local machine, proceed as follows:

 1. Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).
 2. Download the MiREDiBase GitHub repository.
 3. Unzip the *data.zip* file.
 4. Create a directory called *mbdata*.
 5. Within the MiREDiBase directory, modify the **.env** file setting up the database *name*, *username*, and *password*.
 6. Open you *Command Prompt/Terminal* and go to the MiREDiBase directory.
 7. For the first run ever, exec the command `docker-compose -f docker-compose.yml up --build -d`. The command will create all the required Docker images and run the MiREDiBase application.
 8. Once the installation is complete, open your browser and type *[localhost:8080](localhost:8080)* to use the MiREDiBase web interface and *[localhost:9001/docs](localhost:9001/docs)* to try out the RESTful API.
 9. When you are done, from within the MiREDiBase directory exec the command `docker-compose -f docker-compose.yml down` to stop MiREDiBase.
 10. You can completely uninstall MiREDiBase by running the command `docker-compose rm` from within the MiREDiBase directory.

More information about MiREDiBase can be found at [link](https://ncrnaome.osumc.edu/miredibase/).

<hr />

### References
If you have used any of the project code, please cite the following preprint:

Gioacchino P. Marceca, Rosario Distefano, Luisa Tomasello, Alessandro Lagana’, Francesco Russo, Federica Calore, Giulia Romano, Marina Bagnoli, Pierluigi Gasparini, Alfredo Ferro, Mario Acunzo, Qin Ma, Carlo M. Croce, Giovanni Nigita. *MiREDiBase: a manually curated database of editing events in microRNAs*.
bioRxiv 2020.09.04.283689; doi: https://doi.org/10.1101/2020.09.04.283689 

