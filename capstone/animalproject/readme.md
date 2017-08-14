# New Searchable Database for OFOSA (Oregon Friends of Shelter Animals)
### Product Overview
 The goal of this project is to set up a new searchable database for Oregon Friends of Shelter Animals (OFOSA), which will be added to the existing website of the organization. The current system that the website has, is poorly organized and has limited options. The new search engine will allow potential adopters to find the best match. The shelter team should be able to add and edit animal profiles easily. The new application will be simply looking, easy to use, lightweight and mobile-friendly. It's very important for the OFOSA team to be able to access the database from any device and edit it on the go. 
### Specific Functionality
The information about adoptable animals will be contained in animal profiles stored in the database. The project will have two main sections for the two groups of users: 
   - the database management system available **for the shelter staff** from the admin panel;
   - the search engine available **for everyone** on the main website.
##### 1. Database Management
- Ability to search through the profiles and filter results
- Ability to add new profiles quickly, with as little typing as possible, eg. by selecting tags for personality description
- Plenty of options to choose from, when creating a new profile (drop-down or autocomplete)
- Ability to add many profiles one by one easily
- Ability to search, view, sort, edit and delete existing profiles from the admin panel
- Ability to upload several pictures to every animal profile
##### 2. Search Engine
- Full text search and autosuggest. Enables users to quickly find and select from a pre-populated list of values as they type. Will correct user's typos.
- Ability to see all profiles at once or apply filters
- Ability to sort search results
- Ability to share profiles on social media
- Ability to send an email to OFOSA staff about a specific animal using a button in the profile
- Ability to make a donation from the animal profile
### Data Model
![alt text]( https://github.com/jastr945/PDXclass/blob/master/capstone/animalproject/animalapp/static/animalapp/img/capstone_data_structure.jpg "Data model diagram")
 ### Technical Components

The entire frontend was created using SASS and CSS Flexbox.

#### Sign up/ log in pages
- Django built-in authentication system
- Customized templates

#### My Activity page
- Django ModelForm based on 3 models
- Basic form validation in models, views and HTML
- Django FileField uploading multiple images
- Django TypedChoiceFields with customized RadioSelect widgets
- Django Taggit package for searchable tags
- Python function calculating each animal's precise age
- Python function adding 'kitten', 'puppy' or 'adult' tags depending on animal's age
- RegEx function splitting several-words fields into one-word tags
- JQuery for displaying the 'delete' option for every database row
- Showing and hiding basic categories on click with JQuery

#### Index (main) page with a search engine
- Django form
- Javascript for zooming in the search form
- Ability to search through tags with Django Taggit

#### Search Resukts page
- Django form for repeating the search
- A template counter for the number of results

#### Animal Profiles
- Image gallery (JQuery PGWSlideShow slider)
- Social media buttons (HTML)
- An email button to contact the shelter team (HTML, coming soon)
- A donation button for sending money (HTML, coming soon)

### Sketches
1. Search engine page prototype
![alt text](https://github.com/jastr945/PDXclass/blob/master/capstone/animalproject/animalapp/static/animalapp/img/search_engine_page.png "Search engine page")
2. Animal profile
![alt text](https://github.com/jastr945/PDXclass/blob/master/capstone/animalproject/animalapp/static/animalapp/img/animal_profile.png "Animal profile")
3. Search results page
![alt text](https://github.com/jastr945/PDXclass/blob/master/capstone/animalproject/animalapp/static/animalapp/img/search_results_page.png "Search results")
4. Admin panel
![alt text](https://github.com/jastr945/PDXclass/blob/master/capstone/animalproject/animalapp/static/animalapp/img/admin_panel.png "Admin panel")
 ### Estimated Schedule
week 1: creating admin profile and login script

week 2: creating animal database and animal profiles

week 3: creating a search engine

week 4: connecting all of the elements and working on design

### Functionality Beyond MVP (coming soon)
- Ability to apply filters to animal pictures and edit them
- Ability to add videos to animal profiles
- Make the shelter team be able to highlight certain animal profiles on the main page
- Add a messenger to the admin panel and connect it to the 'ask a question' button in the animal profile
- Allow users to choose ‘list-view’ or ‘grid-view’ for search results.
- Show search progress (insert a progress indicator)
- Provide alternatives when there are no matching search results 
