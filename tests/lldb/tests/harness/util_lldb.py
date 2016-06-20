'''Module that contains the class UtilLLDB, which provides lldb utility
methods.'''

from __future__ import absolute_import

from . import util_constants

try:
    import lldb
except ImportError:
    print('unable to import lldb')
    print('please run "lldb -P" and add to $PYTHONPATH')
    quit(util_constants.RC_TEST_ERROR)


class UtilLLDB(object):
    '''Provides utility methods to interface with lldb's python bindings.'''

    @staticmethod
    def start():
        '''Initialise the lldb debugger framework.'''
        lldb.SBDebugger_Initialize()

    @staticmethod
    def stop():
        '''Terminate the lldb debugger framework.

        Raises:
            AssertionError: If an assertion fails.
        '''
        assert lldb
        lldb.SBDebugger_Terminate()

    @staticmethod
    def create_debugger():
        '''Create an lldb debugger instance.

        Returns:
            The SBDebugger instance that was created.

        Raises:
            AssertionError: If an assertion fails.
        '''
        assert lldb
        inst = lldb.SBDebugger_Create()
        inst.SetAsync(False)
        return inst

    @staticmethod
    def destroy_debugger(dbg):
        '''Destroy the lldb debugger instance.

        Args:
            dbg: Instance of SBDebugger that is to be destroyed.

        Raises:
            AssertionError: If an assertion fails.
        '''
        assert lldb
        lldb.SBDebugger_Destroy(dbg)

    @staticmethod
    def get_module():
        '''Get the lldb module.

        Returns:
            The lldb module.

        Raises:
            AssertionError: If an assertion fails.
        '''
        assert lldb
        return lldb
