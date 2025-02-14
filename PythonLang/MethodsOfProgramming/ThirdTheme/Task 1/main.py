from typing import List, Sequence
from itertools import product


def find_longest_common_subsequence(
        len_seq_a: int,
        sequence_a: Sequence[int],
        len_seq_b: int,
        sequence_b: Sequence[int]
) -> List[int]:
    lcs_length_table: List[List[int]] = [[0] * (len_seq_b + 1) for _ in range(len_seq_a + 1)]

    for i, j in product(range(1, len_seq_a + 1), range(1, len_seq_b + 1)):
        if sequence_a[i - 1] == sequence_b[j - 1]:
            lcs_length_table[i][j] = lcs_length_table[i - 1][j - 1] + 1
        else:
            lcs_length_table[i][j] = max(lcs_length_table[i - 1][j], lcs_length_table[i][j - 1])

    longest_common_subseq: List[int] = []
    i: int = len_seq_a
    j: int = len_seq_b
    while i > 0 and j > 0:
        if sequence_a[i - 1] == sequence_b[j - 1]:
            longest_common_subseq.append(sequence_a[i - 1])
            i -= 1
            j -= 1
        elif lcs_length_table[i - 1][j] == lcs_length_table[i][j]:
            i -= 1
        else:
            j -= 1

    return longest_common_subseq[::-1]


def main() -> None:
    len_seq_a: int = int(input())
    sequence_a: List[int] = list(map(int, input().split()))
    len_seq_b: int = int(input())
    sequence_b: List[int] = list(map(int, input().split()))

    longest_common_subseq: List[int] = find_longest_common_subsequence(len_seq_a, sequence_a, len_seq_b, sequence_b)
    print(' '.join(map(str, longest_common_subseq)))


if __name__ == "__main__":
    main()