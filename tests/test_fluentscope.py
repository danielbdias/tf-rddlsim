from tfrddlsim.rddl2tf.fluentscope import TensorFluentScope

import unittest


class TestTensorScope(unittest.TestCase):

    def test_broadcast(self):
        tests = [
            (([], []), ([], [], [])),
            ((['?r'], []), (['?r'], [], [])),
            (([], ['?r']), (['?r'], [], [])),
            ((['?r'], ['?r']), (['?r'], [], [])),
            ((['?s', '?r'], []), (['?s', '?r'], [], [])),
            (([], ['?s', '?r']), (['?s', '?r'], [], [])),
            ((['?s', '?r'], ['?r']), (['?s', '?r'], [], [])),
            ((['?r'], ['?s', '?r']), (['?s', '?r'], [], [])),
            ((['?r', '?s'], ['?r']), (['?s', '?r'], [1, 0], [])),
            ((['?r'], ['?r', '?s']), (['?s', '?r'], [], [1, 0])),
            ((['?r', '?s', '?t'], []), (['?r', '?s', '?t'], [], [])),
            (([], ['?r', '?s', '?t']), (['?r', '?s', '?t'], [], [])),
            ((['?r', '?s', '?t'], ['?r']), (['?s', '?t', '?r'], [2, 0, 1], [])),
            ((['?r'], ['?r', '?s', '?t']), (['?s', '?t', '?r'], [], [2, 0, 1])),
            ((['?r', '?s', '?t'], ['?s']), (['?r', '?t', '?s'], [0, 2, 1], [])),
            ((['?s'], ['?r', '?s', '?t']), (['?r', '?t', '?s'], [], [0, 2, 1])),
            ((['?r', '?s', '?t'], ['?t']), (['?r', '?s', '?t'], [], [])),
            ((['?t'], ['?r', '?s', '?t']), (['?r', '?s', '?t'], [], [])),
            ((['?r', '?s', '?t'], ['?s', '?t']), (['?r', '?s', '?t'], [], [])),
            ((['?s', '?t'], ['?r', '?s', '?t']), (['?r', '?s', '?t'], [], [])),
            ((['?r', '?s', '?t'], ['?t', '?s']), (['?r', '?t', '?s'], [0, 2, 1], [])),
            ((['?t', '?s'], ['?r', '?s', '?t']), (['?r', '?t', '?s'], [], [0, 2, 1])),
            ((['?r', '?s', '?t'], ['?t', '?r']), (['?s', '?t', '?r'], [2, 0, 1], [])),
            ((['?t', '?r'], ['?r', '?s', '?t']), (['?s', '?t', '?r'], [], [2, 0, 1])),
            ((['?r', '?s', '?t'], ['?r', '?t']), (['?s', '?r', '?t'], [1, 0, 2], [])),
            ((['?r', '?t'], ['?r', '?s', '?t']), (['?s', '?r', '?t'], [], [1, 0, 2])),
            ((['?r', '?s', '?t'], ['?r', '?s']), (['?t', '?r', '?s'], [1, 2, 0], [])),
            ((['?r', '?s'], ['?r', '?s', '?t']), (['?t', '?r', '?s'], [], [1, 2, 0])),
            ((['?r', '?s', '?t'], ['?s', '?r']), (['?t', '?s', '?r'], [2, 1, 0], [])),
            ((['?s', '?r'], ['?r', '?s', '?t']), (['?t', '?s', '?r'], [], [2, 1, 0])),
        ]

        for (s1, s2), (s, p1, p2) in tests:
            scope, perm1, perm2 = TensorFluentScope.broadcast(s1, s2)
            self.assertListEqual(perm1, p1)
            self.assertListEqual(perm2, p2)
            self.assertListEqual(scope, s)
