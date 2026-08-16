#!/usr/bin/env python3
"""Tiny deterministic program used for Linux / Shell practice."""

import time


LINES = [
    "Loading dataset...",
    "Epoch 1 Loss: 1.321",
    "Epoch 2 Loss: 0.982",
    "WARNING: dataloader is slow",
    "Epoch 3 Loss: 0.721",
    "Epoch 4 Loss: 0.615",
    "Epoch 5 Loss: 0.532",
    "Training finished.",
]


def main():
    for line in LINES:
        print(line, flush=True)
        time.sleep(0.2)


if __name__ == "__main__":
    main()
