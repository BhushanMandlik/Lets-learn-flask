# Flask Day-04

Date: 24/10/2021 <br>

Learnt about: <br>
1. flask-flashing <br>

The flash() method is used to generate informative messages in the flask. It creates a message in one view and renders it to a template view function called next. <br>

# flash() method 

syntax: flash(message, category)    <br>

It accepts the following parameters.
1. message: it is the message to be flashed to the user.
2. Category: It is an optional parameter. Which may represent any error, information, or warning.

# get_flashed_messages() method

syntax: get_flashed_messages(with_categories, category_filter)  

It accepts the following parameters.
1. with_categories: This parameter is optional and used if the messages have the category.
2. category_filter: This parameter is also optional. It is useful to display only the specified messages.
