=====
Final Project Stream 3
=====

Recipe App
-----------

This is a Django App designed to be a source of ideas for cooking recipes with ingredients you might have at home.
You can use the search box on the home page to search for recipes by recipe name. Using the navigation you
may end up in our blog section, where you can share ideas with other users, or if you want to tell us one of your recipes,
you can do so by clicking on "Add Recipe" (you can chose not to tell your secret ingredient :) It is up to you).
If you know someone who love cooking healthy food, or want to make a good present, or you are just passionate about food, please
use our Product page to purchase one of our books.

This App is built with:
-----------
Python,
Django,
Stripe,
Bootstrap,
Javascript/jQuery
HTML
CSS

Help From:
-----------

I used some help from https://codepen.io/ for my Navbar hover effect and the footer, with some changes on HTML and CSS code to match my needs

=====
Blog
=====
 
Blog is a reusable blog app for Django
 
Detailed documentation is in the "docs" directory.
 
Quick start
-----------
 
1. Add 'reusable_blog' to your INSTALLED_APPS setting like this::
 
    INSTALLED_APPS = (
        ...
        'reusable_blog',
    )
 
2. Include the polls URLconf in your project urls.py like this::
 
    url(r'^blog/', include('reusable_blog.urls')),
 
3. Run `python manage.py migrate` to create the blog models.
 
4. Add the blogs css::
    <link rel="stylesheet" href="{% static "css/blog.css" %}">
 
5. Add a link to the blog in the base.html
=====
Hosting
=====

The project is deployed to Heroku and you can see it by clicking [Here](https://food-recipe-app.herokuapp.com/)