# Project Overview

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Deploy on Heroku | Complete
|Day 1| Project Description | Complete
|Day 1| Wireframes / Priority Matrix / Timeline | Complete
|Day 2| Add Authentication User Model | Incomplete
|Day 3| Finish Models and build out remaining MVC/MVT architecture | Incomplete
|Day 3| Testing and Building Routes + Views | Incomplete
|Day 4| Connecting Front-End Views to Routes | Incomplete
|Day 5| MVP | Incomplete
|Day 6| Final Touches and Present



## Project Description
### Cloud Message

A simple messaging app to help connect you with other Cloud Message users. Post-MVP will visually model what a potential SoundCloud messaging app could look like.
        
User story:  
- Quinn is a musician that wants to connect with other artists.
- He can register an account with the Cloud Message app to have his login info saved.
- In order to access his inbox, he will input his registered account information into the login form on the landing page.
- Upon logging in, he will see the main inbox, with a list of messages received from senders and a preview of the messages last received or sent from that user.
- To access a conversation, the user can click on the individual conversation in the list and a new view with the conversation between the users will appear.
- A popup text field in the conversation view will either create or update the message from the user upon submission depending on the models used.
- A upper navbar giving the option to select profile settings or to log out of the account.
- A user settings modal that allows user to change their avatar or delete their account.

POST-MVP

- The user can delete conversations. (Models determined)
- An lower nav bar will give the option to compose a new message and pick a recipient from a drop down menu.
- Search user functionality.
- Utilize the SoundCloud API users endpoints to list actual users in a search function.


INSPIRATION:  
https://www.soundcloud.com


## App Build-out Links 
[Front-end deployed URL](https://cloud-msg.netlify.app/#/)

[Front-end GitHub Repo](https://github.com/studiosemantica/p4frontend/)

[Back-end deployed URL](https://p4-app.herokuapp.com/)

[Back-end GitHub Repo](https://github.com/studiosemantica/p4backend/)


## Wireframes

[Mobile]
- [Landing Page](https://res.cloudinary.com/dinqukx6a/image/upload/v1600182066/Signup_upfles.png)
- [Logged in, post view](https://res.cloudinary.com/dinqukx6a/image/upload/v1600182067/Mobile_Inbox___Conversations___Settings_m1fcvd.png)

[Tablet & Desktop]
- [Landing Page]()
- [Logged in, edit post view](https://res.cloudinary.com/dinqukx6a/image/upload/v1600182066/Desktop_wzbvhd.png)


Wireframing Resources:

- [MockFlow](https://www.mocflow.com/)


## Time/Priority Matrix 

[Time and Priority Matrix](https://res.cloudinary.com/dinqukx6a/image/upload/v1598235735/Project%203/Music_Journal_Front_EndTPM_isr7ab.jpg)

#### MVP


- Create JWT Authorized accounts for Multiple Users
- Models for API
- Views for API
- Serializers for App
- URLS/Routes for API / testing 
- Register Account Functionality
- Log In Functionality
- Make Create view : Register Account
- Make Read view: Display logged-in username & avatar in nav bar
- Make Read view: Display list of conversations with users
- Make Read view: Display messages for individual conversation
- Make Update view : User profile settings to update avatar, username or password
- Make Create/Update view : User can send message through text field to update message array for conversation
- Make Delete view : User can delete account
- Refactored to work with Vue
- Deployed on Heroku

#### PostMVP 

- Make Read view: Search list function for users.
- Make Read view/ fetch request: Implement user endpoints from SoundCloud's API.
- Make Create/Update view : User can send message by selecting user from populated list generated from search.
- Make delete view : Users can delete conversations or messages

## Functional Components
 
| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
Create JWT Authorized accounts for Multiple Users | H | 0hr | 0hr | 0hr|		
Models for API | H | 0hr | 0hr | 0hr|		
Views for API | H | 0hr | 0hr | 0hr|		
Serializers for App | H | 0hr | 0hr | 0hr|		
URLS/Routes for API / testing | H | 0hr | 0hr | 0hr|		
Register Account Functionality | H | 0hr | 0hr | 0hr|		
Log In Functionality | H | 0hr | 0hr | 0hr|		
Make Create view : Register Account | H | 0hr | 0hr | 0hr|		
Make Read view: Display logged-in username & avatar in nav bar | H | 0hr | 0hr | 0hr|		
Make Read view: Display list of conversations with users | H | 0hr | 0hr | 0hr|		
Make Read view: Display messages for individual conversation | H | 0hr | 0hr | 0hr|		
Make Update view : User profile settings to update avatar, username or password | H | 0hr | 0hr | 0hr|		
Make Create/Update view : User can send message through text field to update message array for conversation | H | 0hr | 0hr | 0hr|		
Make Delete view : User can delete account | H | 0hr | 0hr | 0hr|		
Refactored to work with Vue | H | 0hr | 0hr | 0hr|		
Deployed on Heroku | H | 0hr | 0hr | 0hr|
Testing | H | 0hr | 0hr | 0hr|		
Total | H | 0hr | 0hr | 0hr|

## PostMVP

| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
Search list function | H | 0hr | 0hr | 0hr|	
Implement user endpoints from SoundCloud's API | H | 0hr | 0hr | 0hr|	
Make Read view: Search list function for users | H | 0hr | 0hr | 0hr|	
Make Read view/ fetch request: Implement user endpoints from SoundCloud's API | H | 0hr | 0hr | 0hr|	
Make Create/Update view : User can send message by selecting user from populated list generated from search | H | 0hr | 0hr | 0hr|	
Make delete view : Users can delete conversations or messages | H | 0hr | 0hr | 0hr|	
Total | H | 0hr | 0hr | 0hr|


## Additional Libraries
- Vue
- Bootstrap

## Code Snippet


## Issues and Resolutions

