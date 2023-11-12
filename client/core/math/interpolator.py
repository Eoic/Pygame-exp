from math import sqrt


class Interpolator(object):
    def __init__(
            self,
            start=None,
            stop=None,
            seconds=None,
            fps=None,
            shape=1.0,
            middle=0.5
    ):
        self._sec = -1
        self._length = 0

        if start is None:
            start = (0, 0)

        if stop is None:
            self.stop = start
        else:
            if (seconds is None) or (fps is None):
                raise ValueError('Must specify both "seconds" and "fps".')

            if shape <= 0.0:
                raise ValueError('Argument "shape" must have a value > 0.0.')

            if not (0.0 <= middle <= 1.0):
                raise ValueError('Argument "middle" must be in range [0.0, 1.0].')

            self.stop = stop
            self.diff = [b - a for a, b in zip(start, stop)]
            self.inc = 1.0 / fps
            self.step = [a * self.inc / seconds for a in self.diff]
            self._pos = start
            self._sec = seconds
            self.seconds = seconds
            self.shape = shape
            self.mid = middle
            self.maxs = [max(a, b) for a, b in zip(start, stop)]
            self.mins = [min(a, b) for a, b in zip(start, stop)]
            self._length = None

    def next(self):
        def d(a, b, c):
            if b == 0.0:
                return c
            else:
                return a / b

        if self._sec >= 0.0:
            if self.shape == 1.0:
                factor = 1.0
            else:
                percent = 1.0 - (self._sec / self.seconds)

                if percent < 0.95:
                    if percent > self.mid:
                        k = d((1.0 - percent), (1.0 - self.mid), 1.0)
                    else:
                        k = d(percent, self.mid, 0.0)

                    if k in [0.0, 1.0]:
                        factor = k - self.shape
                    else:
                        factor = pow(k, self.shape - 1.0) - self.shape
                else:
                    if self.mid is not None:
                        self.diff = [b - a for a, b in zip(self._pos, self.stop)]
                        self.step = [a * self.inc / self._sec for a in self.diff]
                        self.mid = None

                    factor = 1.0

            self._pos = tuple([min(max(a + step * factor, mina), maxa) for a, step, mina, maxa in
                               zip(self._pos, self.step, self.mins, self.maxs)])
            self._sec -= self.inc
            return self._pos
        else:
            self._pos = self.stop
            return None

    def _get_pos(self):
        return self._pos

    def _get_length(self):
        if self._length is None:
            total = 0

            for a in self.diff:
                total += a * a
                self._length = sqrt(total)

            return self._length

    pos = property(_get_pos, doc='The location of the current vector. Read-only.')
    length = property(_get_length, doc='The length of the line. Read-only.')
