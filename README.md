

## Organizacja przerw:

Przerwa poranna: 10:30 - 10:45
Przerwa obiadowa: 12:15 - 12:45
Przerwa popołudniowa: 14:15 - 14:30

## narzedzia

Pycharm
Visual Studio Code

## REPL

Read Eval Print Loop

## Python

Jezyk pozwala na uzywanie roznych paradygmatow programowania: funkcyjne, proceduralne, obiektowe ...
Język interpretowany.

Typowany silnie (w odroznieniu od slabego)
Typowanie dynamicznie (w odroznieniu od statycznego)

Wszechstronne zastosowania.
Bogaty zbior bibliotek
Rozbudowana społecznosć


## Środowisko

1. Visual Studio Code lub Pycharm (Community)
2. Tworzenie wirtualnego środowiska

    python -m venv .venv

linux:

    source .venv/bin/activate

windows

    .venv\Scripts\activate


## krótki wstęp do git

```
   git init
   git remote add origin <twoj adres repo zdalnego>
   
   git status
   git add <konkretny plik>
   git add .
   
   git commit
   git commit -m "<git message>"
   git commit -a --amend  # dodaje do poprzedniego comita
   
   git diff
   git log
   git push <origin> <nazwa brancha>
   
   git pull
   git pull <origin> <nazwa brancha>
```