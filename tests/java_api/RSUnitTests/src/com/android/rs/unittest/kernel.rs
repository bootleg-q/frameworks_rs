/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "shared.rsh"

int *ain;
int *aout;
int dimX;
static bool failed = false;

void init_vars(int *out) {
    *out = 7;
}


int RS_KERNEL root(int ain, uint32_t x) {
    _RS_ASSERT(ain == 7);
    return ain + x;
}

static bool test_root_output() {
    bool failed = false;
    int i;

    for (i = 0; i < dimX; i++) {
        _RS_ASSERT(aout[i] == (i + ain[i]));
    }

    if (failed) {
        rsDebug("test_root_output FAILED", 0);
    }
    else {
        rsDebug("test_root_output PASSED", 0);
    }

    return failed;
}

void verify_root() {
    failed |= test_root_output();
}

void kernel_test() {
    if (failed) {
        rsSendToClientBlocking(RS_MSG_TEST_FAILED);
    }
    else {
        rsSendToClientBlocking(RS_MSG_TEST_PASSED);
    }
}
