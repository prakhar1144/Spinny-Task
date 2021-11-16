## API Service for CRUD 

  #### Credentials for Testing

  permission | username | password
  -----------|----------|----------
  Admin      |  admin   | admin@14
  Staff      |  user2   | spinny@14
  Normal User|  user1   | spinny@14

* Task 0

  > [Data Modeling]()


* Task 1 

  ```
  Add API

  POST /create/
  ```
* Task 2

  ```
  Update API
  
  
  ```
* Task 3

  ```
  List All - API
  
  GET /list/
  ```
  * Filters example url : 
    * /list/?length__lt=5
    * /list/?length__gt=5

    * /list/?breadth__lt=5
    * /list/?breadth__gt=5

    * /list/?height__lt=5
    * /list/?height__gt=5

    * /list/?area__lt=5
    * /list/?area__gt=5

    * /list/?volume__lt=5
    * /list/?volume__gt=5

    * /list/?creator=1

    * /list/?created_at__lt=2021-11-16
    * /list/?created_at__gt=2021-11-16

* Task 4

  ```
  List My Boxes - API
  
  GET /my-boxes/
  ```
  * Filters example url :
    > Filters canbe used in a similar way as Task 3
    
    > Example : /my-boxes/?length__lt=5
 
* Task 5

  ```
  Delete - API
  
  DELETE /delete/1
  ```
