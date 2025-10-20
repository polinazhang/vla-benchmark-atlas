# Contributing

Thanks for helping improve the VLA Benchmark Atlas! This document explains how to propose changes and keep the catalog consistent.

## Project Overview

- Benchmark definitions live in `benchmarks/datasets.yaml`.
- Simulator entries live in `benchmarks/simulators.yaml`.
- `python generate.py` reads both YAML files and regenerates the rendered Markdown in `tables/`.
- `README.md` is automatically rebuilt by `generate.py`, so never edit it by hand.

## Making Changes

1. Fork and clone the repository or work in a feature branch.
2. Edit the YAML files. 
3. Run `python generate.py` to update `tables/datasets.md`, `tables/simulators.md`, and `README.md`.
4. Commit both your YAML edits and the regenerated Markdown files.
5. Open a pull request with a short description of your changes.
*If you prefer, just submit the YAML changes. The author will handle regeneration.*

## Adding a New Dataset

- Add a new entry to `benchmarks/datasets.yaml`.
- Include the required fields following existing examples.
- Optionally add a link and a list of papers.

## Adding a Reference Paper
- Find the dataset entry in `benchmarks/datasets.yaml`.
- Add paper links under its `papers` field.

## Adding a Simulator

- Add a new entry to `benchmarks/simulators.yaml`.
- Include the name and optionally a link.

## Reporting Issues

Noticed something off? Please open an issue.
