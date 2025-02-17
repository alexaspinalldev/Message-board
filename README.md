# Message Board

![Message Board header](readme/images/message-board-header.png)

## Introduction
Message Board is a full-stack web application that allows users to post messages for others to see. Whether it’s a note of appreciation, a public announcement, or a simple thought to share, the site provides a clean and easy way to express yourself. Leveraging Django, Message Board seamlessly manages user authentication and message posting, all within a welcoming user experience.

Message Board is the result of a 3-day hackathon by a team of developers:

* Alex Aspinall
* Jess Howkins
* Jude Woolls
* Kate Elliott

This project is open source and can be forked for customisation.  

A special edition of Message Board—**Thank You, Dillon!**—was built for us, and fellow students, to express our appreciation for Code Institute Facilitator Dillon Mc Caffrey. Deployed, documented, and delivered with gratitude.

<a href="https://messageboard1-f1454f42f245.herokuapp.com/" target="_blank">View the deployed site here.</a>

## Agile

To ensure we delivered a minimum viable product (MVP) in the hackathon's allotted time frame, as a team we used MoSCoW prioritisation. Doing so allowed us to determine the MVP from the offset and work effectively to reach this first. The <a href="" target="_blank">project board</a> shows the complete user stories along with their acceptance criteria. The user stories are also laid out below within UX Design.

## UX Design
### User Stories

The <a href="" target="_blank">project board</a> shows the complete user stories along with their acceptance criteria.

<details><summary>Must Have</summary>

* As a user, I can submit a thank-you message so that I can express my appreciation for the facilitator
* As a user, I can see all thank-you messages displayed on the board so that I can read what others have written.
* As a user, I can use a form with validation so that I don't submit an empty or invalid message.
* As an admin, I can remove inappropriate messages so that the board stays respectful and relevant.
* As a user, I can see a visually appealing message board so that it feels engaging and pleasant to use.
* As a user, I can access the message board on different devices so that I can participate from a phone, tablet, or computer.
</details>

<details><summary>Should Have</summary>

* As a user, I can edit or delete my own messages so that I can correct mistakes or remove unwanted posts.
* As a user, I can see timestamps on messages so that I know when each message was posted.
</details>

<details><summary>Could Have</summary>

* As a user, I can filter or search for messages so that I can easily find specific posts.
* As a user, I can react or 'like' messages so that popular messages get highlighted.
* As a user I would like to be able to upload a picture or gif to express my gratitude.
* As a User I would like the webpage to automatically update so I don't miss any new messages.
</details>

## Branding

![Message Board branding](readme/images/message-board-branding-slide.png)

### Fonts

Message Board uses 'Luckiest Guy' as a bold, mostly uppercase heading font and 'Shadows Into Light Two' for a body text that mimics handwriting. Both fonts are sourced from Google Fonts and there is a backup of 'sans-serif' applied on the site.

### Colour Palette

Message Board features a bold and vibrant colour palette, designed to create a welcoming and engaging experience. The chosen colours are carefully combined on the live site to ensure accessibility and readability.

<details><summary>View</summary>

![Message Board colour palette](readme/images/message-board-colours-palette.png)
</details>

### Imagery

All imagery for Message Board is from Canva, including the logo design and customisable graphics. The Message Board logo has been made available as a <a href="https://www.canva.com/design/DAGeDvOeI_E/ZyXe0WT5poslv3GVNi5maQ/view?utm_content=DAGeDvOeI_E&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview">template on Canva</a> for anyone choosing to customise their own version.

<details><summary>View</summary>

![Message Board imagery](readme/images/message-board-imagery.png)
</details>

### Wireframes

The wireframes below show the planned output for Message Board on desktop. The end result is very similar to these, with the focus being the randomised collage of messages that come to the front when hovered over. On a mobile view the messages are instead displayed in a list to ensure each message is readable.

<details><summary>View</summary>

![Message Board wireframes](readme/images/landing-wireframe.png)
![Message Board wireframes](readme/images/homepage-wireframe.png)
</details>


### Responsiveness

Message Board is reponsive across screen sizes thanks to the use of media queries, Bootstrap, and the changing layout on mobile.

<details><summary>View</summary>

![Message Board ERD](readme/images/ERD-pic.png)
</details>

## ERD

<details><summary>View</summary>

![Message Board ERD](readme/images/responsiveness.png)
</details>
    
## Features

### Existing Features

- User Authentication: Users can sign up, log in, and log out.
- User Profiles: Each user has a profile page displaying their posts and reactions.
- Responsive Design: The application is fully responsive and works on various devices (desktop, tablet, mobile).
- The delete button to delete a post you no longer want displayed
- Like button to add a like reaction to the post

### Future Features

* Ability to filter or search for specific messages.
* Ability to upload a picture of gif with a message.

## Deployment
- **Platform:** Heroku
- **High-Level Deployment Steps:** 
  1. Ensure project is set correctly for deployment
  2. Push code to Github
  3. Deploy from main in Heroku dashboard
- **Verification and Validation:**
  - All CRUD operations were retested manually in the deployed version. Often this was faster for making DB changes than spooling up the local server.
- **Security Measures:**
  - Use of environment variables for sensitive data.
  - Ensured DEBUG mode is disabled in production.

 <a href="https://messageboard1-f1454f42f245.herokuapp.com/" target="_blank">View the deployed site here.</a>


## AI Implementation and Orchestration
### Use Cases and Reflections:
  - **Code Suggestions and Autocompletion:**
    - AI tools like GitHub Copilot have been instrumental in providing code suggestions and autocompletion, significantly speeding up the development process and reducing the likelihood of syntax errors.
  - **Automated Testing:**
    - AI has been used to generate a test cases, ensuring the robustness and reliability of the application.

- **Overall Impact:**
  - The integration of AI tools has streamlined the development workflow, enhanced code quality, and improved the efficiency of testing and content moderation processes.

## Testing

Below is evidence of the external testing that we were able to complete in the allotted time frame, but it is missing external testing for Python, HTML, and accessibility. The developer team also each manually tested the site.

### Lighthouse

<details><summary>Landing</summary>

![Lighthouse testing](readme/images/lighthouse-home-desktop.png)
![Lighthouse testing](readme/images/lighthouse-home-mobile.png)
</details>
<details><summary>Home</summary>

![Lighthouse testing](readme/images/lighthouse-main-desktop.png)
![Lighthouse testing](readme/images/lighthouse-main-mobile.png)
</details>
<details><summary>Form</summary>

![Lighthouse testing](readme/images/lighthouse-form-desktop.png)
![Lighthouse testing](readme/images/lighthouse-form-mobile.png)
</details>

### CSS

<details><summary>Validation</summary>

![Lighthouse testing](readme/images/css-validation.png)
</details>
<details><summary>Warnings</summary>

![Lighthouse testing](readme/images/css-warnings.png)
</details>

### JavaScript

<details><summary>script.js</summary>

![Lighthouse testing](readme/images/script.js.png)
</details>
<details><summary>cloudPlacement.js</summary>

![Lighthouse testing](readme/images/cloudPlacement.js.png)
</details>

## Credits
### Code
* Code Institute's Codestar project assisted with the foundations of Message Board.

### Media
* Canva

## Acknowledgements
A huge thank you to Dillon Mc Caffrey for inspiring this project and providing support and kindness throughout our entire time studying with Code Institute.
