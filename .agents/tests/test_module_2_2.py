# -*- coding: utf-8 -*-
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_2.task_2 import manage_clients

def test_manage_clients():
    clients = {1: "Jan Kowalski"}
    
    # Dodawanie
    clients = manage_clients(clients, 2, "add", "Anna Nowak")
    assert clients[2] == "Anna Nowak"
    
    # Usuwanie
    clients = manage_clients(clients, 1, "remove")
    assert 1 not in clients
    assert 2 in clients
