# ShortIt

ShortIt is a web application crafted to simplify the process of URL shortening. With a clean, intuitive interface, ShortIt makes it easy to convert long URLs into short, manageable links. This is particularly useful for sharing links in a more user-friendly manner across different platforms.

## Installation

This project is built with Django. Follow these steps to get it running on your local machine:

1. Clone the repository to your local machine using `git clone <repository-url>`.
2. Navigate to the project directory with `cd ShortIt`.
3. Copy `settings.py.example` to `settings.py` and update the environment variables to match your setup.
4. Run `pip install -r requirements.txt` to install the project dependencies.
5. Run `python manage.py migrate` to set up the database.
6. Run `python manage.py createsuperuser` to create an admin user for the Django admin interface.
7. Run `python manage.py runserver` to start the local development server.

## Contributing

We welcome contributions to ShortIt. Feel free to fork the repository or submit a pull request. We appreciate any help, whether it's fixing bugs, improving documentation, or suggesting new features.

## License

ShortIt is distributed under the MIT License. See `LICENSE` file for more information.

## Contact

If you have any questions or suggestions, feel free to reach out at business@shortit.com.
