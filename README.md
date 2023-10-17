# ShortIt

ShortIt is a web application crafted to simplify the process of URL shortening. With a clean, intuitive interface, ShortIt makes it easy to convert long URLs into short, manageable links. This is particularly useful for sharing links in a more user-friendly manner across different platforms.

## Installation

This project is built with Django and uses Pipenv for managing dependencies. Follow these steps to get it running on your local machine:

1. Clone the repository to your local machine using `git clone <repository-url>`.

2. Navigate to the project directory with `cd ShortIt`.

3. Copy `settings.py.example` to `settings.py` and update the environment variables to match your setup.

4. Install Pipenv if you haven't already with `pip install pipenv`.

5. Install project dependencies with Pipenv by running `pipenv install`.

6. Enter the Pipenv shell using `pipenv shell`.

7. Run database migrations with `python manage.py migrate`.

8. Create an admin user for the Django admin interface using `python manage.py createsuperuser`.

9. Start the local development server with `python manage.py runserver`.

Now you can access the ShortIt web application locally.

## Contributing

We welcome contributions to ShortIt. Feel free to fork the repository or submit a pull request. We appreciate any help, whether it's fixing bugs, improving documentation, or suggesting new features.

## License

ShortIt is distributed under the MIT License. See `LICENSE` file for more information.

## Contact

If you have any questions or suggestions, feel free to reach out at business@shortit.com.
