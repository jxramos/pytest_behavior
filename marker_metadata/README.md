# Marker Metadata

A test cases's own markers can be injected into the junit xml to retain the marker metadata defined
for each test case. This can be done very conveniently in the context of the conftest file where the
collected items can be modified to inject into the [`user_property`](https://docs.pytest.org/en/6.2.x/reference.html#pytest.Item.user_properties)
the marker metadata. This will input into the junit xml the same name value pairs as the standard
[`record_property`](https://docs.pytest.org/en/6.2.x/reference.html#record-property) fixture does.

Consider the following junit xml generated from the following command
```bash
pytest marker_metadata --junit-xml=marker_metadata/test_result.xml
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<testsuite errors="0" failures="0" name="pytest" skipped="0" tests="4" time="0.029">
    <testcase classname="marker_metadata.test_module" file="marker_metadata/test_module.py" line="2" name="test_no_markers" time="0.001">
        <properties>
            <property name="markers" value="" />
        </properties>
    </testcase>
    <testcase classname="marker_metadata.test_module" file="marker_metadata/test_module.py" line="5" name="test_sole_marker" time="0.001">
        <properties>
            <property name="markers" value="sole_marker" />
        </properties>
    </testcase>
    <testcase classname="marker_metadata.test_module" file="marker_metadata/test_module.py" line="9" name="test_two_markers" time="0.001">
        <properties>
            <property name="markers" value="marker2, marker1" />
        </properties>
    </testcase>
    <testcase classname="marker_metadata.test_module" file="marker_metadata/test_module.py" line="14" name="test_record_property" time="0.001">
        <properties>
            <property name="markers" value="record_prop" />
            <property name="data" value="3" />
        </properties>
    </testcase>
</testsuite>
```
