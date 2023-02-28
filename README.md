# Flask Api Template

The project's aim is to provide a functional and simple template
structure while following best practices for software architecture patterns for a Flask application.

## Project Archecture

    app 
    |- api 
        |- application
                |- data_service
        |- domain
                |- model
                |- repository
        |- infra
                |- v1
                |- exceptions
                |- routers
                |- schema
        | - presentation
                |- controller
                |- validators
    |- test
        |- Same structure above


## How to use ?

- Install Docker on your machine. 
- Clone the repository to your local machine. 
- Open the project directory in your terminal and run the command:
    
        docker-compose up --build

- Access the Swagger API documentation by opening your browser and visiting http://localhost:5000/api/v1. 
- Click on the description "Main API used to represent some data," and then click "Try it out."
- Test the different parameters and try to retrieve data. 
- To run unit tests, after building all containers, run the following command:

         docker exec service-api pytest


### Thank you !
Thank you for using our API. If you have any questions or feedback, please feel free to contact us.