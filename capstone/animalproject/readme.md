# A Searchable Database For An Animal Shelter
### Product Overview
 The goal of this project is to set up a searchable database, which could be potentially used on a website of any animal shelter or animal rescue organization. This search engine will allow potential adopters to find the best match. The shelter team should be able to add and edit animal profiles easily. This Django app is simply looking, easy to use, lightweight and mobile-friendly.
### Specific Functionality
The information about adoptable animals will be contained in animal profiles stored in the database. The project will have two main sections for the two groups of users:
   - the database management system available **for the shelter staff** from the admin panel;
   - the search engine available **for everyone** on the main website.
##### 1. Database Management
- Ability to search through the profiles and filter results
- Ability to add new profiles quickly, with as little typing as possible, eg. by selecting tags for personality description
- Plenty of options to choose from, when creating a new profile (drop-down and select menus)
- Ability to add many profiles one by one easily
- Ability to search, view, sort, edit and delete existing profiles
- Ability to upload multiple pictures to every animal profile
##### 2. Search Engine
- Searching by tags (full text search and autosuggest with ElasticSearch coming soon)
- Ability to see all profiles at once or apply filters
- Ability to sort search results
- Ability to share profiles on social media
- Ability to send an email to OFOSA staff about a specific animal using a button in the profile
- Ability to make a donation from the animal profile
### Data Model
![alt text]( https://github.com/jastr945/PDXclass/blob/master/capstone/animalproject/animalapp/static/animalapp/img/capstone_data_structure.jpg "Data model diagram")
 ### Technical Components

**__The responsive design was created using SASS and CSS Flexbox.__**

#### Sign up/ log in pages
- Django built-in authentication system
- Customized templates
- The ability to edit and delete existing profiles is reserved only for logged users

#### My Activity page
- Django ModelForm based on 3 models
- Basic form validation in models, views and HTML
- Django FileField uploading multiple images
- Django TypedChoiceFields with customized RadioSelect widgets
- Django Multiselect package for selecting multiple categories
- Python function calculating each animal's precise age
- Python function adding 'kitten', 'puppy' or 'adult' tags depending on animal's age
- RegEx function splitting several-words fields into one-word tags
- Filtering database rows dynamically with Django-filters
- JQuery for displaying the 'delete' option for every database row
- Showing and hiding basic categories on click with JQuery

#### Index (main) page with a search engine
- A Django form for searching the database
- Javascript for zooming in the search form
- Ability to search through the database tags with Django Taggit package

#### Search Results page
- A Django form for repeating the search
- A template counter for the number of results
- Filtering the results dynamically with Django-filters

#### Animal Profiles
- Image gallery (JQuery PGWSlideShow slider)
- Social media buttons
- Searchable tags (Django Taggit package)
- An email button to contact the shelter team
- A donation button for sending money

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
