class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(number: str) -> tuple[int, int]:
            real, imaginary = number[:-1].split("+", maxsplit=1)
            return int(real), int(imaginary)

        real1, imag1 = parse(num1)
        real2, imag2 = parse(num2)
        real = real1 * real2 - imag1 * imag2
        imag = real1 * imag2 + imag1 * real2
        return f"{real}+{imag}i"