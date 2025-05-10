# Hamiltonian Analysis for Nonlinear Force: \( F_x = -k x^3 \)

This repository solves Problem 13.26 from a classical mechanics textbook using both analytical and computational tools.

## Problem Statement

Find the Hamiltonian \( H \) for a mass \( m \) confined to move along the \( x \)-axis and subject to a nonlinear force:
\[
F_x = -k x^3 \quad \text{where} \quad k > 0
\]
Sketch and describe the phase-space orbits.

## Solution Summary

- The potential energy is:
  \[
  U(x) = \frac{1}{4} k x^4
  \]

- The Hamiltonian is:
  \[
  H = \frac{p^2}{2m} + \frac{1}{4} k x^4
  \]

- The phase-space trajectories follow:
  \[
  \frac{p^2}{2m} + \frac{1}{4} k x^4 = E
  \]
  which forms closed orbits in the \( (x, p) \) plane resembling flattened ellipses.

## Files

- `phase_space_plot.py`: Python script that plots the phase-space orbit
- `hamiltonian_solution.tex`: LaTeX document with step-by-step derivation
