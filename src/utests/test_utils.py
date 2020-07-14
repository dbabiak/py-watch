from utils import fpath_to_module_name


def test_fpath_to_module():
    assert fpath_to_module_name('./models/b/__init__.py') == 'models.b'
    assert fpath_to_module_name('models') == 'models'
    assert fpath_to_module_name('models/b/c.py') == 'models.b.c'
    assert fpath_to_module_name('models.b.c') == 'models.b.c'
    assert 'bang' == 'bang'
