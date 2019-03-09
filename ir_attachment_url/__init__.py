def post_load():
    pass
    # in /controllers/main there is an import from the `mail` module
    # it leads to loading the mail and all its dependencies earlier than the patch in `binary_fields` is applied.
    # That is why the `from . import controller` line is here
