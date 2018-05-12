# Piscium 

A lightweight web development lab

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python 3.6.5
```
sudo apt install python3
```
* pip
```
sudo apt-get install python3-pip
```

### Installing

#### Back-end development env running:

##### Web server and web application framework:
* Tornado 5.0.2
    ```
    sudo pip3 install tornado
    ```
##### Database server:
* MariaDB 10.2.14
    ```
    sudo apt install mariadb-server
    ```
* Python mariaDB connector: PyMySQL
    ```
    sudo pip3 install PyMySQL
    ```
##### In-Memory database server:
* Redis 4.0.9
    ```
    sudo apt-get install redis-server
    ```
* Python Redis connector: redis-py
    ```
    sudo pip3 install redis
    ```

#### Front-end development env running:
##### JavaScript run-time environment
* Node.js 8.10.0
    ```
    sudo apt install nodejs
    ```
##### JavaScript dependency management:
* Yarn 1.6.0 (npm comes witho node.js)
    ```
    sudo npm install -g yarn
    ```
##### JavaScripts dependencies packages:
* Use Yarn to install all dependencies packages in the project folder with:
    ```
    yarn install
    ```
## Running the tests
Run server.py
```
python3 server.py
```
Open http://localhost:8000/ in web browser

## Deployment

## Built With

* [Tornado](http://www.tornadoweb.org/en/stable/guide.html) - The web framework used
* [Yarn](https://yarnpkg.com/en/docs/) - JavaScript Dependency Management
* [webpack](https://webpack.js.org/concepts/) - JavaScript static module bundler
* [React](https://reactjs.org/docs/hello-world.html) - JavaScript library for building user interfaces

## Development tools
### IDE
* PyCharm Community
    * plugins:
        * GitHub
        * Git Integration
### Editor
* Visual Studio Code
    * plugins:
        * Python
        * Tornado
        * JavaScript (ES6) code snippets
        * Path Intellisense
        * Yarn
        * Reactjs code snippets
        * ReactJS, Redux & React Router snippets
        * vscode-icons
### Database GUI
* MySQL Workbench

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [Git](https://git-scm.com/doc) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Menglong Wu** - *Initial work* - [me-lon](https://github.com/me-lon)

See also the list of [contributors](https://github.com/piscium-proj/piscium/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments