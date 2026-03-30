class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "EMPTY_STR_DATA"
        return "\n\n".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY_STR_DATA":
            return []
        return s.split("\n\n")
