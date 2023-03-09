# To-Do App



Functional specifications (FS) are a detailed description of the functions, features, and capabilities of a software system. They define how the system will behave in different scenarios, what inputs it will accept, and what outputs it will produce.
The to-do app software will have the following functional specifications:
1.	## User Account Creation:
 The app should allow users to create an account by providing their email address and a password. The user can log in to the app using the registered email and password.
2.	## Task Creation: 
The app should allow users to create tasks by providing the task name, description, date, time, and reminder interval. The user can create tasks for any day or week.
3.	## Task Management:
 The user should be able to view their tasks in a list or calendar view. They can mark a task as complete when they finish it. The app should show the completed tasks as completed and the remaining tasks as pending. If a task is not completed by the expected date and time, the app should mark it as skipped.
4.	## Reminder Notification: 
The app should send a reminder notification to the user's registered email address according to the reminder interval specified by the user. The email should contain the task name, description, and a link to the task.
5.	## Task Deletion:
 The user should be able to delete a task at any time.
6.	## Data Retention: 
The app should not store the user's tasks for more than seven days. After seven days, the app should automatically delete the task data from the database.



Technological specifications are a detailed description of the technical requirements, capabilities, and constraints of a software system. These specifications define the technology and infrastructure required to develop, deploy, and maintain the system.
The to-do app software will have the following technological specifications:
1.	## Platform: 
The app will be a web application accessible through a web browser.
2.	## Programming Language: 
The app will be developed using a combination of programming languages such as HTML, CSS, JavaScript, and Python(Django).
3.	## Database: 
The app will use a MySQL database to store user data, such as user accounts and task data.
4.	## Front-end:
 The app's front-end will be developed using HTML and CSS, and JavaScript will be used for dynamic functionality.
5.	## Back-end: 
The app's back-end will be developed using Django and will handle user authentication, task creation, task deletion, and database management.
6.	## Email Notification: 
The app will use an email service provider such as SendGrid to send reminder emails to the user.
7.	## Deployment: 
The app will be deployed on Railway hosting
