#!/usr/bin/env python3

# Copyright (C) 2016 Kaspar Schleiser <kaspar@schleiser.de>
# Copyright (C) 2016 Takuo Yonezawa <Yonezawa-T2@mail.dnp.co.jp>
#
# This file is subject to the terms and conditions of the GNU Lesser
# General Public License v2.1. See the file LICENSE in the top level
# directory for more details.

import os
import sys

sys.path.append(os.path.join(os.environ['RIOTBASE'], 'dist/tools/testrunner'))
import testrunner


def testfunc(child):
    child.expect(r"OK \(\d+ tests\)")

if __name__ == "__main__":
    sys.exit(testrunner.run(testfunc, timeout=1))
