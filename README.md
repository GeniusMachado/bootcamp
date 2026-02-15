before you do anything mnake sure you have cloned the github repostiory correctly and then make sure to have the corrrect .env file created with from the boiler plate which is the .env.example file and then add your desired admin login credentials and also the password and then make sure everything is setup correctly becuase we are going to have to run it now through the uv package manager. Because I like it as it is faster and lightweight in comparison to Pip which is the alternative to python package managers.
After that I want to tell you that you make sure that you run this first command as this will initialize and sync your repository and makes sure to download and install all the dependencies on your local system inorder to run the application that are required for it: 





1) 
uv sync



The commands you need to run this application by first building it in docker and then running it. 





1) Build the docker images from your source code and tag it with the name hiring-bot:
So the terminal command to build it is with adding a tag to it. This command will actually build the image of the container in the current directory and then you will have to just run this build into a container. 



docker build -t hiring-bot .






2) Running the image you just built :

And then you just run the app that you built the image with the same tag as hiring bot. 
You are also mapping the docker container's volume to the current directory on your linux machine with the $(pwd):/app command and then we are making sure that the app runs on a different port my default port  is already in use on my system that holds my resume landing page and portfolio. Just make sure to use the --reload tag to check and listen for changes on the backend in any of the fastapi or uvicorn code. 




 docker run -p 8007:8007 -v $(pwd):/app hiring-bot uvicorn main:app --host 0.0.0.0 --port 8007 --reload 

