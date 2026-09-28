class Cipher:
    def __init__(self, salt: str) -> None:
        self.salt = salt
        self.cipher = []
        for ch in salt + "".join(chr(ord("a") + i) for i in range(26) if i != 9):
            if ch in self.cipher:
                continue
            self.cipher.append(ch)
        self.cipher_table = []
        for i, ch in enumerate(self.cipher):
            if i % 5 == 0:
                self.cipher_table.append([])
            self.cipher_table[-1].append(ch)
        self.cipher_map: dict[str, tuple[int, int]] = {
            ch: (r, c)
            for r, chars in enumerate(self.cipher_table)
            for c, ch in enumerate(chars)
        }

    def encrypt(self, decrypted: str) -> str:
        word = self.pad_and_deduplicate(decrypted)
        bigrams = [c1 + c2 for c1, c2 in zip(word[::2], word[1::2])]
        encrypted = ""
        for ch1, ch2 in bigrams:
            r1, c1 = self.cipher_map[ch1]
            r2, c2 = self.cipher_map[ch2]
            if r1 == r2:
                encrypted += self.cipher_table[r1][(c1 + 1) % 5]
                encrypted += self.cipher_table[r1][(c2 + 1) % 5]
            elif c1 == c2:
                encrypted += self.cipher_table[(r1 + 1) % 5][c1]
                encrypted += self.cipher_table[(r2 + 1) % 5][c1]
            else:
                encrypted += self.cipher_table[r1][c2]
                encrypted += self.cipher_table[r2][c1]
        return encrypted

    def pad_and_deduplicate(self, word: str) -> str:
        result = []
        last_ch = ""
        for ch in word:
            if ch == last_ch:
                result.append("x")
            result.append(ch)
            last_ch = ch
        if len(result) % 2 == 1:
            result.append("x")
        return "".join(result)

    def decrypt(self, encrypted: str) -> str:
        bigrams = [c1 + c2 for c1, c2 in zip(encrypted[::2], encrypted[1::2])]
        decrypted = ""
        for ch1, ch2 in bigrams:
            r1, c1 = self.cipher_map[ch1]
            r2, c2 = self.cipher_map[ch2]
            if r1 == r2:
                decrypted += self.cipher_table[r1][(c1 - 1) % 5]
                decrypted += self.cipher_table[r1][(c2 - 1) % 5]
            elif c1 == c2:
                decrypted += self.cipher_table[(r1 - 1) % 5][c1]
                decrypted += self.cipher_table[(r2 - 1) % 5][c1]
            else:
                decrypted += self.cipher_table[r1][c2]
                decrypted += self.cipher_table[r2][c1]

        return decrypted


def solve_23(file: str) -> str:
    print(Cipher("playfair").encrypt("flawless"))
    return Cipher("powerplant").decrypt(file)
