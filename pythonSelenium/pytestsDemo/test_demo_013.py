import pytest
# create HTML report
# first need to install -> pip install pytest-html

# By default, the filename used is pytest_html_reporter.html and path chosen is report; you can skip both or either
# one of them if not needed: $ pytest tests/ Custom path, filename, and title Add --html-report tag followed by path
# location and filename to customize the report location and filename: $ pytest tests/ --html-report=./report $
# pytest tests/ --html-report=./report/report.html Add --title tag followed by the report title:
#
# $ pytest tests/ --html-report=./report --title='PYTEST REPORT'
# pytest.ini
#
# Alternate option is to add this snippet in the pytest.ini file:
#
# [pytest]
# addopts = -vs -rf --html-report=./report --title='PYTEST REPORT'
# Note: If you fail to provide --html-report tag, it considers your project’s home directory as the base
#
# screenshots on failure
# Import attach from the library and call it with the selenium command as given below:
#
# from pytest_html_reporter import attach
#
# ...
# attach(data=self.driver.get_screenshot_as_png())


def test_crassBrowser(crossBroser):  # we haven't pass self because it not in class now
    print(crossBroser[1])  # we can use index

# to create report used
# --> pytest test_demo_013.py --html=report_of_demo_013.html -vs
# to run all test and create report
# pytest --html=report_of_all_test.html -vs

# here report_of_all_test is file name you can give any name based on your convenience
