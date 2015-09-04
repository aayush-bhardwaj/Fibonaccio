# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Fibonaccio',"'",'s'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="http://aksinghdce.github.io/",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
          (T('My Fibonacci'), False, '#', []),
          ('Mentors', False, '#', [             ]),
          (T('Programs'), False, '#', [             ]),
          (T('Community'), False, None, [
             (T('Groups'), False,
              'http://www.web2py.com/examples/default/usergroups'),
              (T('Twitter'), False, 'http://twitter.com/web2py'),
              (T('Live Chat'), False,
               'http://webchat.freenode.net/?channels=web2py'),
              ]),
        (T('About Us'), False, '#', [
           (T('About'), False, URL('default', 'About'), []),
           (T('What we do?'), False, URL('default', 'what_we_do'), []),
            (T('Learning Process'), False, URL('default', 'Learning_Process'), []),
            (T('Core Idea'), False, URL('default', 'Core_Idea'), []),
            (T('Revenue Model'), False, URL('default', 'Revenue_Model'), []),
            (T('Operational Activities'), False, URL('default', 'Operational_Activities'), []),
            (T('Programming'), False, URL('default', 'Programming'), []),
        ]),


        ]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu() 
