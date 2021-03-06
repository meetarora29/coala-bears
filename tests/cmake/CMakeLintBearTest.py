import os

from bears.cmake.CMakeLintBear import CMakeLintBear
from coalib.misc.ContextManagers import prepare_file
from tests.LocalBearTestHelper import verify_local_bear


good_file = 'project(FooBar C)\nset(VERSION 0)\n'

bad_file_mixes_case = 'ProJeCt(FooBar C)\nseT(VERSION 0)\n'


conf_file = os.path.join(os.path.dirname(__file__),
                         "test_files",
                         "cmake_config.txt")


CMakeLintBearTest = verify_local_bear(
    CMakeLintBear,
    valid_files=(good_file,),
    invalid_files=(bad_file_mixes_case,),
    tempfile_kwargs={"suffix": ".cmake"})


CMakeLintBearConfigTest = verify_local_bear(
    CMakeLintBear,
    valid_files=(good_file, bad_file_mixes_case),
    invalid_files=(),
    tempfile_kwargs={"suffix": ".cmake"},
    settings={'cmakelint_config': conf_file})
