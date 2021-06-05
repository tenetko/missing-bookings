from controllers.basic import BasicHandler


def test_get_config():
    handler = BasicHandler()
    name = "test"
    config = handler.get_config(name)
    assert config["name"] == "test"
    assert config["profit"] == 0.02
