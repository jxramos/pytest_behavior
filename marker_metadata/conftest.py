def pytest_collection_modifyitems(config, items):
    """
    copies a test's markers to the user properties for the test case
    """
    for item in items:
        # Copy all markers as a record property
        markers = ", ".join([mark.name for mark in item.own_markers])
        item.user_properties.append(("markers",markers))
