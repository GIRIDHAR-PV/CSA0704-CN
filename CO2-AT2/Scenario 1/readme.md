# Error Detection & Correction

## Overview
This project demonstrates basic error detection techniques used in computer networking to identify corrupted data during transmission over a noisy channel.

## Concepts
- **Parity Bit (Even Parity):** Adds an extra bit to ensure the total count of 1s in the binary sequence is even. It can detect single-bit errors.
- **Checksum:** Sums up the numerical (ASCII) values of all characters in a message.

## Comparison
- **Parity Bit:** Lightweight and fast, but fails if an even number of bits are flipped (e.g., two bits flip, leaving the parity count unchanged).
- **Checksum:** More robust than a simple parity bit because it sums character values across the whole payload, catching multiple-bit corruptions effectively.
