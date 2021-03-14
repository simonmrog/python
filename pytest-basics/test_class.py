from main import calculator


def test_class_monkey(monkeypatch):
    monkeypatch.setattr(calculator, "sum", lambda x: 4)
    c = calculator()
    assert c.sum() == 4
