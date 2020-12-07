# DeepStack Documentation
This repository contains the source code and content for **DeepStack AI Server** official documentation site [https://docs.deepstack.cc](https://docs.deepstack.cc), owned by [DeepQuest AI](https://deepquestai.com/) . The content of the documentation includes the following

- Installation instructions across all supported platforms
- Python, NodeJS and C# example codes for all supported `APIs and features`
- API Reference ( coming soon )
- End-to-end guides ( coming soon )

N.B: Updates to the `main` branch of this repository is deployed to the `Live` documentation site.

# Contribution
We welcome contributions from the open source community to this documentation. The following items are our priorities for the repository:

- Example codes for `Java`, `Swift`, `Golang`, `Rust` and `Matlab`.
- Commons problems and solutions
- Language specific instructions and guidelines

Feel free to submit a `pull request` to update the documentation. It will be reviewed and merged as appropriate, provided the guidelines below are followed and it passes the review process.

- The documentation is versioned as `1.x.x` . For a minor update such as 
    - typo fixes
    - missing link fixes
    - adding missing resources
    - add/change example media

    , make sure you edit 
    - `.github/workflows/publish.yml` and increase last number of the `tags` by 1. 
    - `src/conf.py` and change the `release` to same number as above

    E.g `v1.0.1` >> `v1.0.2`

- For updates like
    - adding example codes for new progreamming language
    - adding guidelines and/or new page

    , make sure you edit 
    - `.github/workflows/publish.yml` and increase middle number of the `tags` by 1 and set the last number to 0. 
    - `src/conf.py` and change the `release` to same number as above

    E.g `v1.0.1` >> `v1.1.0`

