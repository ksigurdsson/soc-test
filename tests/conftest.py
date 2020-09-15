import pytest

# Only invoke this fixture once per test session
#@pytest.fixture(scope="session")

# Only invoke this fixture once per test module
#@pytest.fixture(scope="module")

# Note: Use dynamic scope to power on/off for each test (function)
#       or for each set of tests (module)
#       or for all tests (session)

def pytest_addoption(parser):
    parser.addoption("--sim",
                     action="store_true",
                     help="run test(s) in simulation environment")



@pytest.fixture(scope="module", params=["0.72", "0.8", "0.88"], ids=["VMin", "VTyp", "VMax"])
def chip_init(env_init, request):

    #-=========================================================================-
    # Setup Phase
    #-=========================================================================-

    if request.config.getoption("sim"):
        voltage = 0
        print("SIMULATING")
    else:
        voltage = request.param
        print("  Powering ON VCore:", voltage)

    # Measure VCore - if not reading what was requested then raise an exception
    # Note: that if an exception happens during the setup code (before the yield keyword),
    # the teardown code (after the yield) will not be called

    #-=========================================================================-
    # Setup Phase complete - run test(s)
    #-=========================================================================-
    yield voltage

    #-=========================================================================-
    # Teardown Phase
    #-=========================================================================-
    
    # Note: An alternative option for executing teardown code is to make use of the
    # addfinalizer method of the request-context object to register finalization functions.
    print("  Powering OFF VCore")
    

@pytest.fixture(scope="session", params=["0", "25", "125"], ids=["TMin", "TTyp", "TMax"])
def env_init(request):
    temp = request.param
    #-=========================================================================-
    # Setup Phase
    #-=========================================================================-
    print("  Forcing Temp:", temp)

    # Measure temp - if not reading what was requested then raise an exception
    # Note: that if an exception happens during the setup code (before the yield keyword),
    # the teardown code (after the yield) will not be called

    #-=========================================================================-
    # Setup Phase complete - run test(s)
    #-=========================================================================-
    yield temp

    #-=========================================================================-
    # Teardown Phase
    #-=========================================================================-
    
    # Note: An alternative option for executing teardown code is to make use of the
    # addfinalizer method of the request-context object to register finalization functions.
    print("  Releasing Temp Force")

#@pytest.fixture(scope="session")
#def asic_regress(chip_init, env_init):
#    return chip_init, env_init
