class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        la, lb = len(A), len(B)
        if la!=lb:
            return False
        elif not la and not lb:
            return True
        for i in range(0, la):
            if A[i]==B[0] and B==A[i:]+A[:i]:
                return True
        return False