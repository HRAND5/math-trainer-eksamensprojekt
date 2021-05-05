# Eksamensprojekt 2021
This program is a part of an end of year project in Programmering B at a tehcnical High School in Denmark, made by [HRAND5](https://github.com/HRAND5) and [kanka9876](https://github.com/kanka9876). 

The program is a tool to help students get better at Mathematics. As a user you are given a rating, and as you answer more questions correctly, your rating will be increased. The higher your rating, the more difficult questions you will get. If you answer questions wrong, your rating will drop and you will get easier questions. Only two questions are included, but you can add more using a command line tool included. 

Most of this project is in Danish for obvious reasons, and the code is a healthy mismatch of Danish/English and snakecase/camelcase naming conventions. Just to give you a bit of an edge while reading the code ;) 

## Installation
### Windows
Clone the repository to a local directory. Open a command line and navigate to the directory you cloned the repository to. Run the following command to install all the dependencies. 
```console
$ pip install -r requirements.txt
```

To run the main program, run the following command in the directory

```console
$ python main.py 
```
To run the command line tool to add new questions to the program, run the following command. 

```console
$ python edit_question.py
```
