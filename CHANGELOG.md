# Changelog

All notable changes to Syntax Highlighting will be documented here. You can click on each release number to be directed to a detailed log of all code commits for that particular release. The download links will direct you to the GitHub release page, allowing you to manually install a release if you want.

If you enjoy Syntax Highlighting, please consider supporting my work on Patreon, or by buying me a cup of coffee :coffee::

<p align="center">
<a href="https://www.patreon.com/glutanimate" rel="nofollow" title="Support me on Patreon 😄"><img src="https://glutanimate.com/logos/patreon_button.svg"></a>      <a href="https://ko-fi.com/X8X0L4YV" rel="nofollow" title="Buy me a coffee 😊"><img src="https://glutanimate.com/logos/kofi_button.svg"></a>
</p>

:heart: My heartfelt thanks goes out to everyone who has supported this add-on through their tips, contributions, or any other means (you know who you are!). All of this would not have been possible without you. Thank you for being awesome!

## [Unreleased]

    
## [2.0.2] - 2018-10-07

### Fixed

- workaround for double-curly-bracket support (which otherwise conflict with Anki's card template system)
    
## [2.0.1] - 2018-10-06

### Changed

- case-insensitive lexer sorting

## [2.0.0] - 2018-02-27

This is the first public release of my fork of Tiago Barroso's *Syntax Highlighting for Code* add-on. I would like to extend my heartfelt gratitude to all of what he has done for the Anki community over the years.

This update is meant to carry on his legacy by adding Anki 2.1 support, implementing some long-requested features, and refactoring major parts of the codebase. All of this was made possible through the generous support of a fellow Anki user who would like to remain anonymous.

An overview of the most important changes in this release follows below:

### Added

- **New**: Anki 2.1 compatibility
- **New**: Option to apply syntax highlighting via CSS (thanks to [Tim Rae](https://github.com/timrae/SyntaxHighlight)!)
- **New**: Ability to customize language selection and hotkey
- **New**: Ability to customize [syntax highlighting theme](https://help.farbox.com/pygments.html)
- **New**: Upgraded pygments from v1.6 to v2.2.0. This is a [major jump](http://pygments.org/docs/changelog/#version-2-2-0) and should come with a lot of added functionality in terms of supported languages and language features

### Fixed

- **Fixed**: Position options dialog correctly
- **Fixed**: Various improvements and bug fixes (e.g. the ImportErrors and KeyErrors frequently reported in earlier reviews)

## 2.0.0-beta - 2018-02-27

See version notes above.


[Unreleased]: https://github.com/glutanimate/syntax-highlighting/compare/v2.0.2...HEAD
[2.0.2]: https://github.com/glutanimate/syntax-highlighting/compare/v2.0.1...v2.0.2
[2.0.1]: https://github.com/glutanimate/syntax-highlighting/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/glutanimate/syntax-highlighting/compare/v2.0.0-beta...v2.0.0

-----

The format of this file is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).