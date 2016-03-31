'''Module that contains the test TestAllocationDump2JNI.'''

from harness.test_base_remote import TestBaseRemote


class TestAllocationDump2JNI(TestBaseRemote):
    '''Tests printing the contents of allocations of a JNI apk.'''

    def get_bundle_target(self):
        '''Return string with name of bundle executable to run.

        Returns:
            A string containing the name of the binary that this test can be run
            with.
        '''
        return 'JNIAllocations'

    def test_case(self, _):
        '''Run the lldb commands that are being tested.

        Raises:
            TestFail: One of the lldb commands did not provide the expected
            output.
        '''
        # pylint: disable=line-too-long
        self.try_command('language renderscript kernel breakpoint all enable',
                         ['Breakpoints will be set on all kernels'])

        self.try_command('process continue',
                         ['resuming',
                          'stopped',
                          'stop reason = breakpoint'])

        self.try_command('breakpoint del 1',
                         ['1 breakpoints deleted'])

        # Hit second kernel
        self.try_command('process continue',
                         ['resuming',
                          'stopped',
                          'stop reason = breakpoint'])

        # uchar
        self.try_command('language renderscript allocation dump 20',
                         ['(0, 0, 0) = 0',
                          '(1, 0, 0) = 1',
                          '(2, 0, 0) = 2',
                          '(3, 0, 0) = 3',
                          '(4, 0, 0) = 4',
                          '(5, 0, 0) = 5',
                          '(6, 0, 0) = 6',
                          '(7, 0, 0) = 7',
                          '(8, 0, 0) = 8',
                          '(9, 0, 0) = 9',
                          '(10, 0, 0) = 10',
                          '(11, 0, 0) = 11',
                          '(12, 0, 0) = 12',
                          '(13, 0, 0) = 13',
                          '(14, 0, 0) = 14',
                          '(15, 0, 0) = 15',
                          '(16, 0, 0) = 16',
                          '(17, 0, 0) = 17',
                          '(18, 0, 0) = 18',
                          '(19, 0, 0) = 19',
                          '(20, 0, 0) = 20',
                          '(21, 0, 0) = 21',
                          '(22, 0, 0) = 22',
                          '(23, 0, 0) = 23'])

        # uchar2
        self.try_command('language renderscript allocation dump 21',
                         ['(0, 0, 0) = {0x00 0x01}',
                          '(1, 0, 0) = {0x02 0x03}',
                          '(0, 1, 0) = {0x04 0x05}',
                          '(1, 1, 0) = {0x06 0x07}',
                          '(0, 2, 0) = {0x08 0x09}',
                          '(1, 2, 0) = {0x0a 0x0b}',
                          '(0, 3, 0) = {0x0c 0x0d}',
                          '(1, 3, 0) = {0x0e 0x0f}',
                          '(0, 4, 0) = {0x10 0x11}',
                          '(1, 4, 0) = {0x12 0x13}',
                          '(0, 5, 0) = {0x14 0x15}',
                          '(1, 5, 0) = {0x16 0x17}'])

        # uchar3
        self.try_command('language renderscript allocation dump 22',
                         ['(0, 0, 0) = {0x00 0x01 0x02}',
                          '(1, 0, 0) = {0x04 0x05 0x06}',
                          '(2, 0, 0) = {0x08 0x09 0x0a}',
                          '(3, 0, 0) = {0x0c 0x0d 0x0e}',
                          '(4, 0, 0) = {0x10 0x11 0x12}',
                          '(5, 0, 0) = {0x14 0x15 0x16}'])

        # uchar4
        self.try_command('language renderscript allocation dump 23',
                         ['(0, 0, 0) = {0x00 0x01 0x02 0x03}',
                          '(1, 0, 0) = {0x04 0x05 0x06 0x07}',
                          '(2, 0, 0) = {0x08 0x09 0x0a 0x0b}',
                          '(3, 0, 0) = {0x0c 0x0d 0x0e 0x0f}',
                          '(4, 0, 0) = {0x10 0x11 0x12 0x13}',
                          '(5, 0, 0) = {0x14 0x15 0x16 0x17}'])

        # ushort
        self.try_command('language renderscript allocation dump 24',
                         ['(0, 0, 0) = 0',
                          '(1, 0, 0) = 1',
                          '(2, 0, 0) = 2',
                          '(3, 0, 0) = 3',
                          '(4, 0, 0) = 4',
                          '(5, 0, 0) = 5',
                          '(6, 0, 0) = 6',
                          '(7, 0, 0) = 7',
                          '(8, 0, 0) = 8',
                          '(9, 0, 0) = 9',
                          '(10, 0, 0) = 10',
                          '(11, 0, 0) = 11',
                          '(12, 0, 0) = 12',
                          '(13, 0, 0) = 13',
                          '(14, 0, 0) = 14',
                          '(15, 0, 0) = 15',
                          '(16, 0, 0) = 16',
                          '(17, 0, 0) = 17',
                          '(18, 0, 0) = 18',
                          '(19, 0, 0) = 19',
                          '(20, 0, 0) = 20',
                          '(21, 0, 0) = 21',
                          '(22, 0, 0) = 22',
                          '(23, 0, 0) = 23'])

        # ushort2
        self.try_command('language renderscript allocation dump 25',
                         ['(0, 0, 0) = {0x0000 0x0001}',
                          '(1, 0, 0) = {0x0002 0x0003}',
                          '(2, 0, 0) = {0x0004 0x0005}',
                          '(3, 0, 0) = {0x0006 0x0007}',
                          '(4, 0, 0) = {0x0008 0x0009}',
                          '(5, 0, 0) = {0x000a 0x000b}',
                          '(6, 0, 0) = {0x000c 0x000d}',
                          '(7, 0, 0) = {0x000e 0x000f}',
                          '(8, 0, 0) = {0x0010 0x0011}',
                          '(9, 0, 0) = {0x0012 0x0013}',
                          '(10, 0, 0) = {0x0014 0x0015}',
                          '(11, 0, 0) = {0x0016 0x0017}'])

        # ushort3
        self.try_command('language renderscript allocation dump 26',
                         ['(0, 0, 0) = {0x0000 0x0001 0x0002}',
                          '(0, 1, 0) = {0x0004 0x0005 0x0006}',
                          '(0, 2, 0) = {0x0008 0x0009 0x000a}',
                          '(0, 3, 0) = {0x000c 0x000d 0x000e}',
                          '(0, 4, 0) = {0x0010 0x0011 0x0012}',
                          '(0, 5, 0) = {0x0014 0x0015 0x0016}'])

        # ushort4
        self.try_command('language renderscript allocation dump 27',
                         ['(0, 0, 0) = {0x0000 0x0001 0x0002 0x0003}',
                          '(1, 0, 0) = {0x0004 0x0005 0x0006 0x0007}',
                          '(2, 0, 0) = {0x0008 0x0009 0x000a 0x000b}',
                          '(3, 0, 0) = {0x000c 0x000d 0x000e 0x000f}',
                          '(4, 0, 0) = {0x0010 0x0011 0x0012 0x0013}',
                          '(5, 0, 0) = {0x0014 0x0015 0x0016 0x0017}'])

        # uint
        self.try_command('language renderscript allocation dump 28',
                         ['(0, 0, 0) = 0',
                          '(1, 0, 0) = 1',
                          '(2, 0, 0) = 2',
                          '(3, 0, 0) = 3',
                          '(4, 0, 0) = 4',
                          '(5, 0, 0) = 5',
                          '(6, 0, 0) = 6',
                          '(7, 0, 0) = 7',
                          '(8, 0, 0) = 8',
                          '(9, 0, 0) = 9',
                          '(10, 0, 0) = 10',
                          '(11, 0, 0) = 11',
                          '(12, 0, 0) = 12',
                          '(13, 0, 0) = 13',
                          '(14, 0, 0) = 14',
                          '(15, 0, 0) = 15',
                          '(16, 0, 0) = 16',
                          '(17, 0, 0) = 17',
                          '(18, 0, 0) = 18',
                          '(19, 0, 0) = 19',
                          '(20, 0, 0) = 20',
                          '(21, 0, 0) = 21',
                          '(22, 0, 0) = 22',
                          '(23, 0, 0) = 23'])

        # uint2
        self.try_command('language renderscript allocation dump 29',
                         ['(0, 0, 0) = {0x00000000 0x00000001}',
                          '(1, 0, 0) = {0x00000002 0x00000003}',
                          '(2, 0, 0) = {0x00000004 0x00000005}',
                          '(3, 0, 0) = {0x00000006 0x00000007}',
                          '(4, 0, 0) = {0x00000008 0x00000009}',
                          '(5, 0, 0) = {0x0000000a 0x0000000b}',
                          '(6, 0, 0) = {0x0000000c 0x0000000d}',
                          '(7, 0, 0) = {0x0000000e 0x0000000f}',
                          '(8, 0, 0) = {0x00000010 0x00000011}',
                          '(9, 0, 0) = {0x00000012 0x00000013}',
                          '(10, 0, 0) = {0x00000014 0x00000015}',
                          '(11, 0, 0) = {0x00000016 0x00000017}'])

        # uint3
        self.try_command('language renderscript allocation dump 30',
                         ['(0, 0, 0) = {0x00000000 0x00000001 0x00000002}',
                          '(1, 0, 0) = {0x00000004 0x00000005 0x00000006}',
                          '(2, 0, 0) = {0x00000008 0x00000009 0x0000000a}',
                          '(3, 0, 0) = {0x0000000c 0x0000000d 0x0000000e}',
                          '(4, 0, 0) = {0x00000010 0x00000011 0x00000012}',
                          '(5, 0, 0) = {0x00000014 0x00000015 0x00000016}'])

        # uint4
        self.try_command('language renderscript allocation dump 31',
                         ['(0, 0, 0) = {0x00000000 0x00000001 0x00000002 0x00000003}',
                          '(0, 0, 1) = {0x00000004 0x00000005 0x00000006 0x00000007}',
                          '(0, 0, 2) = {0x00000008 0x00000009 0x0000000a 0x0000000b}',
                          '(0, 0, 3) = {0x0000000c 0x0000000d 0x0000000e 0x0000000f}',
                          '(0, 0, 4) = {0x00000010 0x00000011 0x00000012 0x00000013}',
                          '(0, 0, 5) = {0x00000014 0x00000015 0x00000016 0x00000017}'])

        # ulong
        self.try_command('language renderscript allocation dump 32',
                         ['(0, 0, 0) = 0',
                          '(1, 0, 0) = 1',
                          '(2, 0, 0) = 2',
                          '(3, 0, 0) = 3',
                          '(0, 1, 0) = 4',
                          '(1, 1, 0) = 5',
                          '(2, 1, 0) = 6',
                          '(3, 1, 0) = 7',
                          '(0, 2, 0) = 8',
                          '(1, 2, 0) = 9',
                          '(2, 2, 0) = 10',
                          '(3, 2, 0) = 11',
                          '(0, 0, 1) = 12',
                          '(1, 0, 1) = 13',
                          '(2, 0, 1) = 14',
                          '(3, 0, 1) = 15',
                          '(0, 1, 1) = 16',
                          '(1, 1, 1) = 17',
                          '(2, 1, 1) = 18',
                          '(3, 1, 1) = 19',
                          '(0, 2, 1) = 20',
                          '(1, 2, 1) = 21',
                          '(2, 2, 1) = 22',
                          '(3, 2, 1) = 23'])

        # ulong2
        self.try_command('language renderscript allocation dump 33',
                         ['(0, 0, 0) = {0x0000000000000000 0x0000000000000001}',
                          '(1, 0, 0) = {0x0000000000000002 0x0000000000000003}',
                          '(2, 0, 0) = {0x0000000000000004 0x0000000000000005}',
                          '(3, 0, 0) = {0x0000000000000006 0x0000000000000007}',
                          '(4, 0, 0) = {0x0000000000000008 0x0000000000000009}',
                          '(5, 0, 0) = {0x000000000000000a 0x000000000000000b}',
                          '(6, 0, 0) = {0x000000000000000c 0x000000000000000d}',
                          '(7, 0, 0) = {0x000000000000000e 0x000000000000000f}',
                          '(8, 0, 0) = {0x0000000000000010 0x0000000000000011}',
                          '(9, 0, 0) = {0x0000000000000012 0x0000000000000013}',
                          '(10, 0, 0) = {0x0000000000000014 0x0000000000000015}',
                          '(11, 0, 0) = {0x0000000000000016 0x0000000000000017}'])

        # ulong3
        self.try_command('language renderscript allocation dump 34',
                         ['(0, 0, 0) = {0x0000000000000000 0x0000000000000001 0x0000000000000002}',
                          '(1, 0, 0) = {0x0000000000000004 0x0000000000000005 0x0000000000000006}',
                          '(2, 0, 0) = {0x0000000000000008 0x0000000000000009 0x000000000000000a}',
                          '(3, 0, 0) = {0x000000000000000c 0x000000000000000d 0x000000000000000e}',
                          '(4, 0, 0) = {0x0000000000000010 0x0000000000000011 0x0000000000000012}',
                          '(5, 0, 0) = {0x0000000000000014 0x0000000000000015 0x0000000000000016}'])

        # ulong4
        self.try_command('language renderscript allocation dump 35',
                         ['(0, 0, 0) = {0x0000000000000000 0x0000000000000001 '
                                       '0x0000000000000002 0x0000000000000003}',
                          '(1, 0, 0) = {0x0000000000000004 0x0000000000000005 '
                                       '0x0000000000000006 0x0000000000000007}',
                          '(2, 0, 0) = {0x0000000000000008 0x0000000000000009 '
                                       '0x000000000000000a 0x000000000000000b}',
                          '(3, 0, 0) = {0x000000000000000c 0x000000000000000d '
                                       '0x000000000000000e 0x000000000000000f}',
                          '(4, 0, 0) = {0x0000000000000010 0x0000000000000011 '
                                       '0x0000000000000012 0x0000000000000013}',
                          '(5, 0, 0) = {0x0000000000000014 0x0000000000000015 '
                                       '0x0000000000000016 0x0000000000000017}'])

        self.try_command('breakpoint del 2',
                         ['1 breakpoints deleted'])

        # Hit third kernel
        self.try_command('process continue',
                         ['resuming',
                          'stopped',
                          'stop reason = breakpoint'])

        # Test that uint allocation has been squared by square_kernel
        self.try_command('language renderscript allocation dump 28',
                         ['(0, 0, 0) = 0',
                          '(1, 0, 0) = 1',
                          '(2, 0, 0) = 4',
                          '(3, 0, 0) = 9',
                          '(4, 0, 0) = 16',
                          '(5, 0, 0) = 25',
                          '(6, 0, 0) = 36',
                          '(7, 0, 0) = 49',
                          '(8, 0, 0) = 64',
                          '(9, 0, 0) = 81',
                          '(10, 0, 0) = 100',
                          '(11, 0, 0) = 121',
                          '(12, 0, 0) = 144',
                          '(13, 0, 0) = 169',
                          '(14, 0, 0) = 196',
                          '(15, 0, 0) = 225',
                          '(16, 0, 0) = 256',
                          '(17, 0, 0) = 289',
                          '(18, 0, 0) = 324',
                          '(19, 0, 0) = 361',
                          '(20, 0, 0) = 400',
                          '(21, 0, 0) = 441',
                          '(22, 0, 0) = 484',
                          '(23, 0, 0) = 529'])

        # half
        self.try_command('language renderscript allocation dump 36',
                         ['(0, 0, 0) = inf',
                          '(1, 0, 0) = 1',
                          '(2, 0, 0) = 0.5',
                          '(3, 0, 0) = 0.333252',
                          '(4, 0, 0) = 0.25',
                          '(5, 0, 0) = 0.199951',
                          '(6, 0, 0) = 0.166626',
                          '(7, 0, 0) = 0.142822',
                          '(8, 0, 0) = 0.125',
                          '(9, 0, 0) = 0.111084',
                          '(10, 0, 0) = 0.0999756',
                          '(11, 0, 0) = 0.0908813',
                          '(12, 0, 0) = 0.083313',
                          '(13, 0, 0) = 0.0769043',
                          '(14, 0, 0) = 0.0714111',
                          '(15, 0, 0) = 0.0666504',
                          '(16, 0, 0) = 0.0625',
                          '(17, 0, 0) = 0.0588379',
                          '(18, 0, 0) = 0.055542',
                          '(19, 0, 0) = 0.0526428',
                          '(20, 0, 0) = 0.0499878',
                          '(21, 0, 0) = 0.0476074',
                          '(22, 0, 0) = 0.0454407',
                          '(23, 0, 0) = 0.0434875'])

        # half2
        self.try_command('language renderscript allocation dump 37',
                         ['(0, 0, 0) = {inf 1}',
                          '(1, 0, 0) = {0.5 0.333252}',
                          '(2, 0, 0) = {0.25 0.199951}',
                          '(3, 0, 0) = {0.166626 0.142822}',
                          '(4, 0, 0) = {0.125 0.111084}',
                          '(5, 0, 0) = {0.0999756 0.0908813}',
                          '(6, 0, 0) = {0.083313 0.0769043}',
                          '(7, 0, 0) = {0.0714111 0.0666504}',
                          '(8, 0, 0) = {0.0625 0.0588379}',
                          '(9, 0, 0) = {0.055542 0.0526428}',
                          '(10, 0, 0) = {0.0499878 0.0476074}',
                          '(11, 0, 0) = {0.0454407 0.0434875}'])

        # half3
        self.try_command('language renderscript allocation dump 38',
                         ['(0, 0, 0) = {inf 1 0.5}',
                          '(0, 1, 0) = {0.25 0.199951 0.166626}',
                          '(0, 2, 0) = {0.125 0.111084 0.0999756}',
                          '(0, 3, 0) = {0.083313 0.0769043 0.0714111}',
                          '(0, 4, 0) = {0.0625 0.0588379 0.055542}',
                          '(0, 5, 0) = {0.0499878 0.0476074 0.0454407}'])

        # half4
        self.try_command('language renderscript allocation dump 39',
                         ['(0, 0, 0) = {inf 1 0.5 0.333252}',
                          '(1, 0, 0) = {0.25 0.199951 0.166626 0.142822}',
                          '(2, 0, 0) = {0.125 0.111084 0.0999756 0.0908813}',
                          '(3, 0, 0) = {0.083313 0.0769043 0.0714111 0.0666504}',
                          '(4, 0, 0) = {0.0625 0.0588379 0.055542 0.0526428}',
                          '(5, 0, 0) = {0.0499878 0.0476074 0.0454407 0.0434875}'])

        # float
        self.try_command('language renderscript allocation dump 40',
                         ['(0, 0, 0) = inf',
                          '(1, 0, 0) = 1',
                          '(2, 0, 0) = 0.5',
                          '(3, 0, 0) = 0.333333',
                          '(4, 0, 0) = 0.25',
                          '(5, 0, 0) = 0.2',
                          '(6, 0, 0) = 0.166667',
                          '(7, 0, 0) = 0.142857',
                          '(8, 0, 0) = 0.125',
                          '(9, 0, 0) = 0.111111',
                          '(10, 0, 0) = 0.1',
                          '(11, 0, 0) = 0.0909091',
                          '(12, 0, 0) = 0.0833333',
                          '(13, 0, 0) = 0.0769231',
                          '(14, 0, 0) = 0.0714286',
                          '(15, 0, 0) = 0.0666667',
                          '(16, 0, 0) = 0.0625',
                          '(17, 0, 0) = 0.0588235',
                          '(18, 0, 0) = 0.0555556',
                          '(19, 0, 0) = 0.0526316',
                          '(20, 0, 0) = 0.05',
                          '(21, 0, 0) = 0.047619',
                          '(22, 0, 0) = 0.0454545',
                          '(23, 0, 0) = 0.0434783'])

        # float2
        self.try_command('language renderscript allocation dump 41',
                         ['(0, 0, 0) = {inf 1}',
                          '(1, 0, 0) = {0.5 0.333333}',
                          '(2, 0, 0) = {0.25 0.2}',
                          '(3, 0, 0) = {0.166667 0.142857}',
                          '(4, 0, 0) = {0.125 0.111111}',
                          '(5, 0, 0) = {0.1 0.0909091}',
                          '(6, 0, 0) = {0.0833333 0.0769231}',
                          '(7, 0, 0) = {0.0714286 0.0666667}',
                          '(8, 0, 0) = {0.0625 0.0588235}',
                          '(9, 0, 0) = {0.0555556 0.0526316}',
                          '(10, 0, 0) = {0.05 0.047619}',
                          '(11, 0, 0) = {0.0454545 0.0434783}'])

        # float3
        self.try_command('language renderscript allocation dump 42',
                         ['(0, 0, 0) = {inf 1 0.5}',
                          '(1, 0, 0) = {0.25 0.2 0.166667}',
                          '(2, 0, 0) = {0.125 0.111111 0.1}',
                          '(3, 0, 0) = {0.0833333 0.0769231 0.0714286}',
                          '(4, 0, 0) = {0.0625 0.0588235 0.0555556}',
                          '(5, 0, 0) = {0.05 0.047619 0.0454545}'])

        # float4
        self.try_command('language renderscript allocation dump 43',
                         ['(0, 0, 0) = {inf 1 0.5 0.333333}',
                          '(1, 0, 0) = {0.25 0.2 0.166667 0.142857}',
                          '(2, 0, 0) = {0.125 0.111111 0.1 0.0909091}',
                          '(0, 1, 0) = {0.0833333 0.0769231 0.0714286 0.0666667}',
                          '(1, 1, 0) = {0.0625 0.0588235 0.0555556 0.0526316}',
                          '(2, 1, 0) = {0.05 0.047619 0.0454545 0.0434783}'])

        # double
        self.try_command('language renderscript allocation dump 44',
                         ['(0, 0, 0) = inf',
                          '(1, 0, 0) = 1',
                          '(2, 0, 0) = 0.5',
                          '(3, 0, 0) = 0.333333333333333',
                          '(4, 0, 0) = 0.25',
                          '(5, 0, 0) = 0.2',
                          '(6, 0, 0) = 0.166666666666667',
                          '(7, 0, 0) = 0.142857142857143',
                          '(8, 0, 0) = 0.125',
                          '(9, 0, 0) = 0.111111111111111',
                          '(10, 0, 0) = 0.1',
                          '(11, 0, 0) = 0.0909090909090909',
                          '(12, 0, 0) = 0.0833333333333333',
                          '(13, 0, 0) = 0.0769230769230769',
                          '(14, 0, 0) = 0.0714285714285714',
                          '(15, 0, 0) = 0.0666666666666667',
                          '(16, 0, 0) = 0.0625',
                          '(17, 0, 0) = 0.0588235294117647',
                          '(18, 0, 0) = 0.0555555555555556',
                          '(19, 0, 0) = 0.0526315789473684',
                          '(20, 0, 0) = 0.05',
                          '(21, 0, 0) = 0.0476190476190476',
                          '(22, 0, 0) = 0.0454545454545455',
                          '(23, 0, 0) = 0.0434782608695652'])

        # double2
        self.try_command('language renderscript allocation dump 45',
                         ['(0, 0, 0) = {inf 1}',
                          '(1, 0, 0) = {0.5 0.333333333333333}',
                          '(2, 0, 0) = {0.25 0.2}',
                          '(3, 0, 0) = {0.166666666666667 0.142857142857143}',
                          '(0, 0, 1) = {0.125 0.111111111111111}',
                          '(1, 0, 1) = {0.1 0.0909090909090909}',
                          '(2, 0, 1) = {0.0833333333333333 0.0769230769230769}',
                          '(3, 0, 1) = {0.0714285714285714 0.0666666666666667}',
                          '(0, 0, 2) = {0.0625 0.0588235294117647}',
                          '(1, 0, 2) = {0.0555555555555556 0.0526315789473684}',
                          '(2, 0, 2) = {0.05 0.0476190476190476}',
                          '(3, 0, 2) = {0.0454545454545455 0.0434782608695652}'])

        # double3
        self.try_command('language renderscript allocation dump 46',
                         ['(0, 0, 0) = {inf 1 0.5}',
                          '(0, 1, 0) = {0.25 0.2 0.166666666666667}',
                          '(0, 0, 1) = {0.125 0.111111111111111 0.1}',
                          '(0, 1, 1) = {0.0833333333333333 0.0769230769230769 '
                                       '0.0714285714285714}',
                          '(0, 0, 2) = {0.0625 0.0588235294117647 0.0555555555555556}',
                          '(0, 1, 2) = {0.05 0.0476190476190476 0.0454545454545455}'])

        # double4
        self.try_command('language renderscript allocation dump 47',
                         ['(0, 0, 0) = {inf 1 0.5 0.333333333333333}',
                          '(0, 1, 0) = {0.25 0.2 0.166666666666667 0.142857142857143}',
                          '(0, 0, 1) = {0.125 0.111111111111111 0.1 0.0909090909090909}',
                          '(0, 1, 1) = {0.0833333333333333 0.0769230769230769 '
                                       '0.0714285714285714 0.0666666666666667}',
                          '(0, 0, 2) = {0.0625 0.0588235294117647 '
                                       '0.0555555555555556 0.0526315789473684}',
                          '(0, 1, 2) = {0.05 0.0476190476190476 '
                                       '0.0454545454545455 0.0434782608695652}'])
