# AUGSD Course Load Project

The Course Load Project is a web portaal built to automate the process of course load generation in various format for the AUGSD office, BITS Pilani, K. K. Birla Goa Campus.
Frontend is built on React.js and backend using Django python. The database used is PostgreSQL. Hosted using Heroku and AWS.

## Installation
Clone this repository into your system
```bash
git clone https://github.com/AdarshNandanwar/augsd-course-load.git
```
## Usage
Create and activate a virtualenv.
```bash
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
virtualenv venv 
source venv/bin/activate
```
Install required dependencies.
```bash
pip install -r requirements.txt
```
Run the server.
```bash
python manage.py runserver
```

---

## Contribute
### Create fork (one time)
- Press **Fork** button from [this](https://github.com/AdarshNandanwar/augsd-course-load) repository and select your account.
- In your GitHub fork, press **Clone or Download** and copy the url.
- Open the terminal and type: 
    ```bash
    git clone <copied_url>
    git remote add origin <copied_url>
    git remote add upstream https://github.com/AdarshNandanwar/augsd-course-load
    ```
- **IMPORTANT**: Create a branch development where you can do the changes , accepted changes will get merged with master branch
- **IMPORTANT**: Do the following to disable push on upstream handle
    ```bash
    git remote set-url --push upstream no_push
    ```

### Submiting PR
```bash
git add <filename>
# or to add everything using "git add ."
git commit -m <commit_message>
git pull upstream master
# Resolve merge conflicts (if any)
git push origin master
```
On your GitHub development branch, press **Compare & pull request** and then **Create Pull Request** on next page
