# Contributing to SnakePokemon 🎮

First off, thank you for considering contributing to SnakePokemon! It's people like you that make SnakePokemon such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title
* Describe the exact steps which reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed after following the steps
* Explain which behavior you expected to see instead and why
* Include screenshots if possible

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* Use a clear and descriptive title
* Provide a step-by-step description of the suggested enhancement
* Provide specific examples to demonstrate the steps
* Describe the current behavior and explain which behavior you expected to see instead
* Explain why this enhancement would be useful

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Include screenshots and animated GIFs in your pull request whenever possible
* Follow the Python style guide
* Include thoughtfully-worded, well-structured tests
* Document new code
* End all files with a newline

## Style Guides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

### Python Style Guide

* Follow PEP 8 guidelines
* Use meaningful variable names
* Add comments for complex logic
* Keep functions focused and small
* Use type hints when possible

## Development Process

1. Fork the repo
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## Setting Up Development Environment

1. Clone your fork:
```bash
git clone https://github.com/your-username/snakepokemon.git
cd snakepokemon
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install readchar
```

## Project Structure

```
snakepokemon/
├── SnakePokemon.py      # Main game file
├── ClassPokemon.py      # Pokemon class definitions
└── InterfacesAndFunctions.py  # Game interfaces and utility functions
```

## Testing

Before submitting a pull request, please ensure:

1. Your code follows the style guide
2. You've added tests for new functionality
3. All tests pass
4. Your changes don't break existing functionality

## Documentation

* Update the README.md with details of changes if needed
* Update the docstrings for any new functions or classes
* Add comments for complex logic
* Update any relevant documentation

## Questions?

Feel free to open an issue for any questions you might have about contributing.

## License

By contributing, you agree that your contributions will be licensed under the MIT License. 
