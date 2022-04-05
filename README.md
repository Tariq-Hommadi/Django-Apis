# Elham-s-Task`

> You can use postman to implement the following requests

> The Apis in App folder (view)

> 1- admin api, enduser apis all imlemented

> 2- for admin api **(Api/admin)** there is post and get, post to add new task for each user and get to filter the tasks you can send the request as follow:

POST:
{
    "userID": 5,
    "task": "write what is the task",
    "dueDate": "2022-10-10",
    "status": "pending"

}

GET:
{
    "userID": 5,
    "status": "pending"

}



> 3- **(Api/user/List)** API to list all his/her tasks as send request as follow:

GET:
{
    "userID": 5,

}

> 4- **(Api/user/comleteTask)** API to complete a task, send a request as follow:

PUT:
{
    "Id": 5,  //for task id, remove this comment when test it.
    "status": "Completed" //change the status of a task, remove this comment when test it.

}

> 5- **(Api/user/userFilter)** Api/user/userFilter, send request as follow:

GET:
{
    "userID": 5,
    "status": "Completed"

}


> 6- Dockerfile is implemented along with the needed requirements.
