# Welcome to MiREDiBase!

MiREDiBase (*miR*NA *Edi*ting Data*base*) is a catalog of known miRNA editing sites (*Adenosine-to-Inosine* and *Cytosine-to-Uracil*) and an online resource for functional prediction of miRNA editing. 

## How to run MiREDiBase on your local machine.
To try MiREDiBase out on your local machine, proceed as follows:

 1. Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).
 2. Download the MiREDiBase GitHub repository.
 3. Unzip the *data.zip* file.
 4. Within the MiREDiBase directory, modify the **.env** file setting up the database *name*, *username*, and *password*.
 5. Open you *Command Prompt/Terminal*.
 6. For the first run, exec the command `docker-compose -f docker-compose.yml up --build -d`. The command will create all the required Docker images and run the MiREDiBase application.
 7. Once the installation is complete, open your browser and type *[localhost:8080](localhost:8080)* to use the MiREDiBase web interface and *[localhost:9001/docs](localhost:9001/docs)* to try out the RESTful API.
 8. When you are done, from within the MiREDiBase directory exec the command `docker-compose -f docker-compose.yml down` to stop MiREDiBase. executing the command `docker-compose -f docker-compose-prod.yml up -d`.
 9. You can completely uninstall MiREDiBase by running the command `docker-compose rm` from within the MiREDiBase directory.

More information about MiREDiBase can be found at [link](https://ncrnaome.osumc.edu/miredibase/).

