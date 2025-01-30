# Message Board

**Insert image**
![Message Board header](assets/images)

## Introduction
Message Board is a full-stack web application that allows users to post messages for others to see. Whether it’s a note of appreciation, a public announcement, or a simple thought to share, the site provides a clean and easy way to express yourself. Leveraging Django, Message Board seamlessly manages user authentication and message posting, all within a welcoming user experience.

Message Board is the result of a 3-day hackathon by a team of developers:

* Alex Aspinall
* Jess Howkins
* Jude Wools
* Kate Elliott

This project is open source and can be forked for customisation.  

A special edition of Message Board—**Thank You, Dillon!**—was built for us, and fellow students, to express our appreciation for Code Institute Facilitator Dillon Mc Caffrey. Deployed, documented, and delivered with gratitude.

<a href="..." target="_blank">View the deployed site here.</a>

## Agile

To ensure we delivered a minimum viable product (MVP) in the hackathon's allotted time frame, as a team we used MoSCoW prioritisation. Doing so allowed us to determine the MVP from the offset and work effectively to reach this first. The <a href="" target="_blank">project board</a> shows the complete user stories along with their acceptance criteria. The user stories are also laid out below within UX Design.

## UX Design
### User Stories

The <a href="" target="_blank">project board</a> shows the complete user stories along with their acceptance criteria.

<details><summary>Must Have</summary>

* As a ...
</details>

<details><summary>Should Have</summary>

* As a ...
</details>

<details><summary>Could Have</summary>

* As a ...
</details>

## Branding

**Insert image**
![Message Board branding](assets/images)

### Fonts

Message Board uses 'Luckiest Guy' as a bold, mostly uppercase heading font and 'Shadows Into Light Two' for a body text that mimics handwriting. Both fonts are sourced from Google Fonts and there is a backup of 'sans-serif' applied on the site.

### Colour Palette

Message Board features a bold and vibrant colour palette, designed to create a welcoming and engaging experience. The chosen colours are carefully combined on the live site to ensure accessibility and readability.

**Insert image** 
<details><summary>View</summary>

![Message Board colour palette](assets/images)
</details>

### Imagery

All imagery for Message Board is from Canva, including the logo design and customisable graphics.

**Insert image** 
<details><summary>View</summary>

![Message Board imagery](assets/images)
</details>

### Wireframes



### Wireframes:
<img src="static/images/README/Landing.png" style="width: 32%"></img>
<img src="static/images/README/Catalogue.png" style="width: 32%"></img>
<img src="static/images/README/CoffeeDetail.png" style="width: 32%"></img>
    
## Key Features
- **Filter by your listings:** Logged in Vendors can filter the list view to show only their listings. If they do not have any approved listings to show, Django will return a message to them confiming that this is not an error, rather than leaving simply a blank page.
- **Coffee detail:** Clicking into a coffee listing displays summed information from both the "Coffee" and "Vendor" tables.
- **Seamless UX:** Users can seamlessly register and add/edit/remove their listings without Admin login or involvement. At the moment all listings are approved by default but this is the only reason an admin would be required in day-to-day operations.

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

## AI Implementation and Orchestration
### Use Cases and Reflections:
  - **Site Ideation:**
    - The name of the site was picked from a list of keywords provided by ChatGPT. DALLE was used to create the logo.
    - AI was also used to expand the user stories from the initial prompt describing the site's functions.
    - Whilst my initial ERD was hand drawn in the planning stage, the final one linked above was generated using https://www.eraser.io/diagramgpt from my final model set. 
       
  - **Content:** 
    - Once the ERD was complete, GPT was used to create a JSON import scripts for the lists of Vendors and Coffees. Later I also had it create Python shell scripts to add field data such as vendor.about to the existng database.

  - **Code Creation:** 
    - GPT was used to cross-examine my proposed ERD, suggesting new fields, and then create the model objects. I also used it to suggest improvements to my client javascript, such as in the "loading modal" where I had it add a condition for users ctrl+clicking on the triggering links.

  - **Debugging:** 
    - GPT was utilised lightly to fix initial issues with my views, and also to troubleshoot issues with my DTL variables and static files not being found.

  - **Performance and UX Optimization:** 
    - AI was not used for this purpose.

  - **Automated Unit Testing:**
    - AI was used to troubleshoot issued with testscripts, and provided me the workaround of using python shell commands to the same effect.

- **Overall Impact:**
  - AI is an excellent tool for both generating codeblocks to save time, particularly markup, and also template content for the site's example database items. It is also extremely valuable for getting precise answers to nuanced troubleshooting situations.

## Testing Summary
- **Manual Testing:**
  - **Devices and Browsers Tested:** Tested manually on desktop and mobile devices.
  - **Features Tested:** Signing up, logging in and out, adding, editing and removing Coffee listing functions were tested manually on all devices. I noted that the js scripts targeting features only available to authenticated users would result in console errors for non-authenticated users, so wrapping them in if statements resolved this.
  - **Results:** Mobile testing revealed a few bugs including stretched images and some specific restrictions on iOS around video autoplaying. This later issue was resolved by checking the Apple documentation on the subject and adding the correct attributes.
- **Automated Testing:**
  - Tools Used: Django's built-in testing framework
  - Features Covered: CoffeeAdd, CoffeeUpdate and SignUp forms were tested using automated test cases. I had issues doing this using class-based test so I instead opted to test through the Python Shell. AI suggested this alternative approach. I could not get Automated view testing working unfortunately so had to rely on manual testing results.
  - Adjustments Made: On my Coffee model, I had neglected to include the mandatory "max_length" attribute on my choice field. Resolving this allowed my form tests to pass.
- **Validation:**
All final validation and testing was performed on the deployed version of the site.
  - **HTML:** All pages passed W3C Markup validation checks with minimal changes. 
  - **LightHouse:** Lightouse testing was predictably harsh on the landing page due to the large video load. More efficiently serving this video will be a future enhancement. Other than that, all pages scroed 90+ on all Lighthouse metrics during both mobile and desktop emulations.
  - **CSS:** All CSS passed validation with no changes. There extant errors with the scrolling animation in "catalogue.css" but this contradicts Google's own scroll-driven-animations.style tool.
  - **JS:** All JS passed JSHint check with only a few missing semicolons to correct.


## Future Enhancements
- Add more explicit view to Vendors of their listings that are unapproved, rather than filtering those out for all users.
- Add greater sidebar filtering options.
- Add a more appropriate homepage than just launchng straight into the catalogue.
- Add a webstore app to the site.
- Add the ability to contact vendors.
- Add the ability to leave reviews for the coffees.
