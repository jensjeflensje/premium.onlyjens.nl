# OnlyJens Premium
My personal donation site.
Public, so you can just to take a look and maybe steal some code ;).

## Overview
The site features some information about me, some links to my project, and a donation panel.
The donation panel lets you donate a custom amount.
When a user donates and goes back to the site,
they'll get a popup with their "certificate", as a show of gratitude.

## Backend
I'm using Django as a backend with Django Rest Framework.
There's only a few endpoints to handle donations (and donation certificates).
I'm using Django Q as a task queue to handle donation certificate generation.
I use PostgreSQL as a database (even though I don't store that much),
and redis for Django Q.

## Frontend
The frontend is made with VueJS in TypeScript.
I'm using PrimeVue as a base for my buttons, inputs, dialogs etc.

## Services
I'm using S3 to store certificate files, and to let people download them.
I'm also using stripe to process payments.

