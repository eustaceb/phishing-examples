# Phishing examples
This repo contains a Flask webserver with two phishing examples. These can be run offline and I've used them for one of my courses, to teach children about phishing attacks.

All of these examples are working as of 2017/01/15 but that might change with browser updates.

## Target="_blank" vulnerability - Fakebok example
The example depicts a fakebook page with an ad in it that opens up a 404 page in a new tab. Meanwhile, the previous tab gets redirected to a fake fakebook login page, which, after logging in, redirects you back to fakebook. The details are not actually captured as I mocked the example using images and clickable image maps. Therefore it's a good idea to explain what's happening / at which step the details get captured during the presentation.

Based on [Alex Yumashev](https://www.jitbit.com/alexblog/256-targetblank---the-most-underestimated-vulnerability-ever/)'s article.

## Autofill phishing
Based on [anttiviljami](https://github.com/anttiviljami/browser-autofill-phishing)'s repo. Removed an external httpbin.org dependency and created my own form data capture page so the example can be run in an offline environment. Some schools limit network access.

# Usage
Simply run 
```
python phishing_server.py
```
And then go to http://127.0.0.1:5000/

Requires [Flask](http://flask.pocoo.org/), which can be setup by running
```
pip install Flask
```
