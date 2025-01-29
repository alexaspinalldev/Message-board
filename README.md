# Terra Java

## Overview
Terra Java is a boutique catalogue of all the world's finest coffee blends. Taking its name from the rich coffee fields found on the island of Java in western Indonesia, it aims to showcase the very best coffees from around the globe.

Vendors are able to register themselves on the site and upload, edit and delete their coffees.
Visitors can browse the listed coffees and get details on specific blends and vendors.

This site was built as my Full Stack Capstone Project with Code Institute. It uses the Django framework.

[Link to deployed site](https://terra-java-9165cf0b75d7.herokuapp.com/)
[Link to repository](https://github.com/alexaspinalldev/Terra-Java/)

## UX Design Process
### Graphic design and visual assets:
- [Selected colour palette](https://coolors.co/4f3221-34623f-ffee7d-c1b098-ffffff)

- Logo:<br>
<img src="static/images/tj-logo.webp" style="border: 1px solid white; padding: 10px; width: 40%"></img>

- Image credits:<br>
  - [Ashlyn Ciara](https://unsplash.com/@ashlynciara?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-man-in-a-hat-picking-berries-from-a-bush-4rbWwrtMQ1c?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

  - [wojtal78](https://www.istockphoto.com/portfolio/wojtal78?mediatype=photography) on [iStockPhoto](https://www.istockphoto.com/photo/coffee-bag-gm509212479-45793256?searchscope=image%2Cfilm)

  - [PROJETO CAFÉ GATO-MOURISCO](https://unsplash.com/@projetocafegatomourisco?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-lush-green-hillside-covered-in-lots-of-trees-zOVRgigQMQA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

  - [Nitin Khajotia on Pexels](https://www.pexels.com/video/a-view-of-a-lush-green-valley-with-mountains-in-the-background-19669269/)

### User flow and ERD
  - [Link to Miro](https://miro.com/app/board/uXjVLuC7tmQ=/?share_link_id=877125417995)

### User stories and Project board
  - [Terra Java project board](https://github.com/users/alexaspinalldev/projects/10)

### Wireframes:
<img src="static/images/README/Landing.png" style="width: 32%"></img>
<img src="static/images/README/Catalogue.png" style="width: 32%"></img>
<img src="static/images/README/CoffeeDetail.png" style="width: 32%"></img>
    
### Design Rationale:
- The core design of the site is based on similar simple webstore/catalogue sites. This was chosen in the interest of visual minimalism and the Jakob's Law principle. I added a simple landing page as a canvas to give the site more of an identity to follow the "exotic" nature of the brand.
- I made a concious effort to lean into the Bootstrap defaults where possible with regards to things like font sizing, as in the past I have needlessly complicated my styling and slowed me down. One notable advantage of this is more appropriate use of HTML semantics, improving experience for users of screen readers.

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