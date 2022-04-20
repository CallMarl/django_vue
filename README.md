# DJANGO BASE

#### Stack du projet

_Frameworks :_
- Django
- Django REST
- JQuery
- Bootstrap 5
- VueJS 2
- Sass

_Dev dependencies :_
- Factory Boy
- Webpack

#### Architecture du projet
```python
.
├── api                     # Dossier dédié aux appel d'api
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   └── views.py
├── core                    # Le coeur de l'application
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── exts                    # Dossier des extensions les apps codé à la main
├── main                    # Dossier de configuration du projet
│   ├── configs
│   │   ├── dev.py
│   │   └── prod.py
│   ├── context
│   │   └── ga.py
│   ├── locale
│   │   └── .gitkeep
│   ├── management
│   │   └── commands
│   │       └── setup_domain.py
│   ├── settings.py
│   ├── sitemaps
│   │   └── static.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media                   # Les fichier uploadé par les utilisateurs
│   └── default             # Les fichier avant upload de l'utilisateurs
├── node_modules            # Les librairies JS aditionnels
├── package.json
├── package-lock.json
├── README.md
├── requirements.txt
├── static                  # Les fichier static de l'application sauf: exts
│   ├── dist
│   │   ├── index.css
│   │   ├── index.js
│   │   └── pages
│   │       └── page_vuejs.js
│   └── imgs
├── theme                   # Le themes de l'applications
│   ├── assets              # Les sources compilés par webpack
│   │   ├── fonts
│   │   ├── js
│   │   │   ├── index.js
│   │   │   └── pages
│   │   │       ├── main.js
│   │   │       └── page_vuejs.js
│   │   └── scss
│   │       └── style.scss
│   ├── imgs
│   └── template            # La template HTML
│       ├── layout
│       │   └── main.html
│       └── pages
│           └── home.html
└── webpack.config.js
```

#### Install

```bash
pip install -r requirements.txt
npm i
```

```bash
# Depuis le dossier racine dans 2 terminaux
python manage.py runserver
npm run webpack
```

- La page d'accueil django est sur `127.0.0.1:8000`
- La page d'accueil avec vuejs incorporé est sur `127.0.0.1:8000/home`
