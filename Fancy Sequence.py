class Fancy(object):

    def __init__(self):
        self.nums = []
        self.a = 1  # Cumulative multiplier
        self.b = 0  # Cumulative increment
        self.MOD = 10**9 + 7

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        # Store val normalized to the current global transformation: (val - b) / a
        # We use Fermat's Little Theorem for the modular inverse: a^(MOD-2)
        inv_a = pow(self.a, self.MOD - 2, self.MOD)
        self.nums.append(((val - self.b) * inv_a) % self.MOD)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.b = (self.b + inc) % self.MOD

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        # Update both multiplier and increment: m * (ax + b) = max + mb
        self.a = (self.a * m) % self.MOD
        self.b = (self.b * m) % self.MOD

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx >= len(self.nums):
            return -1
        # Apply the total transformation to the stored normalized value
        return (self.nums[idx] * self.a + self.b) % self.MOD
