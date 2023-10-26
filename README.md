# Downloads-Stats-Flask-Repo
<div align="center" >
<img src="https://downloads-report-flask-parthdasawant.vercel.app/" />
</div>
## A) Cloning & Getting Started with the Project

1. **Clone the Git Repository**: Open your terminal or command prompt and navigate to the directory where you want to clone the Git repository. Use the `git clone` command to clone the repository:

    ```bash
    git clone https://github.com/parthdasawant/Downloads-Stats-Flask-Repo.git
    ```

2. **Change Directory**: Navigate into the cloned repository's directory:

    ```bash
    cd Downloads-Stats-Flask-Repo
    ```

3. **Create a Virtual Environment**: To create a Python virtual environment for this project, use `venv`. You can specify the environment's name (replace `myenv` with your preferred name):

   - Using `venv`:
     ```bash
     python -m venv myenv
     ```

4. **Activate the Virtual Environment**:

   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```

   - On macOS and Linux:
     ```bash
     source myenv/bin/activate
     ```
     
   Once activated, you will see the virtual environment's name in your command prompt.


5. **Installing Dependencies from Requirements.txt**: To install the project's dependencies from a `requirements.txt` file in a new virtual environment, use:

    ```bash
    pip install -r requirements.txt
    ```

- **Removing a Virtual Environment**: To delete a virtual environment, simply remove its directory. Be cautious when doing this, as it will permanently delete the environment and its installed packages.


## B) Editing & Running 
1. Follow the Folder struture since the deployment of vercel requires the file structure as I have created.
2. Move Key JSON file to the api folder
3. Go to api/app.py and insert your information

### For testing locally,
```bash
    cd api
```
```bash
    flask run
```
### For deployment
**Make sure to use the proper JSON key file path with `api/` in starting of the path(or relative path)** 
Since Vercel root directory will be ```./```.
