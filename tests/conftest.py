import pytest

# Only invoke this fixture once per test session
#@pytest.fixture(scope="session")

# Only invoke this fixture once per test module
#@pytest.fixture(scope="module")

# Note: Use dynamic scope to power on/off for each test (function)
#       or for each set of tests (module)
#       or for all tests (session)

@pytest.fixture(scope="module", params=["0.72", "0.8", "0.88"], ids=["VMin", "VTyp", "VMax"])
def power_vcore(force_temp, request):
    voltage = request.param
    #-=========================================================================-
    # Setup Phase
    #-=========================================================================-
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
def force_temp(request):
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

@pytest.fixture(scope="session")
def asic_regress(power_vcore, force_temp):
    return power_vcore, force_temp
