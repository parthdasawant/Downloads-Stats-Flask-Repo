# Downloads-Stats-Flask-Repo
<div align="center" >
<img src="https://downloads-report-flask-parthdasawant.vercel.app/" />
</div>

Check out the article for step-by-step guide
<div align="center" >
<a target="_blank" href="https://github-readme-medium-recent-article.vercel.app/medium/@parthdasawant/2"><img src="https://github-readme-medium-recent-article.vercel.app/medium/@parthdasawant/2" alt="Recent Article 0"> 
</div>

## A) Cloning & Getting Started with the Project

1. **Clone the Git Repository**: Open your terminal or command prompt and navigate to the directory where you want to clone the Git repository. Use the `git clone` command to clone the repository:

    ```bash
    git clone https://github.com/parthdasawant/Downloads-Stats-Flask-Repo.git
    ```

2. **Change Directory**: Navigate into the cloned repository's directory:

    ```bash
    cd Downloads-Stats-Flask-Repo/api
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
    flask run
```
### For deployment
**Make sure to use the proper JSON key file path with `api/` in starting of the path(or relative path)** 
Since Vercel root directory will be ```./```.

#### The file structure tree should be as follows
```bash
.
├── api/
│   ├── env/
│   ├── app.py
│   └── keyFile.json
├── .gitignore
├── README.md
├── requirements.txt
└── vercel.json
```
## How to use After deployment
### GitHub Readme badge
Add following code to your readme file by replacing `<Vercel_Deployed_URL>` with your URL.
```bash
    <img src="<Vercel_Deployed_URL>" />
```
### API
You can access the API by replacing `<Vercel_Deployed_URL>` with your URL in following link. 
```bash
    <Vercel_Deployed_URL>/json
```
### Conclusion
Well, I think that’s all for now. If you find any issues, you can directly open an issue on GitHub. I’ll try to help as much as I can.
