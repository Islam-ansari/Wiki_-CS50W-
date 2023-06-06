<!-- Add banner here -->
![Banner](./Wki.png)
# Wiki

## Description
This is a Wiki website based on as you've guessed Wikipedia, it is built using HTML, CSS, Javascript and Django. It allows users to read articles that are listed on the home page. Wikipedia articles are not written in HTML it would start to get tedious if every page on Wikipedia had to be written in HTML. Instead, it can be helpful to store encyclopedia entries using a lighter-weight human-friendly markup language. Wikipedia happens to use a markup language called **Wikitext**, but for this project markup language called **Markdown** is supported. 

Thus it allows user to create their own aricles using markup language **Markdown**. A user can search article by name and can also get random articles.

## Demo Video

[![Watch the video](https://img.youtube.com/vi/mIyvTz4wtNY/maxresdefault.jpg)](https://youtu.be/mIyvTz4wtNY)


## Installation
To run this project locally, follow these steps:
1. Install Python and Django.
2. Clone this repository.
3. Run the migrations using `python manage.py migrate` just to be safe and to migrate all the information from the database.
4. Start the development server using `python manage.py runserver`.

## Usage
- Visit the website and click on the link to read that article.
- Browse different articles and edit them online editor.
- Add new article to the website.
- Get random aricles by cliking on **Random Page**.

## Technologies Used
- Django
- HTML/CSS
- JavaScript
- Bootstrap
- SQL

## Folder Structure
- `wiki/` - Django project settings and configurations.
- `encyclopedia/` - Django app files, including views, models, and templates.
- `entries/` - Markdown files of different aricles.
- `static/` - Static files such as CSS stylesheets and JavaScript scripts.
- `templates/` - HTML templates for different pages.

## Deployment
To deploy this website, follow these steps:
1. Set up the files in your local system as explain in the [Installation](## Installation).
2. Start the development server using `python manage.py runserver`.
3. You should be able to see the website

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them.
- Push your changes to your forked repository.
- Submit a pull request.

## Authors
- Islam Ansari (@Islam-ansari)

## Acknowledgments
- Special thanks to the [**CS50's Web programming using pyton and javascript**](https://cs50.harvard.edu/web/2020/) course for giving me opportunity to work on this amazing project.
- Special thanks to the CS50's **Discord** community for helping me out when i needed.

