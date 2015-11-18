#include "shared.rsh"

int dimX;
int dimY;

int __attribute__((kernel)) foo(int a) {
    return a * 2;
}

int __attribute__((kernel)) goo(int a, int b) {
    return a + b;
}

static void validate(rs_allocation out) {
    bool failed = false;

    int i, j;

    for (j = 0; j < dimY; j++) {
        for (i = 0; i < dimX; i++) {
            const int actual = rsGetElementAt_int(out, i, j);
            int expected = (i + j * dimX) * 4;
            if (j < dimY / 2) {
                expected *= 2;
            }
            expected += (i + j * dimX);
            if (actual != expected) {
                failed = true;
                rsDebug("row     ", j);
                rsDebug("column  ", i);
                rsDebug("expects ", expected);
                rsDebug("got     ", actual);
            }
        }
    }

    if (failed) {
        rsDebug("FAILED", 0);
    } else {
        rsDebug("PASSED", 0);
    }

    if (failed) {
        rsSendToClientBlocking(RS_MSG_TEST_FAILED);
    } else {
        rsSendToClientBlocking(RS_MSG_TEST_PASSED);
    }
}

void entrypoint(rs_allocation in, rs_allocation out) {
    int i, j;
    for (i = 0; i < dimX; i++) {
        for (j = 0; j < dimY; j++) {
            rsSetElementAt_int(in, j * dimX + i, i, j);
        }
    }

    rsForEach(foo, in, out);
    rsForEach(foo, out, out);
    rs_script_call_t opts = {0};
    opts.xStart = 0;
    opts.xEnd = dimX;
    opts.yStart = 0;
    opts.yEnd = dimY / 2;
    rsForEachWithOptions(foo, &opts, out, out);

    rsForEach(goo, in, out, out);

    validate(out);
}