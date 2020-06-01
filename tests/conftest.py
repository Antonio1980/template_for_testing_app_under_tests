import datetime
import time
import pytest
from base.entities.actor import Actor


@pytest.fixture(scope="class")
def run_time_counter(request):
    time.sleep(1.0)
    start_time = time.perf_counter()
    print("START TIME: {0}".format(start_time))

    def stop_counter():
        end_time = time.perf_counter()
        print("END TIME: {0}".format(end_time))
        average_time = datetime.datetime.strptime(time.ctime(end_time - start_time), "%a %b %d %H:%M:%S %Y")
        min_, sec_, m_sec = average_time.minute, average_time.second, average_time.microsecond
        print(f"AVERAGE OF THE TEST CASE RUN TIME: {min_} minutes {sec_} seconds {m_sec} microseconds")
        time.sleep(1.0)

    request.addfinalizer(stop_counter)


@pytest.fixture(scope="class")
def actor():
    """
    Actor can select the funds which will participate in the template
    from the list of all funds of the client
    :return: Actor object
    """
    return Actor("credentials", 1)


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" % previousfailed.name)
