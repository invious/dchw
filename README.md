# Amazon EC2 Instance Monitor

### Installation

* Clone this repository and [create a virtual environment for the project.](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)
* Install the requirements: `pip install -r requirements.txt

### Setup

* Rename `example_local_settings.py` to `local_settings.py` and add your AWS keys.
* In th Django project root directory run:
  * ```
    python manage.py makemigrations updates
    python manage.py migrate
    ```
    
#### Run

`python manage.py runserver`

