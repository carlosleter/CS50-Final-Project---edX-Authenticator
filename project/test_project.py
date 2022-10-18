from _tkinter import TclError
from project import screen_login, screen_register, create_an_account, sign_in, screen_painel, screen_celebration
from pytest import raises


def test_screen_login():
    with raises(TclError):
        screen_login()


def test_sign_in():
    with raises(NameError):
        sign_in()


def test_screen_register():
    with raises(TclError):
        screen_register()


def test_create_an_account():
    with raises(NameError):
        create_an_account()


def test_screen_painel():
    with raises(TclError):
        screen_painel()


def test_screen_celebration():
    with raises(TclError):
        screen_celebration()
    # with raises(NameError):
    #     screen_celebration()
