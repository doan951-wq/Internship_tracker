from User_Input import get_action

def test_valid_input_add(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "add")

    valid_answer = ["add", "remove", "edit", "stop"]
    assert get_action() == "add"

def test_valid_input_remove(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "remove")
    assert get_action() == "remove"

def test_valid_input_edit(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "edit")
    assert get_action() == "edit"


def test_valid_input_stop(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "stop")
    assert get_action() == "stop"

def test_invalid_input(monkeypatch):
    test_inputs = iter(["hello world", "add"])

    monkeypatch.setattr("builtins.input", lambda _: next(test_inputs))


    assert get_action() == "add"       

    


